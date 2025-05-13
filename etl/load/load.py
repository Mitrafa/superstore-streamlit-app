import os
import pandas as pd


def load_to_csv(df: pd.DataFrame, output_path: str) -> None:
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
    except (OSError, IOError, PermissionError) as e:
        print(f"❌ Failed to save data to {output_path}: {e}")
        raise
