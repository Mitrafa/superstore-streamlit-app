import pandas as pd
import os

def extract_data(file_path="/Users/mitra/Documents/digital-futures/capstone_project/superstore-streamlit-app/data/raw/SuperStoreOrders.csv") -> pd.DataFrame:
    """
    Extracts data from a raw CSV file into a Pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Extracted raw data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")
    
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
        print(f"✅ Data successfully extracted. Shape: {df.shape}")
        return df
    except Exception as e:
        raise RuntimeError(f"❌ Failed to extract data: {e}")

# Optional: quick test when run standalone
if __name__ == "__main__":
    df = extract_data()
    print(df.head())
