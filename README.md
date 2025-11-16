# Dynamic County Matching - Godly Python Analysis

## Project Overview

This project aims to deliver a "10/10 godly analysis" for dynamically identifying and comparing U.S. counties. Moving beyond simple data aggregation, this Python-centric solution leverages advanced data science techniques, machine learning, and interactive visualizations to provide deep insights into county similarities based on demographic and disaster profiles. The ultimate goal is to offer a robust, interpretable, and user-friendly platform for exploring county characteristics and relationships.

## Core Components

1.  **Robust Data Pipeline:** Enhanced data fetching, cleaning, and storage from diverse sources.
2.  **Advanced Feature Engineering:** Creation of meaningful derived and engineered features.
3.  **Dynamic County Matching (Machine Learning):** Implementation of sophisticated clustering or similarity algorithms.
4.  **In-depth Exploratory Data Analysis (EDA):** Comprehensive statistical analysis and pattern discovery.
5.  **Interactive Geospatial & Statistical Visualizations:** Clear and interactive presentation of findings.
6.  **Model Interpretability:** Understanding *why* counties are matched.
7.  **Interactive Web Application:** A user-friendly interface for exploring the analysis.
8.  **Code Quality & Best Practices:** Modular code, testing, documentation, and environment management.

## Project Structure

```
.
├── README.md
├── requirements.txt
├── config.py                 # Centralized configuration for API keys, paths, etc.
├── data/
│   ├── raw/                  # Original large datasets (e.g., DisasterDeclarationsSummaries.csv)
│   └── processed/            # Processed data (e.g., processed_county_data.parquet)
├── src/
│   ├── data_pipeline.py      # Fetches, cleans, and merges raw data
│   ├── feature_engineering.py# Creates derived and engineered features
│   ├── matching_model.py     # Implements county matching/clustering logic
│   ├── analysis.py           # Scripts for in-depth EDA and statistical analysis
│   ├── visualization.py      # Functions for generating plots (static and interactive)
│   └── app.py                # The Streamlit/Dash interactive web application
├── notebooks/
│   ├── exploratory_eda.ipynb # For initial EDA and data exploration
│   └── model_prototyping.ipynb# For experimenting with matching algorithms
├── tests/
│   ├── test_data_pipeline.py
│   ├── test_feature_engineering.py
│   └── test_matching_model.py
├── .env                      # Environment variables (e.g., API keys - ignored by Git)
└── .gitignore
```

## How It Works

1.  **Configuration:** Set up your API keys and other parameters in `config.py` and `.env`.
2.  **Data Pipeline:** Run `src/data_pipeline.py` to fetch raw data from Census, NOAA, and FEMA, clean it, and save it to `data/processed/processed_county_data.parquet`.
3.  **Feature Engineering:** `src/feature_engineering.py` takes the processed data and generates advanced features.
4.  **Matching Model:** `src/matching_model.py` applies machine learning algorithms (e.g., clustering, k-nearest neighbors) to identify similar counties.
5.  **Analysis & Visualization:** `src/analysis.py` and `src/visualization.py` are used for in-depth statistical analysis and generating various plots.
6.  **Interactive Web Application:** `src/app.py` (using Streamlit or Dash) provides a user-friendly interface to interact with the model, select counties, customize matching criteria, and explore results through dynamic tables, charts, and maps.

## Getting Started

### Prerequisites

*   **Python 3.x**
*   **Git**
*   **Census API Key:** Obtain a free API key from [https://api.census.gov/data/key_signup.html](https://api.census.gov/data/key_signup.html).

### Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/Dynamic-County-Matching.git
    cd Dynamic-County-Matching
    ```
2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On macOS/Linux:
    source .venv/bin/activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure API Keys:**
    *   Create a `.env` file in the project root.
    *   Add your Census API key: `CENSUS_API_KEY="your_census_api_key_here"`
    *   (Optional) Add other API keys if you expand data sources.
5.  **Run the Data Pipeline:**
    ```bash
    python src/data_pipeline.py
    ```
    This will fetch and process the raw data, saving it to `data/processed/`.
6.  **Run the Interactive Web Application:**
    ```bash
    streamlit run src/app.py
    ```
    (If using Streamlit. Adjust command for Dash if chosen.)
    This will open the interactive application in your web browser.

## Data Sources

*   **U.S. Census Bureau (American Community Survey):** Demographic and socio-economic data.
*   **National Oceanic and Atmospheric Administration (NOAA) Storm Events Database:** Historical storm event data.
*   **Federal Emergency Management Agency (FEMA) Disaster Declarations Summaries:** Official disaster declaration data.
*   **(Potential Additions):** Geospatial data (e.g., county boundaries), economic indicators, environmental data.

## Key Features of the Godly Analysis

*   **Advanced Feature Engineering:** Creation of composite indices, ratios, and geospatial features.
*   **Machine Learning for Matching:** Utilizes clustering (K-Means, DBSCAN, Hierarchical) and k-nearest neighbors for robust county similarity.
*   **Interactive Web Application:** User-friendly interface for dynamic county selection, feature weighting, algorithm choice, and real-time visualization of results.
*   **Comprehensive Visualizations:** Interactive choropleth maps, scatter plots (with dimensionality reduction), radar charts, and comparative bar plots using `plotly` or `bokeh`.
*   **Model Interpretability:** Tools and visualizations to understand the factors driving county similarities.
*   **Modular & Testable Codebase:** Well-structured Python modules with unit tests for reliability.
*   **Reproducible Environment:** `requirements.txt` and virtual environment setup.

## Future Enhancements

*   **Predictive Modeling:** Develop models to predict future disaster impacts or recovery times based on county characteristics.
*   **Time-Series Analysis:** Incorporate more extensive historical data and time-series models to analyze trends and dynamic changes.
*   **More Data Sources:** Integrate additional datasets (e.g., climate data, economic indicators, health data).
*   **Advanced Geospatial Analysis:** Integrate `geopandas` for more sophisticated spatial operations and visualizations.
*   **User Authentication/Persistence:** For saving user-defined matching profiles.
*   **Deployment to Cloud Platform:** Deploy the web application to a cloud service (e.g., AWS, Azure, GCP).

## Author

[Your Name/GitHub Profile Link]
[Your Contact Information (Optional)]