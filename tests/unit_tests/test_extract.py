from etl.extract.extract import extract_data


def test_extract_data_reads_file_correctly():
    df = extract_data("data/raw/SuperStoreOrders.csv")
    assert not df.empty
    assert "order_id" in df.columns
