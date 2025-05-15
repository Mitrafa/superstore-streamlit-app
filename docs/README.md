###### 📊 Superstore Sales ETL & Dashboard Project

Welcome to the **Superstore Sales ETL & Streamlit Dashboard** project! This project showcases end-to-end data engineering — from raw data extraction to transformation, loading, and interactive data visualisation.

---

###### Live Demo

[Click here to view the deployed app](https://mitra-superstore.streamlit.app/)

###### Project Structure

```
superstore-streamlit-app/
├── app/
│   └── dashboard.py              # Streamlit dashboard app
├── data/
│   ├── raw/                      # Original dataset (SuperStoreOrders.csv)
│   └── cleaned/                  # Cleaned dataset after ETL
├── docs/
│   ├── README.md                 # Project documentation
│   └── user_stories.md
├── etl/
│   ├── extract/
│   │   └── extract.py            # extract_data() function
│   ├── transform/
│   │   └── transform.py          # clean_and_transform() function
│   └── load/
│       └── load.py              # load_to_csv() function
├── notebooks/
│   └── exploratory_analysis.ipynb
├── scripts/
│   └── run_etl.py                # Runs full ETL pipeline
├── tests/
│   └── unit_tests/               # Unit tests for ETL
├── requirements.txt              # Python dependencies
└── setup.py                      # Optional project setup

```

---

###### Project Objectives

- Extract data from a raw CSV file
- Clean and transform data using pandas
- Perform time-based and shipping-related feature engineering
- Load the cleaned data into a usable format
- Create a visual dashboard using Streamlit with filters, charts, and data downloads

---

###### Environment Setup

###### 1. Create and activate virtual environment

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

###### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

###### How to Run This Project

###### Step 1: Run the ETL pipeline
```bash
python scripts/run_etl.py
```
This extracts, cleans, and saves the data to:
```
data/cleaned/cleaned_superstore.csv
```

###### Step 2: Launch the Streamlit dashboard
```bash
streamlit run app/dashboard.py
```

---

###### Dashboard Features

- Filter by Region, Ship Mode, and Category
- Download full or filtered datasets
- 5 interactive tabs:
  - Monthly Sales & Profit
  - Shipping Duration Analysis
  - Profit vs Sales by Category
  - Average Sales and Profit by Sub-Category
  - Top 10 Customers by Sales

---

###### Analytical Questions and Answers

**❓ Which months and years had the highest sales and profit?**  
→ Q4 (Oct–Dec) typically shows peak performance in both metrics.

**❓ Which shipping mode results in the longest delivery time?**  
→ Standard Class has the longest average delivery duration.

**❓ Is there a positive correlation between sales and profit?**  
→ Not always — some products generate high sales with low profit margins.

**❓ Which sub-categories perform best in average sales and profit?**  
→ Phones and Chairs lead in both metrics.

**❓ Who are the top customers by sales?**  
→ The dashboard highlights the top 10 customers by revenue.

---

###### Data Transformations

Performed using `clean_and_transform()`:
- Parse `order_date` and `ship_date`
- Clean currency columns: `sales`, `profit`, `shipping_cost`
- Create `order_month`, `order_weekday`, `ship_duration`, and more
- Keep only relevant features for analysis

---

###### Running Tests

Run unit tests using:
```bash
pytest tests/unit_tests/
```

Tests include:
- File extraction and format validation
- Transformation correctness (e.g. shipping duration, date parsing)

---

###### Key Dependencies

- `pandas`
- `streamlit`
- `plotly`
- `pytest`

Install them all with:
```bash
pip install -r requirements.txt
```

---

### Optimising Query Execution and Performance

As the dataset scales, the following strategies would be used to improve performance:

- Convert CSV files to **Parquet** for faster read/write and lower storage.
- Move cleaned data into a **PostgreSQL** or **Amazon Redshift** database.
- Pre-aggregate data and cache results to reduce processing time.
- Implement **incremental ETL** to process only new data instead of the full dataset.

---

### Error Handling and Logging

- The ETL pipeline uses `try/except` blocks to catch:
  - Missing files
  - Parsing errors
  - Data type mismatches
- Logging is implemented using Python's built-in `logging` module.
  - Logs when data is extracted
  - Logs shape of data at each stage
  - Logs errors if encountered
- This setup supports easy debugging and future monitoring via tools like **AWS CloudWatch**.

---

### Security and Privacy Considerations

While the current dataset doesn’t include sensitive (Except name of people) data, in a production environment I would:

- Use **environment variables** or **AWS Secrets Manager** to store credentials.
- Remove or anonymise customer identifiers from shared datasets.
- Enforce HTTPS and secure connections when hosting the app publicly.

---

### Cloud Deployment and AWS Automation

This project could be automated and deployed using AWS services:

- **Amazon S3** — For storing raw and cleaned datasets
- **AWS Lambda** — To automate ETL job execution
- **Amazon MWAA (Managed Airflow)** — For orchestration
- **Amazon RDS/Redshift** — As the data warehouse layer
- **Amazon EC2** — For hosting the Streamlit app
- **AWS CloudWatch** — For log tracking and performance monitoring
- **AWS Secrets Manager** — For secure credential management

This architecture supports full automation, scalability, and integration with enterprise data pipelines.

---

###### Future Enhancements

- Add time series forecasting (e.g. Prophet or ARIMA)
- Improve testing coverage and structured exception logging
- Enable additional export formats (e.g. Excel, Parquet)
- Store cleaned data in a **PostgreSQL** or **Amazon Redshift** database
- Automate ETL workflow using **Apache Airflow** or **AWS Lambda**
- Deploy Streamlit app via **EC2** or **ECS**
- Monitor ETL performance and errors using **AWS CloudWatch**
- Use **Secrets Manager** to securely store database/API credentials

---


##### Acknowledgements
This project was created as part of my Data Engineering Capstone at Digital Futures.
Special thanks to my mentors and peers who supported me throughout this journey.

Made by **Mitra Fazel**  