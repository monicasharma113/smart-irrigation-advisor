#import streamlit as st
#import pandas as pd
#import pickle
#import plotly.graph_objects as go
#
#st.set_page_config(page_title="Irrigation Advisor", page_icon="💧", layout="centered")
#
#st.markdown("""
#<style>
#/* Sidebar background */
#section[data-testid="stSidebar"] {
#    background-color: #F9FAFB;
#    border-right: 1px solid #E5E7EB;
#}
#
#/* Remove extra top padding */
#section[data-testid="stSidebar"] > div {
#    padding-top: 1rem;
#}
#
#/* "Page" links styling */
#div[data-testid="stSidebarNav"] a {
#    display: block;
#    padding: 0.45rem 0.85rem;
#    margin-bottom: 0.25rem;
#    border-radius: 999px;
#    font-size: 14px;
#    font-weight: 500;
#    color: #4B5563;
#    text-decoration: none;
#}
#
#/* Hover effect */
#div[data-testid="stSidebarNav"] a:hover {
#    background-color: #E5E7EB;
#    color: #111827;
#}
#
#/* Active page pill */
#div[data-testid="stSidebarNav"] a[aria-current="page"] {
#    background-color: #16A34A;
#    color: #FFFFFF !important;
#}
#
#/* Optional: sidebar text (like 'Pages') */
#div[data-testid="stSidebarNav"] > div:first-child {
#    font-size: 12px;
#    text-transform: uppercase;
#    letter-spacing: 0.12em;
#    color: #9CA3AF;
#    margin-bottom: 0.5rem;
#}
#</style>
#""", unsafe_allow_html=True)
#
#st.markdown("""
#<style>
#    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
#    
#    * {
#        font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
#    }
#    
#    #MainMenu {visibility: visible;}
#    footer {visibility: hidden;}
#    
#    
#    .main {
#        background: #FFFFFF;
#    }
#    
#    .block-container {
#        padding: 2rem 1.5rem !important;
#        max-width: 900px !important;
#        margin: 0 auto !important;
#    }
#    
#    h1 {
#        font-size: 40px !important;
#        font-weight: 700 !important;
#        color: #111827 !important;
#        margin: 0 0 8px 0 !important;
#        text-align: center !important;
#    }
#    
#    .subtitle {
#        font-size: 16px;
#        color: #6B7280;
#        margin-bottom: 24px;
#        text-align: center;
#    }
#    
#    .section-title {
#        font-size: 20px;
#        font-weight: 600;
#        color: #111827;
#        margin: 0 0 16px 0;
#        padding-bottom: 10px;
#        border-bottom: 1px solid #E5E7EB;
#    }
#    
#    .subsection {
#        font-size: 15px;
#        font-weight: 600;
#        color: #111827;
#        margin: 18px 0 10px 0;
#    }
#    
#    .alert {
#        padding: 14px 16px;
#        border-radius: 10px;
#        margin: 12px 0;
#        font-size: 14px;
#        line-height: 1.5;
#    }
#    
#    .alert-success {
#        background: #ECFDF3;
#        border-left: 4px solid #22C55E;
#        color: #14532D;
#    }
#    
#    .alert-warning {
#        background: #FFFBEB;
#        border-left: 4px solid #F97316;
#        color: #7C2D12;
#    }
#    
#    .alert-error {
#        background: #FEF2F2;
#        border-left: 4px solid #EF4444;
#        color: #7F1D1D;
#    }
#    
#    .alert-info {
#        background: #EFF6FF;
#        border-left: 4px solid #3B82F6;
#        color: #1D4ED8;
#    }
#    
#    .metrics {
#        display: grid;
#        grid-template-columns: repeat(2, minmax(0, 1fr));
#        gap: 12px;
#        margin: 18px 0 8px 0;
#    }
#    
#    .metric {
#        background: #FFFFFF;
#        border: 1px solid #E5E7EB;
#        border-radius: 10px;
#        padding: 12px 10px;
#        text-align: center;
#    }
#    
#    .metric-value {
#        font-size: 22px;
#        font-weight: 700;
#        color: #111827;
#        margin-bottom: 2px;
#    }
#    
#    .metric-label {
#        font-size: 11px;
#        text-transform: uppercase;
#        letter-spacing: 0.06em;
#        color: #6B7280;
#    }
#    
#    .guidelines {
#        background: #FFFFFF;
#        border: 1px solid #E5E7EB;
#        border-radius: 12px;
#        padding: 14px 16px;
#        margin-top: 14px;
#    }
#    
#    .guidelines ul {
#        margin: 8px 0 0 0;
#        padding-left: 20px;
#    }
#    
#    .guidelines li {
#        font-size: 14px;
#        color: #4B5563;
#        line-height: 1.6;
#        margin-bottom: 6px;
#    }
#    
#    .stButton > button {
#        background: #16A34A !important;
#        color: #FFFFFF !important;
#        border: none !important;
#        padding: 12px 32px !important;
#        font-size: 15px !important;
#        font-weight: 500 !important;
#        border-radius: 999px !important;
#        width: 100% !important;
#        margin-top: 16px !important;
#    }
#    
#    .stButton > button:hover {
#        background: #15803D !important;
#    }
#    
#    label {
#        font-size: 14px !important;
#        font-weight: 500 !important;
#        color: #111827 !important;
#    }
#</style>
#""", unsafe_allow_html=True)
#
#
#@st.cache_resource
#def load_models():
#    with open('models/regression_model.pkl', 'rb') as f:
#        reg_model = pickle.load(f)
#    with open('models/classification_model.pkl', 'rb') as f:
#        clf_model = pickle.load(f)
#    with open('models/label_encoder.pkl', 'rb') as f:
#        label_encoder = pickle.load(f)
#    return reg_model, clf_model, label_encoder
#
#
#try:
#    reg_model, clf_model, label_encoder = load_models()
#    models_loaded = True
#except Exception as e:
#    models_loaded = False
#    st.error(f"⚠️ Error loading models: {str(e)}\n\nPlease run `python train_model.py` to generate new models.")
#
#st.title("Irrigation Advisor")
#st.markdown('<p class="subtitle">Get personalized irrigation recommendations based on your data</p>', unsafe_allow_html=True)
#
## ---------- INPUT SECTION (no wrapper div, so no blank box) ----------
#st.markdown('<div class="section-title">Input Parameters</div>', unsafe_allow_html=True)
#
#crop = st.selectbox("Crop Type", ["Rice", "Maize"])
#
#st.markdown('<div class="subsection">Environmental Conditions</div>', unsafe_allow_html=True)
#temperature = st.slider("Temperature (°C)", 15.0, 35.0, 25.0, 0.5)
#humidity = st.slider("Humidity (%)", 40.0, 100.0, 70.0, 1.0)
#rainfall = st.slider("Recent Rainfall (mm)", 0.0, 300.0, 100.0, 5.0)
#
#st.markdown('<div class="subsection">Soil Parameters</div>', unsafe_allow_html=True)
#c1, c2 = st.columns(2)
#with c1:
#    nitrogen = st.number_input("Nitrogen (N)", 0, 150, 80)
#with c2:
#    phosphorus = st.number_input("Phosphorus (P)", 0, 150, 50)
#
#c3, c4 = st.columns(2)
#with c3:
#    potassium = st.number_input("Potassium (K)", 0, 150, 40)
#with c4:
#    ph = st.number_input("Soil pH", 3.0, 10.0, 6.5, 0.1)
#
#predict_button = st.button("Analyze")
#
## ---------- RESULTS SECTION (also no wrapper div) ----------
#st.markdown('<div class="section-title">Results</div>', unsafe_allow_html=True)
#
#if models_loaded and predict_button:
#    crop_encoded = label_encoder.transform([crop.lower()])[0]
#    input_data = pd.DataFrame({
#        'N': [nitrogen], 'P': [phosphorus], 'K': [potassium],
#        'temperature': [temperature], 'humidity': [humidity],
#        'ph': [ph], 'rainfall': [rainfall], 'crop_encoded': [crop_encoded]
#    })
#    
#    water_req = reg_model.predict(input_data)[0]
#    extra = max(0.0, water_req - rainfall)
#    decision = clf_model.predict(input_data)[0]
#    proba = clf_model.predict_proba(input_data)[0]
#    classes = clf_model.classes_
#    
#    # Calculate deficit for rule-based classification
#    deficit = water_req - rainfall
#    deficit_percent = (deficit / water_req * 100) if water_req > 0 else 0
#    
#    # Rule-based classification (more reliable than model if model is biased)
#    if deficit > 40 or deficit_percent > 30:
#        rule_based_decision = "Irrigate Now"
#    elif deficit > 15 or deficit_percent > 10:
#        rule_based_decision = "Irrigate Soon"
#    else:
#        rule_based_decision = "No Irrigation Needed"
#    
#    # Use rule-based decision instead of model prediction for more accurate results
#    # The model might be biased, so we use the calculated deficit
#    decision = rule_based_decision
#    
#    # Show model prediction for reference (in debug mode)
#    model_decision = clf_model.predict(input_data)[0]
#    max_proba = max(proba)
#    
#    # Debug info (can be removed in production)
#    with st.expander("🔍 Debug Information"):
#        st.write(f"**Model Prediction:** {model_decision} (Confidence: {max_proba*100:.1f}%)")
#        st.write(f"**Rule-based Decision:** {rule_based_decision}")
#        st.write(f"**Water Requirement:** {water_req:.1f} mm")
#        st.write(f"**Rainfall:** {rainfall:.1f} mm")
#        st.write(f"**Deficit:** {deficit:.1f} mm ({deficit_percent:.1f}%)")
#        st.write(f"**Model Probabilities:**")
#        for cls, prob in zip(classes, proba):
#            st.write(f"  - {cls}: {prob*100:.1f}%")
#    
#    if decision == "Irrigate Now":
#        st.markdown(
#            '<div class="alert alert-error"><strong>Status:</strong> Irrigate Now<br>Immediate irrigation required within 6–12 hours.</div>',
#            unsafe_allow_html=True
#        )
#    elif decision == "Irrigate Soon":
#        st.markdown(
#            '<div class="alert alert-warning"><strong>Status:</strong> Irrigate Soon<br>Schedule irrigation within 1–2 days.</div>',
#            unsafe_allow_html=True
#        )
#    else:
#        st.markdown(
#            '<div class="alert alert-success"><strong>Status:</strong> No Irrigation Needed<br>Current conditions are adequate.</div>',
#            unsafe_allow_html=True
#        )
#    
#    st.markdown(f"""
#    <div class="metrics">
#        <div class="metric">
#            <div class="metric-value">{water_req:.1f} mm</div>
#            <div class="metric-label">Weekly Water Need</div>
#        </div>
#        <div class="metric">
#            <div class="metric-value">{extra:.1f} mm</div>
#            <div class="metric-label">Extra Irrigation</div>
#        </div>
#    </div>
#    """, unsafe_allow_html=True)
#    
#    st.markdown(
#        f'<div class="alert alert-info">Equivalent to {extra:.1f} liters per square meter</div>',
#        unsafe_allow_html=True
#    )
#    
#    st.markdown("**Prediction Confidence**")
#    fig = go.Figure(
#        data=[go.Bar(
#            x=classes,
#            y=proba * 100,
#            marker_color='#16A34A',
#            text=[f'{p:.1f}%' for p in proba * 100],
#            textposition='auto'
#        )]
#    )
#    fig.update_layout(
#        xaxis_title="",
#        yaxis_title="Confidence (%)",
#        showlegend=False,
#        height= 220,
#        plot_bgcolor='rgba(0,0,0,0)',
#        paper_bgcolor='rgba(0,0,0,0)',
#        margin=dict(l=0, r=0, t=10, b=0)
#    )
#    st.plotly_chart(fig, width='stretch')
#    
#    st.markdown("**Optimal Timing**")
#    if decision != "No Irrigation Needed" and extra > 0:
#        timing = (
#            "Early morning (5–7 AM) or late evening (6–8 PM)"
#            if temperature > 28
#            else "Morning (7–10 AM) or evening (5–7 PM)"
#        )
#        st.markdown(
#            f'<div class="alert alert-info">{timing} recommended</div>',
#            unsafe_allow_html=True
#        )
#    else:
#        st.markdown(
#            '<div class="alert alert-success">No immediate irrigation required</div>',
#            unsafe_allow_html=True
#        )
#    
#    st.markdown(f"""
#    <div class="guidelines">
#        <strong>{crop} Guidelines:</strong>
#        <ul>
#            {'<li>Maintain 2–5 cm standing water during growth</li><li>Optimal: 20–25°C, &gt;80% humidity</li><li>Consistent water levels required</li>'
#              if crop.lower() == 'rice'
#              else '<li>Deep but infrequent irrigation</li><li>Optimal: 20–30°C, 60–70% humidity</li><li>Encourage root development</li>'}
#        </ul>
#    </div>
#    """, unsafe_allow_html=True)
#else:
#    st.markdown(
#        '<div class="alert alert-info">Set your parameters above and click <strong>Analyze</strong> to view recommendations.</div>',
#        unsafe_allow_html=True
#    )
#    
#    st.markdown(f"""
#    <div class="guidelines">
#        <strong>Typical {crop} Ranges:</strong>
#        <ul>
#            {'<li>Temperature: 20–26°C</li><li>Humidity: 75–90%</li><li>Rainfall: 150–250 mm/week</li><li>Soil pH: 6.0–7.0</li>'
#              if crop == 'Rice'
#              else '<li>Temperature: 21–27°C</li><li>Humidity: 60–75%</li><li>Rainfall: 50–100 mm/week</li><li>Soil pH: 5.8–7.0</li>'}
#        </ul>
#    </div>
#    """, unsafe_allow_html=True)
#


import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go

st.set_page_config(page_title="Irrigation Advisor", page_icon="💧", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Main gradient background */
.stApp {
    background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 50%, #a5d6a7 100%);
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1b5e20 0%, #2e7d32 50%, #388e3c 100%);
    border-right: 3px solid #0d3d14;
}

section[data-testid="stSidebar"] > div {
    padding-top: 1rem;
}

/* Navigation styling */
div[data-testid="stSidebarNav"] a {
    background: rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    padding: 0.75rem 1rem !important;
    margin: 0.5rem 0 !important;
    color: #ffffff !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
}

div[data-testid="stSidebarNav"] a:hover {
    background: rgba(255,255,255,0.2) !important;
    transform: translateX(5px) !important;
}

div[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(255,255,255,0.95) !important;
    color: #1b5e20 !important;
    font-weight: 600 !important;
}

.main {
    background: transparent;
}

.block-container {
    padding: 2rem 1.5rem !important;
    max-width: 900px !important;
    margin: 0 auto !important;
}

/* Page Header */
.page-header {
    background: linear-gradient(135deg, #1b5e20, #2e7d32);
    padding: 2.5rem 2rem;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.page-header h1 {
    color: #ffffff;
    font-size: 2.5rem;
    font-weight: 800;
    margin: 0 0 0.5rem 0;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.page-header .subtitle {
    font-size: 1.1rem;
    color: #c8e6c9;
    margin: 0;
}

/* Section Cards */
.section-card {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    margin: 1.5rem 0;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    border-left: 5px solid #2e7d32;
}

.section-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1b5e20;
    margin: 0 0 1.5rem 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.subsection {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2e7d32;
    margin: 1.5rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #e8f5e9;
}

/* Alert styles */
.alert {
    padding: 1.25rem 1.5rem;
    border-radius: 12px;
    margin: 1.5rem 0;
    font-size: 1rem;
    line-height: 1.6;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.alert-success {
    background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
    border-left: 5px solid #28a745;
    color: #155724;
}

.alert-warning {
    background: linear-gradient(135deg, #fff3cd 0%, #ffeeba 100%);
    border-left: 5px solid #ffc107;
    color: #856404;
}

.alert-error {
    background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
    border-left: 5px solid #dc3545;
    color: #721c24;
}

.alert-info {
    background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%);
    border-left: 5px solid #17a2b8;
    color: #0c5460;
}

.alert strong {
    font-weight: 700;
    font-size: 1.1rem;
}

/* Metrics */
.metrics {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin: 1.5rem 0;
}

.metric {
    background: linear-gradient(135deg, #f1f8f4, #e8f5e9);
    border: 2px solid #c8e6c9;
    border-radius: 12px;
    padding: 1.5rem 1rem;
    text-align: center;
    transition: all 0.3s ease;
}

.metric:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(46, 125, 50, 0.2);
    border-color: #2e7d32;
}

.metric-value {
    font-size: 2rem;
    font-weight: 800;
    color: #1b5e20;
    margin-bottom: 0.3rem;
}

.metric-label {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #2e7d32;
    font-weight: 600;
}

/* Guidelines box */
.guidelines {
    background: linear-gradient(135deg, #f9fafb, #f1f8f4);
    border: 2px solid #c8e6c9;
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 1.5rem;
}

.guidelines strong {
    color: #1b5e20;
    font-size: 1.1rem;
}

.guidelines ul {
    margin: 1rem 0 0 0;
    padding-left: 1.5rem;
}

.guidelines li {
    font-size: 0.95rem;
    color: #4B5563;
    line-height: 1.7;
    margin-bottom: 0.5rem;
}

/* Button styling */
.stButton > button {
    background: linear-gradient(135deg, #2e7d32, #43a047) !important;
    color: #FFFFFF !important;
    border: none !important;
    padding: 0.9rem 2rem !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    border-radius: 50px !important;
    width: 100% !important;
    margin-top: 1.5rem !important;
    box-shadow: 0 6px 20px rgba(46, 125, 50, 0.3) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #1b5e20, #2e7d32) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(46, 125, 50, 0.4) !important;
}

/* Input field styling */
label {
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    color: #1b5e20 !important;
    margin-bottom: 0.5rem !important;
}

.stSelectbox > div > div,
.stNumberInput > div > div,
.stSlider > div > div {
    border-radius: 10px !important;
}

/* Slider styling */
.stSlider > div > div > div > div {
    background: #2e7d32 !important;
}

/* Expander styling */
.streamlit-expanderHeader {
    background: linear-gradient(135deg, #f1f8f4, #e8f5e9);
    border-radius: 10px;
    font-weight: 600;
    color: #1b5e20;
}

/* Plotly chart container */
.js-plotly-plot {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_models():
    with open('models/regression_model.pkl', 'rb') as f:
        reg_model = pickle.load(f)
    with open('models/classification_model.pkl', 'rb') as f:
        clf_model = pickle.load(f)
    with open('models/label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
    return reg_model, clf_model, label_encoder

try:
    reg_model, clf_model, label_encoder = load_models()
    models_loaded = True
except Exception as e:
    models_loaded = False
    st.error(f"⚠️ Error loading models: {str(e)}\n\nPlease run `python train_model.py` to generate new models.")

# Page Header
st.markdown("""
<div class="page-header">
    <h1>💧 Irrigation Advisor</h1>
    <p class="subtitle">Get personalized irrigation recommendations based on real-time field data</p>
</div>
""", unsafe_allow_html=True)

# INPUT SECTION
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📊 Input Parameters</div>', unsafe_allow_html=True)

crop = st.selectbox("🌾 Crop Type", ["Rice", "Maize"])

st.markdown('<div class="subsection">🌤️ Environmental Conditions</div>', unsafe_allow_html=True)
temperature = st.slider("Temperature (°C)", 15.0, 35.0, 25.0, 0.5)
humidity = st.slider("Humidity (%)", 40.0, 100.0, 70.0, 1.0)
rainfall = st.slider("Recent Rainfall (mm)", 0.0, 300.0, 100.0, 5.0)

st.markdown('<div class="subsection">🌱 Soil Parameters</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    nitrogen = st.number_input("Nitrogen (N)", 0, 150, 80)
with c2:
    phosphorus = st.number_input("Phosphorus (P)", 0, 150, 50)

c3, c4 = st.columns(2)
with c3:
    potassium = st.number_input("Potassium (K)", 0, 150, 40)
with c4:
    ph = st.number_input("Soil pH", 3.0, 10.0, 6.5, 0.1)

predict_button = st.button("🔍 Analyze & Get Recommendation")
st.markdown('</div>', unsafe_allow_html=True)

# RESULTS SECTION
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📋 Analysis Results</div>', unsafe_allow_html=True)

if models_loaded and predict_button:
    crop_encoded = label_encoder.transform([crop.lower()])[0]
    input_data = pd.DataFrame({
        'N': [nitrogen], 'P': [phosphorus], 'K': [potassium],
        'temperature': [temperature], 'humidity': [humidity],
        'ph': [ph], 'rainfall': [rainfall], 'crop_encoded': [crop_encoded]
    })
    
    water_req = reg_model.predict(input_data)[0]
    extra = max(0.0, water_req - rainfall)
    decision = clf_model.predict(input_data)[0]
    proba = clf_model.predict_proba(input_data)[0]
    classes = clf_model.classes_
    
    # Calculate deficit for rule-based classification
    deficit = water_req - rainfall
    deficit_percent = (deficit / water_req * 100) if water_req > 0 else 0
    
    # Rule-based classification
    if deficit > 40 or deficit_percent > 30:
        rule_based_decision = "Irrigate Now"
    elif deficit > 15 or deficit_percent > 10:
        rule_based_decision = "Irrigate Soon"
    else:
        rule_based_decision = "No Irrigation Needed"
    
    decision = rule_based_decision
    model_decision = clf_model.predict(input_data)[0]
    max_proba = max(proba)
    
    # Debug info
    with st.expander("🔍 Debug Information"):
        st.write(f"**Model Prediction:** {model_decision} (Confidence: {max_proba*100:.1f}%)")
        st.write(f"**Rule-based Decision:** {rule_based_decision}")
        st.write(f"**Water Requirement:** {water_req:.1f} mm")
        st.write(f"**Rainfall:** {rainfall:.1f} mm")
        st.write(f"**Deficit:** {deficit:.1f} mm ({deficit_percent:.1f}%)")
        st.write(f"**Model Probabilities:**")
        for cls, prob in zip(classes, proba):
            st.write(f"  - {cls}: {prob*100:.1f}%")
    
    # Decision Alert
    if decision == "Irrigate Now":
        st.markdown(
            '<div class="alert alert-error"><strong>⚠️ Status: Irrigate Now</strong><br>Immediate irrigation required within 6–12 hours. Water deficit is critical.</div>',
            unsafe_allow_html=True
        )
    elif decision == "Irrigate Soon":
        st.markdown(
            '<div class="alert alert-warning"><strong>⏰ Status: Irrigate Soon</strong><br>Schedule irrigation within 1–2 days to maintain optimal growth conditions.</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="alert alert-success"><strong>✅ Status: No Irrigation Needed</strong><br>Current water conditions are adequate for crop requirements.</div>',
            unsafe_allow_html=True
        )
    
    # Metrics
    st.markdown(f"""
    <div class="metrics">
        <div class="metric">
            <div class="metric-value">{water_req:.1f} mm</div>
            <div class="metric-label">Weekly Water Need</div>
        </div>
        <div class="metric">
            <div class="metric-value">{extra:.1f} mm</div>
            <div class="metric-label">Extra Irrigation Required</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(
        f'<div class="alert alert-info"><strong>💧 Water Conversion:</strong> {extra:.1f} mm = {extra:.1f} liters per square meter</div>',
        unsafe_allow_html=True
    )
    
    # Confidence Chart
    st.markdown("**📊 Prediction Confidence**")
    fig = go.Figure(
        data=[go.Bar(
            x=classes,
            y=proba * 100,
            marker_color=['#2e7d32', '#43a047', '#66bb6a'],
            text=[f'{p:.1f}%' for p in proba * 100],
            textposition='auto',
            textfont=dict(size=14, color='white', family='Inter')
        )]
    )
    fig.update_layout(
        xaxis_title="Decision Category",
        yaxis_title="Confidence (%)",
        showlegend=False,
        height=250,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=10, b=0),
        font=dict(family='Inter', size=12)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Optimal Timing
    st.markdown("**⏰ Optimal Irrigation Timing**")
    if decision != "No Irrigation Needed" and extra > 0:
        timing = (
            "🌅 Early morning (5–7 AM) or 🌆 late evening (6–8 PM)"
            if temperature > 28
            else "🌄 Morning (7–10 AM) or 🌇 evening (5–7 PM)"
        )
        st.markdown(
            f'<div class="alert alert-info"><strong>Best Time:</strong> {timing}<br><small>Timing optimizes water absorption and reduces evaporation losses.</small></div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="alert alert-success"><strong>✅ No immediate irrigation required</strong><br>Monitor conditions and check again in 2-3 days.</div>',
            unsafe_allow_html=True
        )
    
    # Crop Guidelines
    st.markdown(f"""
    <div class="guidelines">
        <strong>🌾 {crop} Specific Guidelines:</strong>
        <ul>
            {'<li>Maintain 2–5 cm standing water during vegetative growth phase</li><li>Optimal temperature: 20–25°C with humidity above 80%</li><li>Ensure consistent water levels to prevent stress</li><li>Monitor for nutrient leaching in flooded conditions</li>'
              if crop.lower() == 'rice'
              else '<li>Apply deep but infrequent irrigation to encourage deep roots</li><li>Optimal temperature: 20–30°C with humidity 60–70%</li><li>Allow soil to dry slightly between irrigations</li><li>Avoid waterlogging to prevent root diseases</li>'}
        </ul>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(
        '<div class="alert alert-info"><strong>ℹ️ Ready to Analyze</strong><br>Set your field parameters above and click <strong>Analyze & Get Recommendation</strong> to receive personalized irrigation guidance.</div>',
        unsafe_allow_html=True
    )
    
    st.markdown(f"""
    <div class="guidelines">
        <strong>📚 Typical {crop} Ranges:</strong>
        <ul>
            {'<li><strong>Temperature:</strong> 20–26°C</li><li><strong>Humidity:</strong> 75–90%</li><li><strong>Rainfall:</strong> 150–250 mm/week</li><li><strong>Soil pH:</strong> 6.0–7.0</li><li><strong>Nitrogen:</strong> 80–120 kg/ha</li>'
              if crop == 'Rice'
              else '<li><strong>Temperature:</strong> 21–27°C</li><li><strong>Humidity:</strong> 60–75%</li><li><strong>Rainfall:</strong> 50–100 mm/week</li><li><strong>Soil pH:</strong> 5.8–7.0</li><li><strong>Nitrogen:</strong> 120–180 kg/ha</li>'}
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)