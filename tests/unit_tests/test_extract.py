import os
import pandas as pd
import pytest

# Add project root to sys.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from etl.extract.extract import extract_data


# ---------- Test 1: Successful extraction ---------- #
def test_extract_data_success(tmp_path):
    # Create a dummy CSV file
    test_file = tmp_path / "test_data.csv"
    test_df = pd.DataFrame({
        "order_id": ["A1", "A2"],
        "sales": [100.0, 200.0]
    })
    test_df.to_csv(test_file, index=False)

    # Call extract function
    result_df = extract_data(str(test_file))

    # Assertions
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.shape == (2, 2)
    assert list(result_df.columns) == ["order_id", "sales"]


# ---------- Test 2: File not found ---------- #
def test_extract_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        extract_data("non_existent_file.csv")

