import requests
import pandas as pd

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 13.08,
    "longitude": 80.27,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "auto"
}

response = requests.get(URL, params=params)

data = response.json()

print(data)