"""Control System Tools (cst) — engineering toolkit for controls/automation work.

Domain subpackages:
    common          shared units, citations, and standards-table loading
    calc            electrical design calculators (voltage drop, thermal, ...)
    motion          servo/encoder scaling and conversion utilities

Every calculator returns a ``CalcResult`` carrying the numeric answer plus the
standard/formula citations and the assumptions used, so results are traceable
in design documentation.

Calculation logic is committed and open; licensed standard table values
(NEC/UL/IEC tables) are NOT stored in this repository — they load at runtime
from ``data/standards_tables/`` which each user populates from their own
licensed copies. See data/standards_tables/README.md.
"""

__version__ = "0.2.0"
