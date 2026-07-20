"""Offline Modbus TCP capture decoding for comms troubleshooting.

Reads a packet capture that someone else already took (classic pcap or
pcapng), reassembles the TCP streams, and decodes the Modbus TCP application
layer into frames, request/response transactions, and the field-diagnostic
summary: exception responses, unanswered requests, and response latency.

This module is strictly passive and offline. It never opens a network
interface and never transmits — on a live OT segment, injected traffic can
disturb a process that is controlling plant, so capture is left to a tool the
site has already approved and this package only reads the file.

Protocol constants (MBAP framing, function codes, exception codes) follow the
Modbus Application Protocol Specification V1.1b3, which modbus.org publishes
openly; no licensed table values are embedded.
"""

from __future__ import annotations

import socket
import struct
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

MODBUS_TCP_PORT = 502

_MBAP_HEADER_LEN = 7
_MODBUS_PROTOCOL_ID = 0
# The MBAP length field counts the unit id plus the PDU: at minimum a unit id
# and a function code, at most a unit id plus the spec's 253-byte PDU limit.
_MIN_MBAP_LENGTH = 2
_MAX_MBAP_LENGTH = 254
_EXCEPTION_MASK = 0x80

# Modbus Application Protocol Specification V1.1b3, section 5 (public codes).
FUNCTION_NAMES: dict[int, str] = {
    1: "Read Coils",
    2: "Read Discrete Inputs",
    3: "Read Holding Registers",
    4: "Read Input Registers",
    5: "Write Single Coil",
    6: "Write Single Register",
    7: "Read Exception Status",
    8: "Diagnostics",
    11: "Get Comm Event Counter",
    12: "Get Comm Event Log",
    15: "Write Multiple Coils",
    16: "Write Multiple Registers",
    17: "Report Server ID",
    20: "Read File Record",
    21: "Write File Record",
    22: "Mask Write Register",
    23: "Read/Write Multiple Registers",
    24: "Read FIFO Queue",
    43: "Encapsulated Interface Transport",
}

# Modbus Application Protocol Specification V1.1b3, section 7.
EXCEPTION_NAMES: dict[int, str] = {
    1: "Illegal Function",
    2: "Illegal Data Address",
    3: "Illegal Data Value",
    4: "Server Device Failure",
    5: "Acknowledge",
    6: "Server Device Busy",
    8: "Memory Parity Error",
    10: "Gateway Path Unavailable",
    11: "Gateway Target Device Failed To Respond",
}

# Function codes whose request PDU is (start address, quantity).
_ADDRESSED_READS = frozenset({1, 2, 3, 4})
_ADDRESSED_WRITES = frozenset({15, 16})
_SINGLE_WRITES = frozenset({5, 6})


# --------------------------------------------------------------- capture I/O


@dataclass(frozen=True)
class RawPacket:
    """One captured TCP segment, already narrowed to IPv4/TCP."""

    timestamp: float
    src_ip: str
    dst_ip: str
    src_port: int
    dst_port: int
    seq: int
    payload: bytes
    fin: bool
    rst: bool


_LINKTYPE_NULL = 0
_LINKTYPE_ETHERNET = 1
_LINKTYPE_RAW = 101
_LINKTYPE_LINUX_SLL = 113

_ETHERTYPE_IPV4 = 0x0800
_ETHERTYPE_VLAN = 0x8100
_IPPROTO_TCP = 6


def read_capture(pcap_path: str | Path) -> list[RawPacket]:
    """Parse a pcap or pcapng file into its IPv4/TCP segments, in capture order.

    Non-TCP and non-IPv4 traffic is skipped rather than raising: a real capture
    routinely contains ARP, UDP, and IPv6 alongside the Modbus conversation.
    """
    path = Path(pcap_path)
    if not path.exists():
        raise FileNotFoundError(f"capture not found: {path}")
    blob = path.read_bytes()
    if len(blob) < 4:
        raise ValueError(f"{path}: file is too short to be a pcap or pcapng capture")

    magic = blob[:4]
    if magic in (b"\xa1\xb2\xc3\xd4", b"\xd4\xc3\xb2\xa1", b"\xa1\xb2\x3c\x4d",
                 b"\x4d\x3c\xb2\xa1"):
        return _read_classic_pcap(blob, path)
    if magic == b"\x0a\x0d\x0d\x0a":
        return _read_pcapng(blob, path)
    raise ValueError(
        f"{path}: not a pcap or pcapng capture (unrecognised magic {magic.hex()})"
    )


def _read_classic_pcap(blob: bytes, path: Path) -> list[RawPacket]:
    magic = blob[:4]
    # A file written little-endian holds the magic reversed, so the byte order
    # on disk is the inverse of the literal constant.
    endian = "<" if magic in (b"\xd4\xc3\xb2\xa1", b"\x4d\x3c\xb2\xa1") else ">"
    # The 0xa1b23c4d variants timestamp in nanoseconds instead of microseconds.
    tick = 1e-9 if magic in (b"\xa1\xb2\x3c\x4d", b"\x4d\x3c\xb2\xa1") else 1e-6
    if len(blob) < 24:
        raise ValueError(f"{path}: truncated pcap global header")
    linktype = struct.unpack(endian + "I", blob[20:24])[0]

    packets: list[RawPacket] = []
    offset = 24
    while offset + 16 <= len(blob):
        ts_sec, ts_frac, incl_len, _orig_len = struct.unpack(
            endian + "IIII", blob[offset : offset + 16]
        )
        offset += 16
        data = blob[offset : offset + incl_len]
        if len(data) < incl_len:
            break  # truncated final record — take what framed cleanly
        offset += incl_len
        packet = _parse_link_frame(data, ts_sec + ts_frac * tick, linktype)
        if packet is not None:
            packets.append(packet)
    return packets


def _read_pcapng(blob: bytes, path: Path) -> list[RawPacket]:
    """Parse the block types that carry packets; skip everything else.

    Only Section Header, Interface Description, and Enhanced Packet blocks are
    interpreted. Timestamp resolution follows the ``if_tsresol`` option when
    present, defaulting to microseconds as the format specifies.
    """
    packets: list[RawPacket] = []
    endian = "<"
    linktypes: list[int] = []
    resolutions: list[float] = []
    offset = 0
    while offset + 12 <= len(blob):
        block_type = struct.unpack(endian + "I", blob[offset : offset + 4])[0]
        if block_type == 0x0A0D0D0A:
            # A new section restarts interface numbering and may flip endianness.
            byte_order = blob[offset + 8 : offset + 12]
            endian = "<" if byte_order == b"\x4d\x3c\x2b\x1a" else ">"
            linktypes, resolutions = [], []
        block_len = struct.unpack(endian + "I", blob[offset + 4 : offset + 8])[0]
        if block_len < 12 or offset + block_len > len(blob):
            break  # truncated or malformed tail — stop at the last good block
        body = blob[offset + 8 : offset + block_len - 4]

        if block_type == 0x00000001:  # Interface Description
            linktypes.append(struct.unpack(endian + "H", body[0:2])[0])
            resolutions.append(_pcapng_tsresol(body[8:], endian))
        elif block_type == 0x00000006:  # Enhanced Packet
            iface, ts_hi, ts_lo, cap_len, _orig = struct.unpack(
                endian + "IIIII", body[0:20]
            )
            data = body[20 : 20 + cap_len]
            linktype = linktypes[iface] if iface < len(linktypes) else _LINKTYPE_ETHERNET
            tick = resolutions[iface] if iface < len(resolutions) else 1e-6
            packet = _parse_link_frame(data, ((ts_hi << 32) | ts_lo) * tick, linktype)
            if packet is not None:
                packets.append(packet)
        offset += block_len
    if not linktypes and not packets:
        raise ValueError(f"{path}: pcapng file contains no readable packet blocks")
    return packets


def _pcapng_tsresol(options: bytes, endian: str) -> float:
    """Read the if_tsresol option (code 9); default microseconds if absent."""
    offset = 0
    while offset + 4 <= len(options):
        code, length = struct.unpack(endian + "HH", options[offset : offset + 4])
        if code == 0:  # opt_endofopt
            break
        value = options[offset + 4 : offset + 4 + length]
        if code == 9 and value:
            raw = value[0]
            # High bit set selects a power of two; otherwise a power of ten.
            return 2.0 ** -(raw & 0x7F) if raw & 0x80 else 10.0 ** -raw
        offset += 4 + length + ((-length) % 4)
    return 1e-6


def _parse_link_frame(data: bytes, timestamp: float, linktype: int) -> RawPacket | None:
    """Strip the link layer, then decode IPv4/TCP. None if not IPv4/TCP."""
    if linktype == _LINKTYPE_ETHERNET:
        if len(data) < 14:
            return None
        ethertype = struct.unpack(">H", data[12:14])[0]
        offset = 14
        if ethertype == _ETHERTYPE_VLAN:
            if len(data) < 18:
                return None
            ethertype = struct.unpack(">H", data[16:18])[0]
            offset = 18
        if ethertype != _ETHERTYPE_IPV4:
            return None
    elif linktype == _LINKTYPE_NULL:
        # Loopback captures prefix a 4-byte address family; 2 == AF_INET.
        if len(data) < 4:
            return None
        family = struct.unpack("<I", data[0:4])[0]
        if family not in (2, 0x02000000):
            return None
        offset = 4
    elif linktype == _LINKTYPE_LINUX_SLL:
        if len(data) < 16 or struct.unpack(">H", data[14:16])[0] != _ETHERTYPE_IPV4:
            return None
        offset = 16
    elif linktype == _LINKTYPE_RAW:
        offset = 0
    else:
        return None
    return _parse_ipv4_tcp(data[offset:], timestamp)


def _parse_ipv4_tcp(data: bytes, timestamp: float) -> RawPacket | None:
    if len(data) < 20 or (data[0] >> 4) != 4:
        return None
    ihl = (data[0] & 0x0F) * 4
    if ihl < 20 or len(data) < ihl:
        return None
    total_length = struct.unpack(">H", data[2:4])[0]
    if data[9] != _IPPROTO_TCP:
        return None
    src_ip = socket.inet_ntoa(data[12:16])
    dst_ip = socket.inet_ntoa(data[16:20])

    # Trust the IP total-length over the captured length: NICs pad frames up to
    # the 60-byte Ethernet minimum, and that padding is not stream data.
    ip_end = min(total_length, len(data)) if total_length else len(data)
    tcp = data[ihl:ip_end]
    if len(tcp) < 20:
        return None
    src_port, dst_port, seq = struct.unpack(">HHI", tcp[0:8])
    data_offset = (tcp[12] >> 4) * 4
    if data_offset < 20 or len(tcp) < data_offset:
        return None
    flags = tcp[13]
    return RawPacket(
        timestamp=timestamp,
        src_ip=src_ip,
        dst_ip=dst_ip,
        src_port=src_port,
        dst_port=dst_port,
        seq=seq,
        payload=tcp[data_offset:],
        fin=bool(flags & 0x01),
        rst=bool(flags & 0x04),
    )


# ------------------------------------------------------------ Modbus frames


@dataclass(frozen=True)
class ModbusFrame:
    """One decoded Modbus TCP application-layer message.

    ``start_address`` and ``quantity`` are populated for requests carrying an
    addressed read or write; they stay None on responses, whose PDU echoes the
    address only for some function codes and carries none for reads.
    """

    timestamp: float
    src_ip: str
    dst_ip: str
    transaction_id: int
    unit_id: int
    function_code: int
    is_request: bool
    is_exception: bool = False
    exception_code: int | None = None
    start_address: int | None = None
    quantity: int | None = None

    @property
    def function_name(self) -> str:
        return FUNCTION_NAMES.get(self.function_code, f"Function {self.function_code}")

    @property
    def exception_name(self) -> str | None:
        if self.exception_code is None:
            return None
        return EXCEPTION_NAMES.get(
            self.exception_code, f"Exception {self.exception_code}"
        )


class _FramingViolation(Exception):
    """The buffered bytes cannot be a valid Modbus TCP stream."""


_StreamKey = tuple[str, int, str, int]


@dataclass
class _Stream:
    """Reassembly state for one direction of one TCP connection."""

    buffer: bytearray = field(default_factory=bytearray)
    next_seq: int | None = None

    def accept(self, payload: bytes, seq: int | None) -> None:
        """Add a segment's bytes, dropping data already delivered."""
        if seq is None or self.next_seq is None:
            self.buffer.extend(payload)
            if seq is not None:
                self.next_seq = (seq + len(payload)) % 2**32
            return

        segment_end = (seq + len(payload)) % 2**32
        delta = _seq_delta(seq, self.next_seq)
        if delta < 0:
            # Retransmission: keep only the bytes past what we already hold.
            payload = payload[-delta:]
            if not payload:
                return
        elif delta > 0:
            # A hole: bytes were lost or reordered beyond what the capture saw,
            # so the buffered prefix can no longer be trusted. Resync here.
            self.buffer.clear()
        self.buffer.extend(payload)
        self.next_seq = segment_end


def _seq_delta(seq: int, expected: int) -> int:
    """Signed distance from ``expected`` to ``seq`` in 32-bit sequence space."""
    return ((seq - expected + 2**31) % 2**32) - 2**31


class ModbusStreamReassembler:
    """Turns captured TCP segments into complete Modbus TCP frames.

    TCP is a byte stream: one segment may carry a fragment of an ADU, several
    ADUs, or bytes that are not Modbus at all. Each direction of each
    connection is buffered separately and a frame is emitted only once a
    complete, validated ADU has arrived.
    """

    # Framing validation caps a buffered partial ADU at ~260 bytes, so total
    # reassembly memory stays bounded by max_streams * that.
    DEFAULT_MAX_STREAMS = 1024

    def __init__(
        self,
        server_port: int = MODBUS_TCP_PORT,
        max_streams: int = DEFAULT_MAX_STREAMS,
    ) -> None:
        if max_streams < 1:
            raise ValueError(f"max_streams must be at least 1, got {max_streams}")
        self._server_port = server_port
        self._max_streams = max_streams
        self._streams: dict[_StreamKey, _Stream] = {}

    @property
    def open_streams(self) -> int:
        """Directional streams currently holding reassembly state."""
        return len(self._streams)

    def feed(self, packet: RawPacket) -> list[ModbusFrame]:
        """Consume one captured segment; return every frame it completed."""
        key: _StreamKey = (
            packet.src_ip,
            packet.src_port,
            packet.dst_ip,
            packet.dst_port,
        )
        frames: list[ModbusFrame] = []
        if packet.payload:
            stream = self._touch(key)
            stream.accept(packet.payload, packet.seq)
            complete, poisoned = self._drain_complete_adus(stream.buffer)
            if poisoned:
                # Byte boundaries cannot be trusted after a framing violation:
                # drop this direction and resync on the next segment. ADUs that
                # framed cleanly before the violation still count.
                self._streams.pop(key, None)
            for adu in complete:
                frames.append(
                    _decode_adu(
                        adu,
                        timestamp=packet.timestamp,
                        src_ip=packet.src_ip,
                        dst_ip=packet.dst_ip,
                        is_request=packet.dst_port == self._server_port,
                    )
                )

        if packet.rst:
            # RST aborts the connection; FIN only ends the sender's direction.
            self._streams.pop(key, None)
            self._streams.pop(
                (packet.dst_ip, packet.dst_port, packet.src_ip, packet.src_port), None
            )
        elif packet.fin:
            self._streams.pop(key, None)
        return frames

    def _touch(self, key: _StreamKey) -> _Stream:
        """Fetch the stream as most-recently-active, evicting the LRU if full.

        dicts iterate in insertion order, so re-inserting on every touch keeps
        the least-recently-active stream first — that is the one evicted.
        """
        stream = self._streams.pop(key, None)
        if stream is None:
            stream = _Stream()
            if len(self._streams) >= self._max_streams:
                del self._streams[next(iter(self._streams))]
        self._streams[key] = stream
        return stream

    @classmethod
    def _drain_complete_adus(cls, buffer: bytearray) -> tuple[list[bytes], bool]:
        """Pop every complete ADU off the front of the buffer.

        Returns the ADUs plus a poisoned flag, set when the remaining bytes
        cannot be a valid MBAP header. A trailing partial ADU stays buffered.
        """
        adus: list[bytes] = []
        while True:
            try:
                adu = cls._next_complete_adu(buffer)
            except _FramingViolation:
                return adus, True
            if adu is None:
                return adus, False
            adus.append(adu)

    @staticmethod
    def _next_complete_adu(buffer: bytearray) -> bytes | None:
        """Pop one complete ADU off the front, or None to wait for more bytes."""
        if len(buffer) < _MBAP_HEADER_LEN:
            return None
        if int.from_bytes(buffer[2:4], "big") != _MODBUS_PROTOCOL_ID:
            raise _FramingViolation
        mbap_length = int.from_bytes(buffer[4:6], "big")
        if not _MIN_MBAP_LENGTH <= mbap_length <= _MAX_MBAP_LENGTH:
            raise _FramingViolation
        adu_len = _MBAP_HEADER_LEN - 1 + mbap_length
        if len(buffer) < adu_len:
            return None
        adu = bytes(buffer[:adu_len])
        del buffer[:adu_len]
        return adu


def _decode_adu(
    adu: bytes, *, timestamp: float, src_ip: str, dst_ip: str, is_request: bool
) -> ModbusFrame:
    """Decode one validated ADU into a frame, including the PDU's addresses."""
    transaction_id = int.from_bytes(adu[0:2], "big")
    unit_id = adu[6]
    raw_function = adu[7]
    is_exception = bool(raw_function & _EXCEPTION_MASK)
    function_code = raw_function & ~_EXCEPTION_MASK
    pdu = adu[7:]

    exception_code = pdu[1] if is_exception and len(pdu) >= 2 else None
    start_address: int | None = None
    quantity: int | None = None
    if is_request and not is_exception:
        if function_code in _ADDRESSED_READS or function_code in _ADDRESSED_WRITES:
            if len(pdu) >= 5:
                start_address, quantity = struct.unpack(">HH", pdu[1:5])
        elif function_code in _SINGLE_WRITES:
            if len(pdu) >= 5:
                start_address = struct.unpack(">H", pdu[1:3])[0]
                quantity = 1

    return ModbusFrame(
        timestamp=timestamp,
        src_ip=src_ip,
        dst_ip=dst_ip,
        transaction_id=transaction_id,
        unit_id=unit_id,
        function_code=function_code,
        is_request=is_request,
        is_exception=is_exception,
        exception_code=exception_code,
        start_address=start_address,
        quantity=quantity,
    )


def decode_frames(
    packets: list[RawPacket], server_port: int = MODBUS_TCP_PORT
) -> list[ModbusFrame]:
    """Reassemble captured segments into Modbus frames, in capture order."""
    reassembler = ModbusStreamReassembler(server_port=server_port)
    frames: list[ModbusFrame] = []
    for packet in packets:
        frames.extend(reassembler.feed(packet))
    return frames


# ------------------------------------------------------------- transactions


@dataclass(frozen=True)
class Transaction:
    """A request and the response that answered it, if one arrived."""

    request: ModbusFrame
    response: ModbusFrame | None = None

    @property
    def unanswered(self) -> bool:
        """True when no response was captured — the comms-dropout signature."""
        return self.response is None

    @property
    def latency_s(self) -> float | None:
        """Seconds from request to response; None when unanswered."""
        if self.response is None:
            return None
        return self.response.timestamp - self.request.timestamp

    @property
    def is_exception(self) -> bool:
        return self.response is not None and self.response.is_exception


def pair_transactions(frames: list[ModbusFrame]) -> list[Transaction]:
    """Match responses to their requests, in request order.

    Polling loops reuse transaction ids, so matching is FIFO within each
    (peer pair, unit, transaction id): the oldest outstanding request wins the
    next matching response.
    """
    pending: dict[tuple[str, str, int, int], list[ModbusFrame]] = defaultdict(list)
    answered: dict[int, ModbusFrame] = {}
    requests: list[ModbusFrame] = []

    for frame in frames:
        if frame.is_request:
            key = (frame.src_ip, frame.dst_ip, frame.unit_id, frame.transaction_id)
            pending[key].append(frame)
            requests.append(frame)
        else:
            key = (frame.dst_ip, frame.src_ip, frame.unit_id, frame.transaction_id)
            queue = pending.get(key)
            if queue:
                answered[id(queue.pop(0))] = frame

    return [Transaction(request=r, response=answered.get(id(r))) for r in requests]


# ----------------------------------------------------------------- summary


@dataclass(frozen=True)
class AddressSpan:
    """A distinct register range a client polls, and how often."""

    unit_id: int
    function_code: int
    start: int
    count: int
    polls: int

    @property
    def end(self) -> int:
        """Last address in the span (inclusive)."""
        return self.start + self.count - 1


def polled_addresses(frames: list[ModbusFrame]) -> list[AddressSpan]:
    """Distinct (unit, function, start, count) request spans, with poll counts.

    Diffing this against a design-time register map (``cst modbus-map``) shows
    what the field actually polls versus what the design says it should.
    """
    counts: dict[tuple[int, int, int, int], int] = defaultdict(int)
    for frame in frames:
        if frame.is_request and frame.start_address is not None:
            quantity = frame.quantity if frame.quantity is not None else 1
            counts[(frame.unit_id, frame.function_code, frame.start_address, quantity)] += 1
    return [
        AddressSpan(unit_id=u, function_code=fc, start=s, count=c, polls=n)
        for (u, fc, s, c), n in sorted(counts.items())
    ]


@dataclass(frozen=True)
class CaptureSummary:
    """Field-diagnostic totals for one capture."""

    frame_count: int
    request_count: int
    response_count: int
    exception_count: int
    unanswered_count: int
    units: list[int]
    by_function: dict[str, int]
    exceptions: list[ModbusFrame]
    max_latency_s: float | None
    mean_latency_s: float | None
    duration_s: float | None

    def report(self) -> str:
        """Render a plain-text block for a commissioning or fault record."""
        lines = [
            f"frames        : {self.frame_count}"
            f"  ({self.request_count} req / {self.response_count} resp)",
            f"unit ids      : {', '.join(str(u) for u in self.units) or '-'}",
        ]
        if self.duration_s is not None:
            lines.append(f"capture span  : {self.duration_s:.3f} s")
        for name, count in sorted(self.by_function.items()):
            lines.append(f"  {name:<34}{count}")
        if self.max_latency_s is not None and self.mean_latency_s is not None:
            lines.append(
                f"response time : mean {self.mean_latency_s * 1000:.2f} ms, "
                f"max {self.max_latency_s * 1000:.2f} ms"
            )
        lines.append(f"exceptions    : {self.exception_count}")
        lines.append(f"unanswered    : {self.unanswered_count}")
        return "\n".join(lines)


def summarize(frames: list[ModbusFrame]) -> CaptureSummary:
    """Reduce decoded frames to the totals an engineer reads first."""
    transactions = pair_transactions(frames)
    latencies = [t.latency_s for t in transactions if t.latency_s is not None]
    exceptions = [f for f in frames if f.is_exception]

    by_function: dict[str, int] = defaultdict(int)
    for frame in frames:
        by_function[frame.function_name] += 1

    timestamps = [f.timestamp for f in frames]
    return CaptureSummary(
        frame_count=len(frames),
        request_count=sum(1 for f in frames if f.is_request),
        response_count=sum(1 for f in frames if not f.is_request),
        exception_count=len(exceptions),
        unanswered_count=sum(1 for t in transactions if t.unanswered),
        units=sorted({f.unit_id for f in frames}),
        by_function=dict(by_function),
        exceptions=exceptions,
        max_latency_s=max(latencies) if latencies else None,
        mean_latency_s=sum(latencies) / len(latencies) if latencies else None,
        duration_s=(max(timestamps) - min(timestamps)) if timestamps else None,
    )
