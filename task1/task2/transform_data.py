import pandas as pd

data = {
    "date": ["2026-05-26", "2026-05-27"],
    "max_temp": [39.4, 39.8],
    "min_temp": [29.9, 29.3]
}

df = pd.DataFrame(data)

df["temp_range"] = df["max_temp"] - df["min_temp"]

print(df)