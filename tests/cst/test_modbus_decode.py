"""Golden-value tests for the offline Modbus TCP capture decoder.

Captures are synthesised in-test rather than committed as binary fixtures, so
every byte under test is visible here and no opaque file can drift.
"""

from __future__ import annotations

import socket
import struct

import pytest

from cst.diagnostics import modbus_decode as md


# ---------------------------------------------------------------- builders


def _tcp_segment(
    src_ip: str,
    dst_ip: str,
    sport: int,
    dport: int,
    seq: int,
    payload: bytes,
    *,
    fin: bool = False,
    rst: bool = False,
    min_frame: int = 0,
) -> bytes:
    """One Ethernet/IPv4/TCP frame carrying ``payload``."""
    flags = 0x10 | (0x01 if fin else 0) | (0x04 if rst else 0)
    tcp = struct.pack(
        ">HHIIBBHHH", sport, dport, seq, 0, 5 << 4, flags, 8192, 0, 0
    )
    ip_payload = tcp + payload
    ip = struct.pack(
        ">BBHHHBBH4s4s",
        0x45,
        0,
        20 + len(ip_payload),
        1,
        0,
        64,
        6,  # TCP
        0,
        socket.inet_aton(src_ip),
        socket.inet_aton(dst_ip),
    )
    frame = b"\x00" * 6 + b"\x11" * 6 + b"\x08\x00" + ip + ip_payload
    if len(frame) < min_frame:
        # Real NICs pad short frames to the 60-byte Ethernet minimum; the
        # decoder must trim by IP total-length, not trust the captured tail.
        frame += b"\x00" * (min_frame - len(frame))
    return frame


def _pcap(frames: list[tuple[float, bytes]]) -> bytes:
    """Classic little-endian microsecond pcap, LINKTYPE_ETHERNET."""
    out = struct.pack("<IHHiIII", 0xA1B2C3D4, 2, 4, 0, 0, 65535, 1)
    for ts, data in frames:
        out += struct.pack(
            "<IIII", int(ts), round((ts - int(ts)) * 1_000_000), len(data), len(data)
        )
        out += data
    return out


def _pcapng(frames: list[tuple[float, bytes]]) -> bytes:
    """Minimal pcapng: SHB + IDB(Ethernet) + one EPB per frame."""
    shb = struct.pack("<IIIHHq", 0x0A0D0D0A, 28, 0x1A2B3C4D, 1, 0, -1) + struct.pack(
        "<I", 28
    )
    idb = struct.pack("<IIHHI", 0x00000001, 20, 1, 0, 65535) + struct.pack("<I", 20)
    out = shb + idb
    for ts, data in frames:
        pad = (-len(data)) % 4
        total = 32 + len(data) + pad
        micros = int(round(ts * 1_000_000))
        out += struct.pack(
            "<IIIIIII",
            0x00000006,
            total,
            0,
            micros >> 32,
            micros & 0xFFFFFFFF,
            len(data),
            len(data),
        )
        out += data + b"\x00" * pad + struct.pack("<I", total)
    return out


def _mbap(txn: int, unit: int, pdu: bytes) -> bytes:
    return struct.pack(">HHHB", txn, 0, len(pdu) + 1, unit) + pdu


CLIENT, SERVER = "192.168.1.50", "192.168.1.10"


def _read_holding_request(txn: int, start: int, qty: int, unit: int = 1) -> bytes:
    return _mbap(txn, unit, struct.pack(">BHH", 3, start, qty))


def _read_holding_response(txn: int, values: list[int], unit: int = 1) -> bytes:
    body = b"".join(struct.pack(">H", v) for v in values)
    return _mbap(txn, unit, struct.pack(">BB", 3, len(body)) + body)


def _exception(txn: int, fc: int, code: int, unit: int = 1) -> bytes:
    return _mbap(txn, unit, struct.pack(">BB", fc | 0x80, code))


def _write(tmp_path, data: bytes, name: str = "capture.pcap"):
    path = tmp_path / name
    path.write_bytes(data)
    return path


def _poll(tmp_path, name="capture.pcap", builder=_pcap):
    """A single request/response exchange, 12.5 ms apart."""
    return _write(
        tmp_path,
        builder(
            [
                (
                    1000.0,
                    _tcp_segment(
                        CLIENT, SERVER, 51000, 502, 1, _read_holding_request(7, 100, 2)
                    ),
                ),
                (
                    1000.0125,
                    _tcp_segment(
                        SERVER, CLIENT, 502, 51000, 1, _read_holding_response(7, [11, 22])
                    ),
                ),
            ]
        ),
        name,
    )


# ------------------------------------------------------------ capture read


def test_reads_classic_pcap(tmp_path):
    packets = md.read_capture(_poll(tmp_path))
    assert [p.src_port for p in packets] == [51000, 502]
    assert packets[0].dst_ip == SERVER
    assert packets[0].timestamp == pytest.approx(1000.0)


def test_reads_pcapng(tmp_path):
    packets = md.read_capture(_poll(tmp_path, "capture.pcapng", _pcapng))
    assert len(packets) == 2
    assert packets[1].timestamp == pytest.approx(1000.0125, abs=1e-6)


def test_ethernet_padding_is_trimmed(tmp_path):
    """A 4-byte PDU in a 60-byte frame must not absorb the padding."""
    request = _read_holding_request(1, 0, 1)
    path = _write(
        tmp_path,
        _pcap([(1.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1, request, min_frame=60))]),
    )
    assert md.read_capture(path)[0].payload == request


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        md.read_capture("/nonexistent/capture.pcap")


def test_unknown_format_raises(tmp_path):
    path = _write(tmp_path, b"not a capture file at all")
    with pytest.raises(ValueError, match="not a pcap"):
        md.read_capture(path)


def test_non_tcp_traffic_ignored(tmp_path):
    """A UDP frame yields no packets — it cannot carry Modbus TCP."""
    udp = struct.pack(">HHHH", 5000, 502, 8, 0)
    ip = struct.pack(
        ">BBHHHBBH4s4s", 0x45, 0, 28, 1, 0, 64, 17, 0,
        socket.inet_aton(CLIENT), socket.inet_aton(SERVER),
    )
    frame = b"\x00" * 6 + b"\x11" * 6 + b"\x08\x00" + ip + udp
    assert md.read_capture(_write(tmp_path, _pcap([(1.0, frame)]))) == []


# ----------------------------------------------------------------- decode


def test_decodes_request_and_response(tmp_path):
    frames = md.decode_frames(md.read_capture(_poll(tmp_path)))
    assert len(frames) == 2

    req, resp = frames
    assert req.is_request and not resp.is_request
    assert req.transaction_id == 7 and req.unit_id == 1
    assert req.function_code == 3
    assert req.function_name == "Read Holding Registers"
    assert req.start_address == 100
    assert req.quantity == 2
    assert not req.is_exception
    assert resp.transaction_id == 7


def test_adu_split_across_segments(tmp_path):
    """A PDU straddling two TCP segments still decodes once, and only once."""
    adu = _read_holding_request(9, 40, 4)
    path = _write(
        tmp_path,
        _pcap(
            [
                (1.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1, adu[:5])),
                (1.001, _tcp_segment(CLIENT, SERVER, 5, 502, 1 + 5, adu[5:])),
            ]
        ),
    )
    frames = md.decode_frames(md.read_capture(path))
    assert len(frames) == 1
    assert frames[0].transaction_id == 9
    assert frames[0].start_address == 40


def test_multiple_adus_in_one_segment(tmp_path):
    """Pipelined requests in a single segment all decode, in order."""
    blob = _read_holding_request(1, 0, 1) + _read_holding_request(2, 8, 1)
    path = _write(
        tmp_path, _pcap([(1.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1, blob))])
    )
    frames = md.decode_frames(md.read_capture(path))
    assert [f.transaction_id for f in frames] == [1, 2]


def test_retransmission_not_double_counted(tmp_path):
    """The same segment seen twice must yield one frame, not two."""
    adu = _read_holding_request(3, 0, 1)
    seg = _tcp_segment(CLIENT, SERVER, 5, 502, 1, adu)
    path = _write(tmp_path, _pcap([(1.0, seg), (1.05, seg)]))
    assert len(md.decode_frames(md.read_capture(path))) == 1


def test_exception_response_decoded(tmp_path):
    path = _write(
        tmp_path,
        _pcap(
            [
                (1.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1, _read_holding_request(4, 9999, 1))),
                (1.01, _tcp_segment(SERVER, CLIENT, 502, 5, 1, _exception(4, 3, 2))),
            ]
        ),
    )
    frames = md.decode_frames(md.read_capture(path))
    exc = frames[1]
    assert exc.is_exception
    assert exc.function_code == 3
    assert exc.exception_code == 2
    assert exc.exception_name == "Illegal Data Address"


def test_non_modbus_stream_produces_no_frames(tmp_path):
    """Traffic on port 502 that is not Modbus must not fabricate frames."""
    path = _write(
        tmp_path,
        _pcap([(1.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1, b"GET / HTTP/1.1\r\n\r\n"))]),
    )
    assert md.decode_frames(md.read_capture(path)) == []


def test_custom_server_port(tmp_path):
    """Direction is decided by the server port, so a bench port must work."""
    path = _write(
        tmp_path,
        _pcap([(1.0, _tcp_segment(CLIENT, SERVER, 5, 5020, 1, _read_holding_request(1, 0, 1)))]),
    )
    packets = md.read_capture(path)
    assert md.decode_frames(packets, server_port=5020)[0].is_request
    assert not md.decode_frames(packets, server_port=502)[0].is_request


# ------------------------------------------------------------- transactions


def test_pairs_transactions_and_measures_latency(tmp_path):
    txns = md.pair_transactions(md.decode_frames(md.read_capture(_poll(tmp_path))))
    assert len(txns) == 1
    assert txns[0].response is not None
    assert txns[0].latency_s == pytest.approx(0.0125)
    assert not txns[0].unanswered


def test_unanswered_request_flagged(tmp_path):
    """A request with no reply is the comms-dropout signature."""
    path = _write(
        tmp_path,
        _pcap([(1.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1, _read_holding_request(1, 0, 1)))]),
    )
    txns = md.pair_transactions(md.decode_frames(md.read_capture(path)))
    assert len(txns) == 1
    assert txns[0].unanswered
    assert txns[0].latency_s is None


def test_transaction_id_reuse_pairs_in_order(tmp_path):
    """Polling loops reuse transaction ids; each reply pairs with its own request."""
    path = _write(
        tmp_path,
        _pcap(
            [
                (1.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1, _read_holding_request(1, 0, 1))),
                (1.01, _tcp_segment(SERVER, CLIENT, 502, 5, 1, _read_holding_response(1, [1]))),
                (2.0, _tcp_segment(CLIENT, SERVER, 5, 502, 13, _read_holding_request(1, 0, 1))),
                (2.02, _tcp_segment(SERVER, CLIENT, 502, 5, 12, _read_holding_response(1, [2]))),
            ]
        ),
    )
    txns = md.pair_transactions(md.decode_frames(md.read_capture(path)))
    assert [t.latency_s for t in txns] == [pytest.approx(0.01), pytest.approx(0.02)]


# ---------------------------------------------------------------- summary


def test_summary_counts(tmp_path):
    path = _write(
        tmp_path,
        _pcap(
            [
                (1.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1, _read_holding_request(1, 0, 1))),
                (1.01, _tcp_segment(SERVER, CLIENT, 502, 5, 1, _read_holding_response(1, [5]))),
                (2.0, _tcp_segment(CLIENT, SERVER, 5, 502, 13, _read_holding_request(2, 9, 1))),
                (2.01, _tcp_segment(SERVER, CLIENT, 502, 5, 12, _exception(2, 3, 2))),
                (3.0, _tcp_segment(CLIENT, SERVER, 5, 502, 25, _read_holding_request(3, 0, 1))),
            ]
        ),
    )
    summary = md.summarize(md.decode_frames(md.read_capture(path)))
    assert summary.frame_count == 5
    assert summary.request_count == 3
    assert summary.response_count == 2
    assert summary.exception_count == 1
    assert summary.unanswered_count == 1
    assert summary.units == [1]
    assert summary.by_function["Read Holding Registers"] == 5
    assert summary.max_latency_s == pytest.approx(0.01)


def test_summary_of_empty_capture_is_zeroed():
    summary = md.summarize([])
    assert summary.frame_count == 0
    assert summary.max_latency_s is None
    assert summary.by_function == {}


def test_polled_addresses_reports_register_span(tmp_path):
    """Feeds the diff against a design-time register map."""
    path = _write(
        tmp_path,
        _pcap(
            [
                (1.0, _tcp_segment(CLIENT, SERVER, 5, 502, 1, _read_holding_request(1, 100, 4))),
                (2.0, _tcp_segment(CLIENT, SERVER, 5, 502, 13, _read_holding_request(2, 200, 2))),
            ]
        ),
    )
    spans = md.polled_addresses(md.decode_frames(md.read_capture(path)))
    assert spans == [
        md.AddressSpan(unit_id=1, function_code=3, start=100, count=4, polls=1),
        md.AddressSpan(unit_id=1, function_code=3, start=200, count=2, polls=1),
    ]
