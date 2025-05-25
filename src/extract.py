import requests
import os

def download_csv(url, save_path):
    print("🔄 Baixando dados de:", url)
    response = requests.get(url)
    response.raise_for_status()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, 'wb') as f:
        f.write(response.content)
    print(f"✅ Dados salvos em: {save_path}")

if __name__ == "__main__":
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    save_path = "data/raw/owid-covid-data.csv"
    download_csv(url, save_path)
