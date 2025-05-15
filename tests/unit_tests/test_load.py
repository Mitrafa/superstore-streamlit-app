import os
import pandas as pd
import pytest
from pathlib import Path

# Add project root to sys.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from etl.load.load import load_to_csv


# ---------- Test 1: Successful load ---------- #
def test_load_to_csv_success(tmp_path):
    # Create a small test DataFrame
    test_df = pd.DataFrame({
        "order_id": ["A1", "A2"],
        "sales": [100.0, 200.0]
    })

    # Define output file path inside temp dir
    output_file = tmp_path / "output" / "test_output.csv"

    # Call the function
    load_to_csv(test_df, str(output_file))

    # Check if file exists
    assert output_file.exists()

    # Verify content
    saved_df = pd.read_csv(output_file)
    pd.testing.assert_frame_equal(test_df, saved_df)


# ---------- Test 2: Invalid path error handling ---------- #
def test_load_to_csv_invalid_path():
    # Create dummy dataframe
    test_df = pd.DataFrame({"col": [1, 2, 3]})

    # Intentionally invalid path (e.g., forbidden root path)
    with pytest.raises(Exception):
        load_to_csv(test_df, "/invalid_dir/test.csv")
