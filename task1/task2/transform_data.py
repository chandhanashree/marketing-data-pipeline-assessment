import pandas as pd
from google.cloud import bigquery

data = {
    "date": ["2026-05-26", "2026-05-27"],
    "max_temp": [39.4, 39.8],
    "min_temp": [29.9, 29.3]
}

df = pd.DataFrame(data)

df["temp_range"] = df["max_temp"] - df["min_temp"]

print(df)

client = bigquery.Client()

table_id = "marketing-pipeline-497613.weather_dataset.weather_data"

job = client.load_table_from_dataframe(df, table_id)

job.result()

print("Loaded data into BigQuery")