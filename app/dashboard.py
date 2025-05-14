import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- Page Setup ----
st.set_page_config(page_title="Superstore Dashboard", layout="wide")


# ---- Load Cleaned Data ----
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned/cleaned_superstore.csv")
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['order_month'] = df['order_date'].dt.to_period('M')
    return df

df = load_data()

# ---- Sidebar Filters ----
st.sidebar.header("🔎 Filter Options")

# Region filter
regions = df['region'].unique().tolist()
selected_regions = st.sidebar.multiselect(
    "Select Region(s)",
    options=regions,
    default=regions
)

# Ship Mode filter
ship_modes = df['ship_mode'].unique().tolist()
selected_ship_modes = st.sidebar.multiselect(
    "Select Ship Mode(s)",
    options=ship_modes,
    default=ship_modes
)

# Category filter
categories = df['category'].unique().tolist()
selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=categories,
    default=categories
)

# ---- Filtered Data ----
df_filtered = df[
    (df['category'].isin(selected_categories)) &
    (df['region'].isin(selected_regions)) &
    (df['ship_mode'].isin(selected_ship_modes))
]

# ---- Handle Empty Filters or Show Tabs ----
if df_filtered.empty:
    st.warning("⚠️ No data to display. Please select at least one option from each filter.")
else:
    st.title("📊 Superstore Sales Dashboard")
    st.markdown("Use the sidebar filters to explore the dataset.")

    # ---- Tabs ----
    tab1, tab2, tab3 = st.tabs(["📈 Monthly Sales & Profit", "📦 Shipping Duration", "🔴 Profit vs Sales"])

    with tab1:
        st.subheader("📈 Monthly Sales & Profit Trend")
        monthly_summary = df_filtered.groupby('order_month')[['sales', 'profit']].sum().sort_index()

        if monthly_summary.empty:
            st.info("ℹ️ No sales or profit data available for the selected filters.")
        else:
            fig1, ax1 = plt.subplots(figsize=(12, 5))
            monthly_summary.plot(ax=ax1)
            ax1.set_title("Monthly Sales and Profit")
            ax1.set_xlabel("Order Month")
            ax1.set_ylabel("USD Amount")
            ax1.grid(True)
            st.pyplot(fig1)

    with tab2:
        st.subheader("📦 Shipping Duration by Ship Mode")
        if df_filtered['ship_duration'].dropna().empty:
            st.info("ℹ️ No shipping duration data to display.")
        else:
            fig2, ax2 = plt.subplots()
            df_filtered.boxplot(column='ship_duration', by='ship_mode', ax=ax2)
            ax2.set_title("Shipping Duration by Ship Mode")
            ax2.set_xlabel("Ship Mode")
            ax2.set_ylabel("Duration (days)")
            plt.suptitle("")
            st.pyplot(fig2)

    with tab3:
        st.subheader("🔴 Profit vs Sales by Category")
        if df_filtered[['sales', 'profit']].dropna().empty:
            st.info("ℹ️ No sales/profit data available to plot.")
        else:
            fig3, ax3 = plt.subplots()
            for cat in df_filtered['category'].dropna().unique():
                temp = df_filtered[df_filtered['category'] == cat]
                ax3.scatter(temp['sales'], temp['profit'], label=cat, alpha=0.6)
            ax3.set_title("Profit vs Sales")
            ax3.set_xlabel("Sales")
            ax3.set_ylabel("Profit")
            ax3.legend()
            st.pyplot(fig3)
