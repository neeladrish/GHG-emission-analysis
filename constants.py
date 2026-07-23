# ==========================================
# SHARED PROJECT CONSTANTS
# ==========================================


# ------------------------------------------
# PROJECT COUNTRIES
# ------------------------------------------

COUNTRIES = [
    "Australia",
    "Brazil",
    "China",
    "Germany",
    "India",
    "Japan",
    "Russia",
    "South Africa",
    "United Kingdom",
    "United States"
]


# ------------------------------------------
# NON-SOVEREIGN / AGGREGATE ENTITIES
# ------------------------------------------

NON_SOVEREIGN = [

    # Continental / regional aggregates (OWID)
    "World",
    "Asia",
    "Europe",
    "Africa",
    "North America",
    "South America",
    "Oceania",

    # Continental / regional aggregates (GCP variants)
    "Africa (GCP)",
    "Asia (GCP)",
    "Europe (GCP)",
    "North America (GCP)",
    "South America (GCP)",
    "Oceania (GCP)",
    "Central America (GCP)",
    "Middle East (GCP)",

    # Sub-regional exclusion variants
    "Asia (excl. China and India)",
    "Europe (excl. EU-27)",
    "Europe (excl. EU-28)",
    "North America (excl. USA)",

    # European Union aggregates
    "European Union (27)",
    "European Union (28)",

    # Income / development groupings
    "High-income countries",
    "Low-income countries",
    "Upper-middle-income countries",
    "Lower-middle-income countries",
    "Least developed countries (Jones et al.)",

    # OECD / Non-OECD groupings
    "OECD (GCP)",
    "OECD (Jones et al.)",
    "Non-OECD (GCP)",

    # International transport components
    "International aviation",
    "International shipping",

    # Special / historical entries
    "Kuwaiti Oil Fires",
    "Kuwaiti Oil Fires (GCP)",
    "Ryukyu Islands (GCP)"
]


# ------------------------------------------
# TIME SETTINGS
# ------------------------------------------

TRAIN_CUTOFF = 2018

FORECAST_START = 2024

FORECAST_END = 2043


# ------------------------------------------
# MACHINE LEARNING SETTINGS
# ------------------------------------------

TARGET = "target_co2"


# Use the exact feature list from Week 3
FEATURES = [
    "year",
    "co2",
    "co2_per_capita",
    "co2_5yr_rolling_mean",
    "co2_lag1",
    "co2_lag2",
    "co2_lag3",
    "co2_yoy_pct_change",
    "ghg_intensity"
]