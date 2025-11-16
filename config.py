# config.py

# API Keys (consider using environment variables for production)
CENSUS_API_KEY = "YOUR_CENSUS_API_KEY" # Replace with your actual key or load from .env

# Data Paths
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"
PROCESSED_DATA_FILE = f"{PROCESSED_DATA_DIR}/processed_county_data.parquet"

# Census API Configuration
CENSUS_YEAR = 2023
CENSUS_BASE_URL = f"https://api.census.gov/data/{CENSUS_YEAR}/acs/acs5"

# ACS Variables to fetch
ACS_VARS = {
    "median_income": "B19013_001E",
    "avg_hh_size": "B25010_001E",
    "sf_detached": "B25024_002E",
    "sf_attached": "B25024_003E"
}

# NOAA API Configuration (if direct API access is implemented later)
# For now, data is downloaded via direct URL in data_pipeline.py

# FEMA API Configuration (if direct API access is implemented later)
# For now, data is downloaded via direct URL in data_pipeline.py

# Years for disaster data
DISASTER_YEARS = [2022, 2023, 2024]
