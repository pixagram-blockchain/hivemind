"""Chain-specific symbol configuration and helpers."""

from __future__ import annotations

import os
from typing import Dict, Final


def _env(name: str, default: str) -> str:
    value = os.getenv(name)
    if value is None:
        return default
    value = value.strip()
    return value or default


# Canonical asset symbols for the chain. Override via environment for forks.
HIVE_SYMBOL: Final[str] = _env("HIVEMIND_HIVE_SYMBOL", "HIVE")
HBD_SYMBOL: Final[str] = _env("HIVEMIND_HBD_SYMBOL", "HBD")
VESTS_SYMBOL: Final[str] = "VESTS"


LEGACY_SYMBOL_ALIASES: Final[Dict[str, str]] = {
    HIVE_SYMBOL: HIVE_SYMBOL,
    HBD_SYMBOL: HBD_SYMBOL,
    VESTS_SYMBOL: VESTS_SYMBOL,
    "HIVE": HIVE_SYMBOL,
    "HBD": HBD_SYMBOL,
    "STEEM": HIVE_SYMBOL,
    "SBD": HBD_SYMBOL,
}


def canonical_symbol(symbol: str) -> str:
    """Return canonical symbol for a possibly legacy symbol."""
    return LEGACY_SYMBOL_ALIASES.get(symbol, symbol)


NAI_MAP: Final[Dict[str, str]] = {
    "@@000000013": HBD_SYMBOL,
    "@@000000021": HIVE_SYMBOL,
    "@@000000037": VESTS_SYMBOL,
}

NAI_PRECISION: Final[Dict[str, int]] = {
    "@@000000013": 3,
    "@@000000021": 3,
    "@@000000037": 6,
}

UNIT_NAI: Final[Dict[str, str]] = {
    HBD_SYMBOL: "@@000000013",
    HIVE_SYMBOL: "@@000000021",
    VESTS_SYMBOL: "@@000000037",
}


def sql_template_vars() -> Dict[str, str]:
    """Variables for SQL template substitution."""
    return {
        "HIVE_SYMBOL": HIVE_SYMBOL,
        "HBD_SYMBOL": HBD_SYMBOL,
        "VESTS_SYMBOL": VESTS_SYMBOL,
    }
