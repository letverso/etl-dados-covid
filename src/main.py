from extract import download_csv
from transform import process_csv
from load import load_to_sqlite

def run_etl():
    raw = "data/raw/owid-covid-data.csv"
    processed = "data/processed/brazil_covid.csv"
    db = "database/covid_data.db"

    download_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv", raw)
    process_csv(raw, processed)
    load_to_sqlite(processed, db)

if __name__ == "__main__":
    run_etl()
