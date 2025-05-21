# app/main.py
import streamlit as st
import pandas as pd
import plotly.express as px  # For interactive plots

# Set page configuration for a clean layout
st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

# Title and description
st.title("🌞 Solar Potential Dashboard")
st.markdown("""
This dashboard visualizes solar potential across Benin, Sierra Leone, and Togo.  
Select countries to compare their GHI distributions and see the top regions by average GHI.
""")

# Load data
@st.cache_data  # Cache the data loading for performance
def load_data():
    """Load and combine cleaned datasets for all countries."""
    countries = ['benin', 'sierra_leone', 'togo']
    dfs = []
    for country in countries:
        df = pd.read_csv(f'../../data/{country}_clean.csv')
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df['Country'] = country.capitalize().replace('_', ' ')
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

# Load the data with a spinner
with st.spinner("Loading data..."):
    df = load_data()

# Sidebar for user inputs
st.sidebar.header("Filters")

# Country selection widget
countries = ['Benin', 'Sierra Leone', 'Togo']
selected_countries = st.sidebar.multiselect(
    "Select Countries to Compare",
    options=countries,
    default=countries
)

# Main content
st.header("Solar Metrics Visualization")

# Check if at least one country is selected
if not selected_countries:
    st.warning("Please select at least one country.")
else:
    # Filter the DataFrame based on selected countries
    filtered_df = df[df['Country'].isin(selected_countries)].copy()

    # Boxplot of GHI
    st.subheader("GHI Distribution by Country")
    fig = px.box(
        filtered_df,
        x='Country',
        y='GHI',
        color='Country',
        title='GHI Distribution Across Selected Countries',
        labels={'Country': 'Country', 'GHI': 'GHI (W/m²)'}
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12),
        margin=dict(l=40, r=40, t=60, b=40)
    )
    st.plotly_chart(fig, use_container_width=True)

    # Top regions table (ranked by average GHI)
    st.subheader("Top Regions by Average GHI")
    avg_ghi = filtered_df.groupby('Country')['GHI'].mean().sort_values(ascending=False).round(2)
    top_regions_df = pd.DataFrame({
        'Country': avg_ghi.index,
        'Average GHI (W/m²)': avg_ghi.values
    })
    st.dataframe(top_regions_df, use_container_width=True)
