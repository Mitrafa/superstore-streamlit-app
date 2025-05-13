import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Convert sales to float
    df['sales'] = df['sales'].replace(r'[$,]', '', regex=True).astype(float)

    # Parse dates (handle mixed formats)
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', dayfirst=True)
    df['order_date'] = df['order_date'].fillna(pd.to_datetime(df['order_date'], errors='coerce', dayfirst=False))

    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce', dayfirst=True)
    df['ship_date'] = df['ship_date'].fillna(pd.to_datetime(df['ship_date'], errors='coerce', dayfirst=False))

    # Drop rows with missing critical dates
    df.dropna(subset=['order_date', 'ship_date'], inplace=True)

    # Calculate ship duration
    df['ship_duration'] = (df['ship_date'] - df['order_date']).dt.days
    
    # Clean up and bin
    # Drop rows with negative or missing shipping durations before binning
    df = df[df['ship_duration'].notna() & (df['ship_duration'] >= 0)]

    # Recalculate max after cleanup
    max_duration = df['ship_duration'].max()

    # Ensure max_duration is strictly increasing from previous bin (e.g. > 20)
    if max_duration <= 20:
        max_duration = 21

    # Bin ship_duration
    df['shipping_speed'] = pd.cut(
        df['ship_duration'],
        bins=[-1, 2, 5, 10, 20, max_duration],
        labels=['Fast', 'Standard', 'Slow', 'Very Slow', 'Extreme'])


    # Add order_month and order_quarter
    df['order_month'] = df['order_date'].dt.to_period('M')
    df['order_quarter'] = df['order_date'].dt.to_period('Q')

    # Add profit_margin
    df['profit_margin'] = (df['profit'] / df['sales']) * 100

    # Add is_profitable flag
    df['is_profitable'] = df['profit'] > 0

    # Add customer_order_count
    df['customer_order_count'] = df.groupby('customer_name')['order_id'].transform('count')

    # Add order_weekday
    df['order_weekday'] = df['order_date'].dt.day_name()

    # Remove rows with negative shipping durations
    df = df[df['ship_duration'] >= 0]

    print("✅ Transform complete. Final shape:", df.shape)
    return df