import pandas as pd
import sqlite3

def load_to_sqlite(csv_path, db_path, table_name='covid_data'):
    print("💾 Carregando dados para o banco SQLite...")
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"✅ Dados carregados em {db_path} (tabela: {table_name})")

if __name__ == "__main__":
    load_to_sqlite("data/processed/brazil_covid.csv", "database/covid_data.db")
