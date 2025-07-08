import streamlit as st
import pandas as pd

# Título
st.title("🌍 Dashboard de Países e Idiomas (Camada Gold)")

# Carregar dados
df_lang = pd.read_parquet("data/gold/languages_most_spoken.parquet")
df_cap = pd.read_parquet("data/gold/capitals_by_language_count.parquet")

# Seção 1: Idiomas mais falados
st.subheader("🗣️ Idiomas mais falados no mundo (por número de países)")
top_n = st.slider("Quantos idiomas exibir?", min_value=5, max_value=30, value=10)
st.bar_chart(df_lang.head(top_n).set_index("language"))

# Seção 2: Capitais com mais idiomas oficiais
st.subheader("🏙️ Capitais com mais idiomas oficiais")
st.dataframe(df_cap.head(20))
