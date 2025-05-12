from etl.extract.extract import extract_csv
from etl.transform.transform import transform_data
from etl.load.load import load_to_csv
from etl.extract.extract import extract_csv

def run_etl():
    df = extract_csv("data/raw/SuperStoreOrders.csv")
    df = transform_data(df)
    load_to_csv(df, "data/cleaned/cleaned_superstore.csv")
    print("ETL process completed.")

if __name__ == "__main__":
    run_etl()
