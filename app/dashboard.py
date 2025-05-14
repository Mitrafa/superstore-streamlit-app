import streamlit as st
import pandas as pd
import plotly.express as px
import io

# ---- Page Setup ----
st.set_page_config(page_title="Superstore Dashboard", layout="wide")

# ---- Colour Palette (CUD - Colour Universal Design) ----
cud_palette = [
    "#E69F00",  # orange
    "#56B4E9",  # sky blue
    "#009E73",  # green
    "#F0E442",  # yellow
    "#0072B2",  # blue
    "#D55E00",  # red-orange
    "#CC79A7",  # purple
    "#999999",  # grey
]

# ---- Load Cleaned Data ----
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned/cleaned_superstore.csv")
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['order_month'] = df['order_date'].dt.to_period('M')
    return df

df = load_data()

# ---- Sidebar ----
st.sidebar.header("🔎 Filter Options")

regions = df['region'].unique().tolist()
selected_regions = st.sidebar.multiselect("Select Region(s)", options=regions, default=regions)

ship_modes = df['ship_mode'].unique().tolist()
selected_ship_modes = st.sidebar.multiselect("Select Ship Mode(s)", options=ship_modes, default=ship_modes)

categories = df['category'].unique().tolist()
selected_categories = st.sidebar.multiselect("Select Category", options=categories, default=categories)

# ---- Filtered Data ----
df_filtered = df[
    (df['category'].isin(selected_categories)) &
    (df['region'].isin(selected_regions)) &
    (df['ship_mode'].isin(selected_ship_modes))
]

# ---- Download Buttons ----
st.sidebar.markdown("📥 **Download Filtered Data**")
st.sidebar.download_button(
    label="Download Filtered CSV",
    data=df_filtered.to_csv(index=False).encode('utf-8'),
    file_name="filtered_superstore_data.csv",
    mime="text/csv"
)

st.sidebar.markdown("📄 **Download Full Dataset**")
st.sidebar.download_button(
    label="Download Original CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name="superstore_original_data.csv",
    mime="text/csv"
)

# ---- Main Content ----
if df_filtered.empty:
    st.warning("⚠️ No data to display. Please select at least one option from each filter.")
else:
    st.title("📊 Superstore Sales Dashboard")
    st.markdown("Use the sidebar filters to explore the dataset.")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Monthly Sales & Profit",
        "📦 Shipping Duration",
        "🔴 Profit vs Sales",
        "🛒 Category Performance",
        "👤 Top Customers"
    ])

    with tab1:
        st.subheader("📈 Monthly Sales & Profit Trend")
        monthly_summary = df_filtered.groupby('order_month')[['sales', 'profit']].sum().sort_index().reset_index()
        monthly_summary['order_month'] = monthly_summary['order_month'].astype(str)

        fig = px.line(
            monthly_summary, x='order_month', y=['sales', 'profit'],
            labels={'value': 'USD Amount', 'order_month': 'Order Month'},
            title='Monthly Sales and Profit',
            template='plotly_white',
            color_discrete_sequence=cud_palette
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("📦 Shipping Duration by Ship Mode")
        if df_filtered['ship_duration'].dropna().empty:
            st.info("ℹ️ No shipping duration data to display.")
        else:
            ship_summary = df_filtered[['ship_mode', 'ship_duration']].dropna()
            fig2 = px.box(
                ship_summary, x='ship_mode', y='ship_duration',
                color='ship_mode',
                title='Shipping Duration by Ship Mode',
                color_discrete_sequence=cud_palette,
                template='plotly_white'
            )
            st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        st.subheader("🔴 Profit vs Sales by Category")
        if df_filtered[['sales', 'profit']].dropna().empty:
            st.info("ℹ️ No sales/profit data available to plot.")
        else:
            fig3 = px.scatter(
                df_filtered, x='sales', y='profit', color='category',
                title="Profit vs Sales by Category", opacity=0.6,
                color_discrete_sequence=cud_palette,
                template='plotly_white',
                hover_data=['product_id']
            )
            st.plotly_chart(fig3, use_container_width=True)

    with tab4:
        st.subheader("🛒 Average Sales and Profit by Sub-Category")
        subcat_summary = df_filtered.groupby('sub_category')[['sales', 'profit']].mean().sort_values(by='sales', ascending=False).reset_index()

        fig4 = px.bar(
            subcat_summary, x='sub_category', y=['sales', 'profit'],
            barmode='group',
            title="Average Sales and Profit by Sub-Category",
            labels={'value': 'USD Amount', 'sub_category': 'Sub-Category'},
            color_discrete_sequence=cud_palette,
            template='plotly_white'
        )
        fig4.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig4, use_container_width=True)

    with tab5:
        st.subheader("👤 Top 10 Customers by Sales")
        top_customers = df_filtered.groupby('customer_name')['sales'].sum().sort_values(ascending=False).head(10).reset_index()

        fig5 = px.bar(
            top_customers, x='sales', y='customer_name', orientation='h',
            title="Top 10 Customers by Sales",
            color_discrete_sequence=[cud_palette[1]],
            template='plotly_white'
        )
        fig5.update_layout(yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig5, use_container_width=True)
