import os
import pytest
import pandas as pd
from etl.load.load import load_to_csv


def test_load_to_csv_creates_file(tmp_path):
    # Sample DataFrame
    df = pd.DataFrame({
        'name': ['Alice', 'Bob'],
        'age': [30, 25]
    })

    # Temp file path (automatically cleaned by pytest)
    output_file = tmp_path / "output.csv"

    # Run function
    load_to_csv(df, output_file)

    # Check that the file was created
    assert os.path.exists(output_file)

    # Check that the content matches
    loaded_df = pd.read_csv(output_file)
    pd.testing.assert_frame_equal(df, loaded_df)


def test_load_to_csv_invalid_path():
    # Sample DataFrame
    df = pd.DataFrame({'a': [1], 'b': [2]})

    # Use an invalid path (e.g., writing to a directory as a file)
    invalid_path = "/dev/null/output.csv"  # On Unix/macOS: /dev/null is not a directory

    with pytest.raises(Exception) as exc_info:
        load_to_csv(df, invalid_path)

    assert "Failed to save data" in str(exc_info.value) or isinstance(exc_info.value, (OSError, PermissionError))