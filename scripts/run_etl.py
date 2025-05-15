import pandas as pd
from etl.extract.extract import extract_data
from etl.transform.transform import clean_and_transform
from etl.load.load import load_to_csv

def run_etl():
    try:
        # Step 1: Extract
        print("Extracting raw data...")
        df_raw = extract_data("data/raw/SuperStoreOrders.csv")

        # Step 2: Transform
        print("Transforming data...")
        df_cleaned = clean_and_transform(df_raw)

        # Step 3: Load
        output_path = "data/cleaned/cleaned_superstore.csv"
        print("Saving cleaned data...")
        load_to_csv(df_cleaned, output_path)

    except Exception as e:
        print(f"❌ ETL process failed: {e}")
        raise

if __name__ == "__main__":
    run_etl()
