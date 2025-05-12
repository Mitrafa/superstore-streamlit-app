def transform_data(df):
    # Example transformation: convert date columns and drop nulls
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df = df.dropna()
    return df
