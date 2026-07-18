"""
Sector-specific valuation profiles.

These are starting defaults and will be refined over time.
"""

SECTOR_VALUATION_PROFILES = {

    "Technology": {
        "pe": 35,
        "pb": 8,
        "peg": 2.0,
        "ev_ebitda": 22,
    },

    "Healthcare": {
        "pe": 40,
        "pb": 7,
        "peg": 2.2,
        "ev_ebitda": 24,
    },

    "Financial Services": {
        "pe": 20,
        "pb": 2.5,
        "peg": 1.8,
        "ev_ebitda": 15,
    },

    "Consumer Defensive": {
        "pe": 30,
        "pb": 8,
        "peg": 2.0,
        "ev_ebitda": 20,
    },

    "Industrials": {
        "pe": 25,
        "pb": 4,
        "peg": 1.8,
        "ev_ebitda": 18,
    },

    "default": {
        "pe": 25,
        "pb": 4,
        "peg": 1.5,
        "ev_ebitda": 15,
    },
}