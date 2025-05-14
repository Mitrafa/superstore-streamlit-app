Analytical Questions
This project aims to answer the following key business questions:

1. How do monthly sales and profit vary over time?

2. Which shipping methods lead to longer delivery times?

3. How does profitability vary by product category?

4. Are there regional patterns in sales or customer behavior?

Data Preprocessing Summary
Initial Dataset: 
Rows: 51,290
Columns: 21

Contains sales, shipping, customer, and product-level information.

Column Standardisation:
All column names converted to lowercase with underscores for consistency (order_id instead of Order ID).

Data Types Checked:
Verified data types using .dtypes and .info() to ensure correct parsing (e.g., date columns, sales as float).

Sales Column Cleaned:
Converted from string ("$200.00") to float, removing $ and ,.

Missing Values:
Initially checked for missing values.

After preprocessing, no missing values remained in the cleaned dataset.

Date Parsing
Steps Taken:
Inspected unique values in order_date and ship_date.

Detected mixed formats (DD/MM/YYYY and MM/DD/YYYY).

Used two-step parsing with dayfirst=True and fallback parsing.

Dropped rows where both dates could not be parsed.

New Columns Created:
Column Name	Description
ship_duration: Number of days between order and shipping dates
order_month: Month period (e.g. 2023-04) for trend analysis
order_quarter: Quarter period (e.g. 2023Q2) for seasonal analysis
order_weekday: Day of the week the order was placed
shipping_speed: Categorised bin of delivery time (Fast, Slow, etc.)
profit_margin: Calculated as (profit / sales) * 100
is_profitable: Boolean indicating whether the sale was profitable
customer_order_count: Number of orders placed by each customer

Data Transformation Functions
Each transformation function performs a single, testable operation:

Function Name	Description
clean_column_names()	Standardises column names to lowercase with underscores
convert_sales_to_float()	Converts sales from string with $/, to float
parse_dates()	Parses mixed date formats and handles missing values
calculate_ship_duration()	Computes days between order and ship dates
bin_shipping_speed()	Categorises shipping speed into 5 bins
add_time_columns()	Adds order_month, order_quarter, and order_weekday
calculate_profit_metrics()	Adds profit_margin and is_profitable flags
add_customer_order_count()	Adds count of orders per customer

Testing Approach
Area	Method
ETL functionality	Manually validated with .head(), .info(), .describe()
Unit Testing	Used pytest for function-level tests in tests/unit_tests/
Error Handling	Added tests to simulate invalid paths (e.g., permission errors)
Dashboard behaviour	Interactions validated manually through the Streamlit UI

