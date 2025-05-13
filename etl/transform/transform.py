import pandas as pd

def transform_data(df):
    # Example transformation: convert date columns and drop nulls
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')
    df = df.dropna()
    return df
