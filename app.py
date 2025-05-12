import streamlit as st
import pandas as pd

st.title("📊 Superstore Sales Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned/cleaned_superstore.csv")

df = load_data()

st.write("## Sample Data", df.head())

# Example: Sales by Category
sales_by_cat = df.groupby('Category')['Sales'].sum()
st.write("## Sales by Category")
st.bar_chart(sales_by_cat)
