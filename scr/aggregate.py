import pandas as pd
from datetime import datetime
from pathlib import Path

silver_path = f"data/silver/countries_clean_{datetime.today().date()}.parquet"
gold_dir = "data/gold"
Path(gold_dir).mkdir(parents=True, exist_ok=True)


df = pd.read_parquet(silver_path)

langs = df.explode("languages")
langs_count = langs["languages"].value_counts().reset_index()
langs_count.columns = ["language", "num_countries"]
langs_count.to_parquet(f"{gold_dir}/languages_most_spoken.parquet", index=False)



df_langs = df[["capital", "num_languages"]].dropna()
df_langs_sorted = df_langs.sort_values(by="num_languages", ascending=False)
df_langs_sorted.to_parquet(f"{gold_dir}/capitals_by_language_count.parquet", index=False)

print("[✔] Agregações salvas na camada Gold.")
