import os

def load_to_csv(df, output_path):
    """
    Saves the cleaned DataFrame to a CSV file.
    Automatically creates the directory if it doesn't exist.

    Args:
        df (pd.DataFrame): The cleaned data to save.
        output_path (str): File path for the output CSV.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"✅ Load Complete. Data successfully saved to: {output_path}")
    except Exception as e:
        print(f"❌ Failed to save data: {e}")
        raise
