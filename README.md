# 🌍 Pipeline de Dados com Arquitetura Bronze, Silver e Gold

Este projeto demonstra a implementação de uma **arquitetura de medallion** (camadas **Bronze → Silver → Gold**) em um pipeline de engenharia de dados, aplicando boas práticas de ingestão, transformação e análise de dados.

O objetivo é extrair dados públicos de uma **API de países** ([restcountries.com](https://restcountries.com/v3.1/all)), tratar e organizar esses dados em camadas estruturadas, e por fim gerar agregações e visualizações para análises exploratórias.

---

## 🏗️ Arquitetura de Camadas (Medalhões)

### 🟫 Camada Bronze — Raw / Bruta

- 🔹 Extração direta da API: [`https://restcountries.com/v3.1/all`](https://restcountries.com/v3.1/all)
- 🔹 Dados salvos **sem modificação** no formato `.json`
- 🔹 Exemplo de entrada:

```json
{
  "capital": ["Beijing"],
  "languages": {"zho": "Chinese"}
}
```

🪙 Camada Silver — Limpeza e Padronização
🔹 Transformações aplicadas com Python e Pandas:

Extração da capital como string

Conversão dos idiomas para lista

Cálculo do número de idiomas

🔹 Dados salvos no formato .parquet (colunar, otimizado)

🔹 Exemplo de saída:

```json
{
  "capital": "Beijing",
  "languages": ["Chinese"],
  "num_languages": 1
}
```

🥇 Camada Gold — Agregações e Insights
🔹 Criação de duas visões analíticas:

languages_most_spoken.parquet — Idiomas mais falados

capitals_by_language_count.parquet — Capitais com mais idiomas oficiais

🔹 Dados prontos para visualização e análises de negócio

📊 Visualização (Streamlit)
Foi construído um dashboard interativo usando Streamlit que permite:

Visualizar os idiomas mais falados

Ver quais capitais têm mais idiomas oficiais

Ajustar número de idiomas exibidos

Interagir com os dados em tempo real

▶️ Para rodar o dashboard:
bash
Copy
Edit
streamlit run scr/app.py
🛠️ Ferramentas Utilizadas
Etapa	Ferramenta
Extração	requests, json
Transformação	pandas, pyarrow
Armazenamento	.parquet (colunar)
Visualização	streamlit
Organização	venv, requirements.txt
Engenharia	Arquitetura Bronze → Silver → Gold

📁 Estrutura do Projeto
```plaintext
pipeline-economia/
├── data/
│   ├── bronze/         ← dados brutos extraídos da API
│   ├── silver/         ← dados tratados e padronizados
│   └── gold/           ← dados agregados prontos para análise
├── scr/
│   ├── extract.py      ← coleta dados da API
│   ├── transform.py    ← trata e padroniza os dados
│   ├── aggregate.py    ← realiza agregações analíticas
│   └── app.py          ← dashboard interativo (Streamlit)
├── requirements.txt
└── README.md
```
📘 Aprendizados
✔️ Compreensão prática da arquitetura de dados em camadas (Bronze → Silver → Gold)

✔️ Manipulação de dados estruturados e semiestruturados com Pandas

✔️ Armazenamento eficiente com o formato .parquet

✔️ Construção de dashboards com Streamlit

✔️ Organização e modularização de pipelines de dados

🚀 Próximos passos (ideias de melhoria)
Orquestrar com Apache Airflow

Containerizar com Docker

Armazenar os dados em um Data Lake (ex: MinIO, S3)

Adicionar testes e logs com logging

Fazer deploy com Streamlit Cloud ou servidor web

📎 Referências
🌐 RestCountries API

📚 Pandas - Parquet Docs

🧱 Arquitetura Medallion (Databricks)

💻 Streamlit

Desenvolvido por [Macauli Missouri] 💻
