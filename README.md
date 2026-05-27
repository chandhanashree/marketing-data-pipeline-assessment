# Marketing Data Pipeline Assessment
Tacheon assessment submission

## Project Overview

This project demonstrates a simple data engineering pipeline using a public weather API.

The pipeline:
1. Fetches weather forecast data from Open-Meteo API
2. Transforms the raw JSON into structured tabular data
3. Creates derived analytical fields
4. Demonstrates SQL-based analysis

---

## Tech Stack

- Python
- Pandas
- Requests
- SQL
- Google BigQuery
- GitHub

---

## Project Structure

task1/
- product_brief.md

task2/
- fetch_data.py
- transform_data.py
- analysis.sql

---

## API Used

Open-Meteo Weather API:
https://open-meteo.com/

---

## Features

- API data ingestion
- Data transformation
- Derived metric calculation
- SQL analytical query

---

## Example Derived Field

temp_range = max_temp - min_temp

---

## Implemented Features

- BigQuery integration
- Automated scheduling
- Logging and monitoring
- Incremental data loads
- Dashboard visualization