import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="Crop Dataset Explorer",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
/* Sidebar background */
section[data-testid="stSidebar"] {
    background-color: #F9FAFB;
    border-right: 1px solid #E5E7EB;
}

/* Remove extra top padding */
section[data-testid="stSidebar"] > div {
    padding-top: 1rem;
}

/* "Page" links styling */
div[data-testid="stSidebarNav"] a {
    display: block;
    padding: 0.45rem 0.85rem;
    margin-bottom: 0.25rem;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 500;
    color: #4B5563;
    text-decoration: none;
}

/* Hover effect */
div[data-testid="stSidebarNav"] a:hover {
    background-color: #E5E7EB;
    color: #111827;
}

/* Active page pill */
div[data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: #16A34A;
    color: #FFFFFF !important;
}

/* Optional: sidebar text (like 'Pages') */
div[data-testid="stSidebarNav"] > div:first-child {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #9CA3AF;
    margin-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# Global Styling – match rest of app
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    * {
        font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
    }

  #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    

    .main {
        background: #FFFFFF;
    }

    .block-container {
        max-width: 1200px !important;
        padding: 2rem 2rem 4rem 2rem !important;
        margin: 0 auto !important;
    }

    .page-hero {
        padding: 32px 24px;
        background: #000000;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 32px;
    }

    .page-hero-title {
        font-size: 36px;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }

    .page-hero-subtitle {
        font-size: 16px;
        color: #A1A1A6;
        margin: 0;
    }

    .section-title {
        font-size: 20px;
        font-weight: 600;
        color: #000000;
        margin: 24px 0 12px 0;
        padding-bottom: 8px;
        border-bottom: 1px solid #E5E5E5;
    }

    .info-text {
        font-size: 14px;
        color: #666666;
        margin-bottom: 8px;
    }

    .metric-row {
        margin-top: 16px;
        margin-bottom: 24px;
    }

    .stMetric {
        text-align: center !important;
    }

    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    return pd.read_csv("data/Crop_recommendation.csv")


# Hero section (centered, consistent colors)
st.markdown(
    """
    <div class="page-hero">
        <div class="page-hero-title">📊 Crop Dataset Explorer</div>
        <p class="page-hero-subtitle">
            Explore the full crop dataset used for training the Smart Irrigation Advisor.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Load data
df = load_data()

# -----------------------------
# Basic Info Section
# -----------------------------
st.markdown('<div class="section-title">📌 Dataset Overview</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Records", len(df))
with col2:
    st.metric("Total Columns", len(df.columns))
with col3:
    st.metric("Unique Crop Types", df['label'].nunique())

# Show data
st.markdown('<div class="section-title">🔍 Sample Rows</div>', unsafe_allow_html=True)
st.markdown('<p class="info-text">First 10 rows of the dataset.</p>', unsafe_allow_html=True)
st.dataframe(df.head(10), width='stretch')

# Data Types
st.markdown('<div class="section-title">🧬 Column Types</div>', unsafe_allow_html=True)
dtypes_df = pd.DataFrame({
    'Column': df.dtypes.index,
    'Data Type': [str(dtype) for dtype in df.dtypes.values]
})
st.dataframe(dtypes_df, width='stretch', hide_index=True)

# Stats
st.markdown('<div class="section-title">📈 Statistical Summary</div>', unsafe_allow_html=True)
stats_df = df.describe()
st.dataframe(stats_df, width='stretch')

# Missing values
st.markdown('<div class="section-title">⚠️ Missing Values Check</div>', unsafe_allow_html=True)
missing_df = pd.DataFrame({
    'Column': df.isnull().sum().index,
    'Missing Count': df.isnull().sum().values
})
st.dataframe(missing_df, width='stretch', hide_index=True)

# Crop distribution
st.markdown('<div class="section-title">🌾 Crop Distribution</div>', unsafe_allow_html=True)
st.bar_chart(df['label'].value_counts())

# Unique crop list
st.markdown('<div class="section-title">🌱 Unique Crop Types</div>', unsafe_allow_html=True)
unique_crops = df['label'].unique()
st.write(f"**Total unique crops:** {len(unique_crops)}")
st.write(", ".join(unique_crops))

# Filter rice & maize
st.markdown('<div class="section-title">🌾 Rice & Maize Subset</div>', unsafe_allow_html=True)
rice_maize_df = df[df['label'].isin(['rice', 'maize'])]

colA, colB = st.columns(2)
with colA:
    st.metric("Rice Records", len(rice_maize_df[rice_maize_df['label'] == 'rice']))
with colB:
    st.metric("Maize Records", len(rice_maize_df[rice_maize_df['label'] == 'maize']))

st.dataframe(rice_maize_df.head(10), width='stretch')

# Rice vs Maize Comparison
st.markdown('<div class="section-title">📊 Rice vs Maize – Average Values</div>', unsafe_allow_html=True)
rice_avg = rice_maize_df[rice_maize_df['label'] == 'rice'].drop('label', axis=1).mean()
maize_avg = rice_maize_df[rice_maize_df['label'] == 'maize'].drop('label', axis=1).mean()

comparison_df = pd.DataFrame({'Rice': rice_avg, 'Maize': maize_avg})
# Convert to numeric to avoid Arrow serialization issues
comparison_df = comparison_df.astype(float)
st.dataframe(comparison_df, width='stretch')
