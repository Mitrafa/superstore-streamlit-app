def load_to_csv(df, output_path: str):
    df.to_csv(output_path, index=False)
