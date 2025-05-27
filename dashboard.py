import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Conexão com o banco
conn = sqlite3.connect("database/covid_data.db")
df = pd.read_sql_query("SELECT * FROM covid_data", conn)

# Layout da dashboard
st.set_page_config(page_title="📊 Dashboard COVID-19", layout="wide")

st.title("📊 Dashboard de Dados COVID-19 - Brasil")

# Filtros
estados = st.multiselect("Filtrar por estado(s):", options=df['estado'].unique(), default=df['estado'].unique())

df_filtrado = df[df['estado'].isin(estados)]

# Tabela de dados
st.subheader("🗂️ Tabela de Dados Filtrados")
st.dataframe(df_filtrado)

# Gráfico de casos por estado
st.subheader("📍 Casos por Estado")
casos_estado = df_filtrado.groupby("estado")["casos"].sum().reset_index()
fig1 = px.bar(casos_estado, x="estado", y="casos", color="estado", title="Total de Casos por Estado")
st.plotly_chart(fig1, use_container_width=True)

# Gráfico de evolução temporal
st.subheader("📈 Evolução Temporal de Casos")
df_filtrado["data"] = pd.to_datetime(df_filtrado["data"])
casos_tempo = df_filtrado.groupby("data")["casos"].sum().reset_index()
fig2 = px.line(casos_tempo, x="data", y="casos", title="Casos Acumulados ao Longo do Tempo")
st.plotly_chart(fig2, use_container_width=True)

# Rodapé
st.markdown("---")
st.markdown("👩‍💻 Feito por Let com 💖")
