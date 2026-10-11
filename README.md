# Dynamic County Matching

> **Status: early stage.** This repository currently holds the project plan and configuration only (`config.py`, `requirements.txt`). The pipeline, model and app described below are not built yet.

The goal is to find U.S. counties that are similar to a chosen county on demographics and disaster exposure. Peer-group matching like this is common in public policy, insurance and emergency planning, for example to compare recovery outcomes or benchmark one county against its closest peers.

## Planned approach

1. **Data:** demographic and housing data from the U.S. Census Bureau's [American Community Survey](https://www.census.gov/programs-surveys/acs) (5-year estimates), storm history from the [NOAA Storm Events Database](https://www.ncdc.noaa.gov/stormevents/) and disaster declarations from [FEMA](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2).
2. **Features:** per-capita and per-household ratios, disaster frequency and severity by type, and standardized indices so no single variable dominates.
3. **Matching:** k-nearest neighbors on the standardized features, with clustering (K-Means, hierarchical) to describe broader peer groups, and user-adjustable feature weights.
4. **Interpretability:** for each match, which features make the counties similar or different.
5. **App:** a Streamlit app to pick a county, adjust weights and see matches on a map.

## Configuration

`config.py` sets the ACS variables to fetch (median household income, average household size and housing type), the Census year (2023) and the disaster years (2022–2024). Add a free [Census API key](https://api.census.gov/data/key_signup.html) to a `.env` file as `CENSUS_API_KEY` rather than editing `config.py`.

## License

MIT. See [LICENSE](LICENSE).

---

Built by [Nishant Iyer](https://www.konnectingnots.com), Senior Associate at Capital One.
