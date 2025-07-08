import requests
import json
from datetime import datetime
from pathlib import Path

url = "https://restcountries.com/v3.1/independent?status=true&fields=languages,capital"
response = requests.get(url)
data = response.json()

Path("data/bronze").mkdir(parents=True, exist_ok=True)
file_path = f"data/bronze/countries_raw_{datetime.today().date()}.json"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
