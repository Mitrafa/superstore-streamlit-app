Analytical Questions:

How do monthly sales and profit vary over time?

Which shipping methods lead to longer delivery times?

How does profitability vary by product category?

Are there regional patterns in sales or customer behavior?


Data Preprocessing Summary
Initial dataset:
21 columns, 51,290 rows of sales data.

Column standardisation:
All column names converted to lowercase with underscores for consistency.

Data types checked:
Verified types across all columns using .dtypes and .info().

Sales column cleaned:
Converted from object (with dollar signs or commas) to float.

Missing values check:
No missing values across any column after processing.

Date parsing:

Inspected unique values in order_date and ship_date

Detected mixed date formats (DD/MM/YYYY and MM/DD/YYYY)

Used two-step parsing to correctly convert both formats

Dropped rows where both order_date and ship_date remained unparsed

New columns created:

ship_duration = days between shipping and order dates

order_month = monthly period for trend analysis

order_quarter = quarterly period for business summary


Testing Approach:

Validated ETL scripts by printing sample outputs and inspecting .head()

Used .info() and .describe() to confirm data types and distributions

Checked filtered dashboard interactions manually

(Optional) Added assertions or wrote simple test scripts in tests/


Analytical Questions:

How do monthly sales and profit vary over time?

Which shipping methods lead to longer delivery times?

How does profitability vary by product category?

Are there regional patterns in sales or customer behavior?

Data Preprocessing Summary
Initial dataset:
21 columns, 51,290 rows of sales data.

Column standardisation:
All column names converted to lowercase with underscores for consistency.

Data types checked:
Verified types across all columns using .dtypes and .info().

Sales column cleaned:
Converted from object (with dollar signs or commas) to float.

Missing values check:
No missing values across any column after processing.

Date parsing:
Inspected unique values in order_date and ship_date
Detected mixed date formats (DD/MM/YYYY and MM/DD/YYYY)
Used two-step parsing to correctly convert both formats
Dropped rows where both order_date and ship_date remained unparsed

New columns created:
ship_duration = days between shipping and order dates
order_month = monthly period for trend analysis
order_quarter = quarterly period for business summary

Testing Approach:

Validated ETL scripts by printing sample outputs and inspecting .head()

Used .info() and .describe() to confirm data types and distributions

Checked filtered dashboard interactions manually

(Optional) Added assertions or wrote simple test scripts in tests/