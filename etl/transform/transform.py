import pandas as pd


def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df


def convert_sales_to_float(df):
    df['sales'] = df['sales'].replace(r'[$,]', '', regex=True).astype(float)
    return df


def parse_dates(df):
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', dayfirst=True)
    df['order_date'] = df['order_date'].fillna(pd.to_datetime(df['order_date'], errors='coerce', dayfirst=False))

    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce', dayfirst=True)
    df['ship_date'] = df['ship_date'].fillna(pd.to_datetime(df['ship_date'], errors='coerce', dayfirst=False))

    df.dropna(subset=['order_date', 'ship_date'], inplace=True)
    return df


def calculate_ship_duration(df):
    df['ship_duration'] = (df['ship_date'] - df['order_date']).dt.days
    df = df[df['ship_duration'].notna() & (df['ship_duration'] >= 0)]
    return df


def bin_shipping_speed(df):
    max_duration = df['ship_duration'].max()
    if max_duration <= 20:
        max_duration = 21

    df['shipping_speed'] = pd.cut(
        df['ship_duration'],
        bins=[-1, 2, 5, 10, 20, max_duration],
        labels=['Fast', 'Standard', 'Slow', 'Very Slow', 'Extreme']
    )
    return df


def add_time_columns(df):
    df['order_month'] = df['order_date'].dt.to_period('M')
    df['order_quarter'] = df['order_date'].dt.to_period('Q')
    df['order_weekday'] = df['order_date'].dt.day_name()
    return df


def calculate_profit_metrics(df):
    df['profit_margin'] = (df['profit'] / df['sales']) * 100
    df['is_profitable'] = df['profit'] > 0
    return df


def add_customer_order_count(df):
    df['customer_order_count'] = df.groupby('customer_name')['order_id'].transform('count')
    return df


# Main transformation function
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_column_names(df)
    df = convert_sales_to_float(df)
    df = parse_dates(df)
    df = calculate_ship_duration(df)
    df = bin_shipping_speed(df)
    df = add_time_columns(df)
    df = calculate_profit_metrics(df)
    df = add_customer_order_count(df)

    print("✅ Transform complete. Final shape:", df.shape)
    return df