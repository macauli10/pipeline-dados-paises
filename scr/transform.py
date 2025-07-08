import json
import pandas as pd
from datetime import datetime
from pathlib import Path

silver_dir = Path("data/silver")
silver_dir.mkdir(parents=True, exist_ok=True)


bronze_path = f"data/bronze/countries_raw_{datetime.today().date()}.json"
silver_path = silver_dir / f"countries_clean_{datetime.today().date()}.parquet"


with open(bronze_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)


clean_data = []
for country in raw_data:
    capital = country.get("capital", [None])[0]
    languages = list(country.get("languages", {}).values())
    clean_data.append({
        "capital": capital,
        "languages": languages,
        "num_languages": len(languages)
    })

df = pd.DataFrame(clean_data)
df.to_parquet(silver_path, index=False)
print(f"[✔] Dados salvos na camada Silver: {silver_path}")
