# 🦠 ETL de Dados COVID-19

Este projeto implementa um pipeline **ETL** (Extração, Transformação e Carga) utilizando dados reais da COVID-19 no Brasil.

---

## ⚙️ Tecnologias utilizadas

- Python 3
- requests
- pandas
- sqlite3
- Git & GitHub

---

## 📌 Objetivo

Criar uma aplicação simples e funcional que:

- Faça a extração de dados COVID-19 a partir de uma fonte pública
- Realize a transformação dos dados brutos
- Armazene os dados processados em um banco SQLite local

---

## 🗂️ Estrutura do projeto

etl-dados-covid/
├── data/ # Armazena os dados brutos e transformados
├── database/ # Contém o banco de dados SQLite
├── src/ # Scripts de extração, transformação e carga
│ ├── extract.py
│ ├── transform.py
│ └── load.py
├── main.py # Roda todo o pipeline
├── requirements.txt # Dependências do projeto
└── README.md


---

## 🚀 Como executar

1. Clone este repositório:

```bash
git clone https://github.com/letverso/etl-dados-covid.git
cd etl-dados-covid

2. Instale as dependências:
pip install -r requirements.txt

3. Execute o pipeline:
python main.py

