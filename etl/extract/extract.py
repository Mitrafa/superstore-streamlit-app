import pandas as pd
import os

def extract_data(filepath="data/raw/SuperStoreOrders.csv") -> pd.DataFrame:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    df = pd.read_csv(filepath)
    return df