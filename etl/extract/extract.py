import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)


def extract_data(file_path: str = "data/raw/SuperStoreOrders.csv") -> pd.DataFrame:
    """
    Extracts data from a raw CSV file into a Pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Extracted raw data.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        RuntimeError: If reading the CSV fails for any reason.
    """
    file_path = os.path.abspath(file_path)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")
    
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
        logging.info(f"Data successfully extracted. Shape: {df.shape}")
        return df
    except pd.errors.ParserError as e:
        raise RuntimeError(f"❌ Failed to parse CSV: {e}")
    except Exception as e:
        raise RuntimeError(f"❌ Unexpected error while extracting data: {e}")


# Standalone test
if __name__ == "__main__":
    try:
        df = extract_data()
        print(df.head())
    except Exception as e:
        print(e)
