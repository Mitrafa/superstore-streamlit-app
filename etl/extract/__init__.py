import sys
import os
import pandas as pd
from datetime import datetime

# Add project root to sys.path so we can import from etl/transform
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


def test_date_parsing_and_shipping_duration():
    # Mock input data
    test_df = pd.DataFrame({
        'order_id': ['A1'],
        'order_date': ['01-01-2023'],
        'ship_date': ['03-01-2023'],
        'ship_mode': ['Standard Class'],
        'customer_name': ['John Doe'],
        'segment': ['Consumer'],
        'state': ['California'],
        'country': ['United States'],
        'market': ['US'],
        'region': ['West'],
        'product_id': ['P1'],
        'category': ['Furniture'],
        'sub_category': ['Chairs'],
        'product_name': ['Office Chair'],
        'sales': [200.0],
        'quantity': [2],
        'discount': [0.1],
        'profit': [50.0],
        'shipping_cost': [20.0],
        'order_priority': ['Medium'],
        'year': [2023]
    })

    result_df = transform_data(test_df)

    assert result_df['order_date'].dtype == 'datetime64[ns]'
    assert result_df['ship_date'].dtype == 'datetime64[ns]'
    assert result_df['ship_duration'].iloc[0] == 2


def test_time_columns_extraction():
    test_df = pd.DataFrame({
        'order_id': ['B2'],
        'order_date': ['15-03-2022'],
        'ship_date': ['18-03-2022'],
        'ship_mode': ['Second Class'],
        'customer_name': ['Jane Smith'],
        'segment': ['Corporate'],
        'state': ['New York'],
        'country': ['United States'],
        'market': ['US'],
        'region': ['East'],
        'product_id': ['P2'],
        'category': ['Technology'],
        'sub_category': ['Phones'],
        'product_name': ['Smartphone'],
        'sales': [500.0],
        'quantity': [1],
        'discount': [0.0],
        'profit': [120.0],
        'shipping_cost': [10.0],
        'order_priority': ['High'],
        'year': [2022]
    })

    result_df = transform_data(test_df)

    assert result_df['order_year'].iloc[0] == 2022
    assert result_df['order_month'].iloc[0] == 3
    assert result_df['order_day'].iloc[0] == 15
    assert result_df['order_weekday'].iloc[0] == 'Tuesday'

