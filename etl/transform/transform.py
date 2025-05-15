import pandas as pd
import re

def clean_and_transform(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform Superstore dataset for analysis."""

    # --- Parse dates ---
    df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=True)
    df['ship_date'] = pd.to_datetime(df['ship_date'], format='mixed', dayfirst=True)

    # --- Clean currency columns (remove $ and , if any) ---
    df['sales'] = df['sales'].replace(r'[\$,]', '', regex=True).astype(float)
    df['profit'] = df['profit'].replace(r'[\$,]', '', regex=True).astype(float)
    df['shipping_cost'] = df['shipping_cost'].replace(r'[\$,]', '', regex=True).astype(float)

    # --- Feature engineering ---
    df['order_year'] = df['order_date'].dt.year
    df['order_month'] = df['order_date'].dt.month
    df['order_day'] = df['order_date'].dt.day
    df['order_weekday'] = df['order_date'].dt.day_name()

    df['ship_month'] = df['ship_date'].dt.month
    df['ship_day'] = df['ship_date'].dt.day

    df['ship_duration'] = (df['ship_date'] - df['order_date']).dt.days

    # --- Select relevant columns ---
    columns_to_keep = [
        'order_id', 'order_date', 'ship_date', 'ship_mode', 'customer_name',
        'segment', 'state', 'country', 'market', 'region', 'product_id',
        'category', 'sub_category', 'product_name', 'sales', 'quantity',
        'discount', 'profit', 'shipping_cost', 'order_priority', 'year',
        'order_day', 'order_month', 'ship_day', 'ship_month',
        'order_year', 'order_weekday', 'ship_duration'
    ]
    df = df[columns_to_keep]

    return df
