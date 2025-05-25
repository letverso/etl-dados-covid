import pandas as pd

def process_csv(input_path, output_path, country='Brazil'):
    print(f"📊 Processando dados de: {input_path}")
    df = pd.read_csv(input_path)
    df_brazil = df[df['location'] == country]

    cols = ['date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']
    df_brazil = df_brazil[cols]
    df_brazil.to_csv(output_path, index=False)
    print(f"✅ Dados processados salvos em: {output_path}")

if __name__ == "__main__":
    process_csv("data/raw/owid-covid-data.csv", "data/processed/brazil_covid.csv")

