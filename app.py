#import streamlit as st
#
#st.set_page_config(
#    page_title="Smart Irrigation Advisor",
#    page_icon="💧",
#    layout="centered"
#)
#
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
#        padding: 2.5rem 1.5rem !important;
#        max-width: 980px !important;
#    }
#    
#    /* Hero */
#    .hero {
#        padding: 52px 28px 48px 28px;
#        text-align: center;
#        background: radial-gradient(circle at top left, #ECFDF3 0, #F9FAFB 40%, #EFF6FF 100%);
#        border-radius: 24px;
#        margin-bottom: 40px;
#        border: 1px solid #E5E7EB;
#    }
#    
#    .hero-pill {
#        display: inline-flex;
#        align-items: center;
#        gap: 6px;
#        font-size: 11px;
#        text-transform: uppercase;
#        letter-spacing: 0.16em;
#        padding: 4px 10px;
#        border-radius: 999px;
#        background: rgba(22,163,74,0.08);
#        color: #15803D;
#        margin-bottom: 10px;
#        font-weight: 600;
#    }
#    
#    .hero-title {
#        font-size: 40px;
#        font-weight: 700;
#        color: #111827;
#        margin: 0 0 10px 0;
#        letter-spacing: -0.03em;
#    }
#    
#    .hero-subtitle {
#        font-size: 16px;
#        color: #4B5563;
#        margin: 0 0 20px 0;
#    }
#    
#    /* Feature Card */
#    .feature-grid {
#        display: grid;
#        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
#        gap: 18px;
#        margin-bottom: 30px;
#    }
#    
#    .feature {
#        background: #F9FAFB;
#        border: 1px solid #3e6835;
#        border-radius: 18px;
#        padding: 22px;
#    }
#    
#    .feature-tag {
#        font-size: 11px;
#        font-weight: 600;
#        color: #15803D;
#        margin-bottom: 10px;
#        letter-spacing: 0.14em;
#        text-transform: uppercase;
#    }
#    
#    .feature-title {
#        font-size: 18px;
#        font-weight: 600;
#        color: #111827;
#        margin-bottom: 6px;
#    }
#    
#    .feature-desc {
#        font-size: 14px;
#        color: #4B5563;
#        line-height: 1.6;
#        margin: 0;
#    }
#    
#    /* Stats */
#    .stats {
#        display: grid;
#        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
#        gap: 18px;
#        padding: 22px 22px 18px 22px;
#        margin: 10px 0 40px 0;
#        background: #F9FAFB;
#        border-radius: 18px;
#        border: 1px solid #E5E7EB;
#    }
#    
#    .stat {
#        text-align: center;
#    }
#    
#    .stat-number {
#        font-size: 26px;
#        font-weight: 700;
#        color: #111827;
#        margin-bottom: 3px;
#    }
#    
#    .stat-label {
#        font-size: 12px;
#        color: #15803D;
#        text-transform: uppercase;
#        letter-spacing: 0.12em;
#    }
#    
#    /* Section heading */
#    h2 {
#        font-size: 26px !important;
#        font-weight: 700 !important;
#        color: #111827 !important;
#        text-align: center !important;
#        margin: 32px 0 20px 0 !important;
#        letter-spacing: -0.02em !important;
#    }
#    
#    .section-subtitle {
#        text-align: center;
#        font-size: 14px;
#        color: #6B7280;
#        margin-bottom: 18px;
#    }
#    
#    /* Steps */
#    .steps-grid {
#        display: grid;
#        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
#        gap: 18px;
#        margin-bottom: 32px;
#    }
#    
#    .step {
#        background: #F9FAFB;
#        border: 1px solid #15803d;
#        border-radius: 18px;
#        padding: 20px 20px 18px 20px;
#    }
#    
#    .step-number {
#        width: 28px;
#        height: 28px;
#        border-radius: 999px;
#        display: inline-flex;
#        align-items: center;
#        justify-content: center;
#        background: #DCFCE7;
#        color: #15803D;
#        font-size: 14px;
#        font-weight: 600;
#        margin-bottom: 10px;
#    }
#    
#    .step-title {
#        font-size: 16px;
#        font-weight: 600;
#        color: #111827;
#        margin-bottom: 6px;
#    }
#    
#    .step-desc {
#        font-size: 14px;
#        color: #4B5563;
#        line-height: 1.6;
#        margin: 0;
#    }
#    
#    /* Use cases */
#    .usecase-grid {
#        display: grid;
#        grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
#        gap: 18px;
#        margin-bottom: 40px;
#    }
#    
#    .usecase {
#        border-radius: 16px;
#        border: 1px solid #15803d;
#        padding: 18px 18px 16px 18px;
#        background: #FFFFFF;
#    }
#    
#    .usecase-label {
#        font-size: 12px;
#        font-weight: 600;
#        color: #6B7280;
#        text-transform: uppercase;
#        letter-spacing: 0.14em;
#        margin-bottom: 4px;
#    }
#    
#    .usecase-title {
#        font-size: 15px;
#        font-weight: 600;
#        color: #111827;
#        margin-bottom: 6px;
#    }
#    
#    .usecase-desc {
#        font-size: 13px;
#        color: #4B5563;
#        line-height: 1.6;
#    }
#    
#    /* CTA */
#    .cta {
#        padding: 30px 22px 28px 22px;
#        text-align: center;
#        background: linear-gradient(135deg, #16A34A, #22C55E);
#        border-radius: 20px;
#        margin: 20px 0 0 0;
#        color: #ECFDF3;
#    }
#    
#    .cta-title {
#        font-size: 22px;
#        font-weight: 700;
#        margin-bottom: 6px;
#    }
#    
#    .cta-subtitle {
#        font-size: 14px;
#        color: #DCFCE7;
#        margin-bottom: 20px;
#    }
#    
#    .stButton > button {
#        background: #FFFFFF !important;
#        color: #15803D !important;
#        border: none !important;
#        padding: 10px 30px !important;
#        font-size: 15px !important;
#        font-weight: 600 !important;
#        border-radius: 999px !important;
#    }
#    
#    .stButton > button:hover {
#        background: #F3F4F6 !important;
#    }
#</style>
#""", unsafe_allow_html=True)
#
## Hero
#st.markdown("""
#<div class="hero">
#    <div class="hero-pill">Smart irrigation • AI powered</div>
#    <h1 class="hero-title">Smart Irrigation Advisor</h1>
#    <p class="hero-subtitle">Turn field data into precise, water-efficient irrigation decisions.</p>
#</div>
#""", unsafe_allow_html=True)
#
## Features in a grid
#st.markdown("""
#<div class="feature-grid">
#    <div class="feature">
#        <div class="feature-tag">Precision</div>
#        <h3 class="feature-title">97.5% model accuracy</h3>
#        <p class="feature-desc">Trained on real crop and soil data to estimate weekly water needs with high confidence.</p>
#    </div>
#    <div class="feature">
#        <div class="feature-tag">Intelligence</div>
#        <h3 class="feature-title">Context-aware guidance</h3>
#        <p class="feature-desc">Accounts for temperature, humidity, rainfall, and soil nutrients instead of fixed rules.</p>
#    </div>
#    <div class="feature">
#        <div class="feature-tag">Efficiency</div>
#        <h3 class="feature-title">Less waste, more yield</h3>
#        <p class="feature-desc">Avoids over-irrigation, protects soil health, and helps you plan irrigation windows.</p>
#    </div>
#</div>
#""", unsafe_allow_html=True)
#
## Stats
#st.markdown("""
#<div class="stats">
#    <div class="stat">
#        <div class="stat-number">97.5%</div>
#        <div class="stat-label">Accuracy</div>
#    </div>
#    <div class="stat">
#        <div class="stat-number">2</div>
#        <div class="stat-label">Crops</div>
#    </div>
#    <div class="stat">
#        <div class="stat-number">8</div>
#        <div class="stat-label">Parameters</div>
#    </div>
#    <div class="stat">
#        <div class="stat-number">100%</div>
#        <div class="stat-label">R² Score</div>
#    </div>
#</div>
#""", unsafe_allow_html=True)
#
## How It Works
#st.markdown("## How It Works")
#st.markdown('<p class="section-subtitle">From field measurements to clear irrigation actions in three quick steps.</p>', unsafe_allow_html=True)
#
#st.markdown("""
#<div class="steps-grid">
#    <div class="step">
#        <div class="step-number">1</div>
#        <h3 class="step-title">Input your conditions</h3>
#        <p class="step-desc">Select your crop and add basic information like temperature, humidity, rainfall, and soil nutrients.</p>
#    </div>
#    <div class="step">
#        <div class="step-number">2</div>
#        <h3 class="step-title">AI evaluates water need</h3>
#        <p class="step-desc">The model processes 8 parameters to estimate weekly water demand and irrigation urgency.</p>
#    </div>
#    <div class="step">
#        <div class="step-number">3</div>
#        <h3 class="step-title">Act with confidence</h3>
#        <p class="step-desc">Get a clear "Irrigate Now / Soon / Not Needed" recommendation plus timing and guideline tips.</p>
#    </div>
#</div>
#""", unsafe_allow_html=True)
#
## Who is it for section
#st.markdown("## Who Is It For?")
#st.markdown('<p class="section-subtitle">Designed for anyone who wants smarter, calmer irrigation decisions.</p>', unsafe_allow_html=True)
#
#st.markdown("""
#<div class="usecase-grid">
#    <div class="usecase">
#        <div class="usecase-label">Field farmers</div>
#        <div class="usecase-title">Plan weekly irrigation</div>
#        <p class="usecase-desc">Use the tool as a quick check before turning pumps on or off, especially in water-limited regions.</p>
#    </div>
#    <div class="usecase">
#        <div class="usecase-label">Researchers & students</div>
#        <div class="usecase-title">Experiment with parameters</div>
#        <p class="usecase-desc">Change one variable at a time and see how recommended water levels respond.</p>
#    </div>
#    <div class="usecase">
#        <div class="usecase-label">Advisors</div>
#        <div class="usecase-title">Support data-driven advice</div>
#        <p class="usecase-desc">Combine local expertise with model outputs for more structured farmer recommendations.</p>
#    </div>
#</div>
#""", unsafe_allow_html=True)
#
## CTA
#st.markdown("""
#<div class="cta">
#    <h2 class="cta-title">Ready to try it on your field data?</h2>
#    <p class="cta-subtitle">Run a quick scenario and see how irrigation plans change with different conditions.</p>
#</div>
#""", unsafe_allow_html=True)
#
#cta_col = st.columns([1, 1, 1])[1]
#with cta_col:
#    if st.button("Open Irrigation Advisor", use_container_width=True):
#        st.switch_page("pages/2_Irrigation_Advisor")




import streamlit as st

st.set_page_config(
    page_title="Smart Irrigation Advisor",
    page_icon="💧",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main background with animated gradient */
    .stApp {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 30%, #a5d6a7 60%, #81c784 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1b5e20 0%, #2e7d32 50%, #388e3c 100%);
        border-right: 3px solid #0d3d14;
        box-shadow: 4px 0 20px rgba(0,0,0,0.2);
    }
    
    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }
    
    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p {
        color: #ffffff !important;
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
    
    /* Hero section */
    .hero-section {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, rgba(27, 94, 32, 0.95), rgba(46, 125, 50, 0.95));
        border-radius: 30px;
        margin: 2rem auto;
        max-width: 1200px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: pulse 8s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        color: #ffffff;
        margin: 0 0 1rem 0;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
        letter-spacing: -1px;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #c8e6c9;
        margin-bottom: 2rem;
        position: relative;
        z-index: 1;
    }
    
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        color: #ffffff;
        font-weight: 600;
        margin-bottom: 1.5rem;
        border: 2px solid rgba(255,255,255,0.3);
        position: relative;
        z-index: 1;
    }
    
    /* Feature cards */
    .features-container {
        max-width: 1200px;
        margin: 3rem auto;
        padding: 0 2rem;
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: all 0.4s ease;
        border: 2px solid transparent;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 5px;
        background: linear-gradient(90deg, #2e7d32, #43a047, #66bb6a);
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 50px rgba(0,0,0,0.2);
        border-color: #2e7d32;
    }
    
    .feature-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1b5e20;
        margin-bottom: 0.75rem;
    }
    
    .feature-description {
        font-size: 1rem;
        color: #4B5563;
        line-height: 1.6;
    }
    
    /* Stats section */
    .stats-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 3rem 2rem;
        margin: 3rem auto;
        max-width: 1200px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        text-align: center;
    }
    
    .stat-item {
        padding: 1.5rem;
        border-radius: 15px;
        background: linear-gradient(135deg, #f1f8f4, #e8f5e9);
        transition: all 0.3s ease;
    }
    
    .stat-item:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(46, 125, 50, 0.2);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        color: #1b5e20;
        display: block;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1rem;
        color: #2e7d32;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* How it works section */
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1b5e20;
        text-align: center;
        margin: 3rem 0 1rem 0;
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .steps-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin: 2rem auto;
        max-width: 1200px;
        padding: 0 2rem;
    }
    
    .step-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 3px solid transparent;
    }
    
    .step-card:hover {
        border-color: #2e7d32;
        transform: translateY(-5px);
    }
    
    .step-number {
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #2e7d32, #43a047);
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0 auto 1.5rem auto;
        box-shadow: 0 5px 15px rgba(46, 125, 50, 0.3);
    }
    
    .step-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1b5e20;
        margin-bottom: 0.75rem;
    }
    
    .step-description {
        font-size: 1rem;
        color: #4B5563;
        line-height: 1.6;
    }
    
    /* CTA Section */
    .cta-section {
        background: linear-gradient(135deg, #1b5e20, #2e7d32, #43a047);
        border-radius: 30px;
        padding: 4rem 2rem;
        text-align: center;
        margin: 4rem auto;
        max-width: 1000px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        color: white;
    }
    
    .cta-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .cta-subtitle {
        font-size: 1.2rem;
        color: #c8e6c9;
        margin-bottom: 2rem;
    }
    
    /* Buttons */
    .stButton>button {
        background: white !important;
        color: #1b5e20 !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 1rem 3rem !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        background: #f1f8f4 !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 35px rgba(0,0,0,0.3) !important;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
        }
        
        .section-title {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">🌱 AI-Powered Agriculture Solution</div>
    <h1 class="hero-title">💧 Smart Irrigation Advisor</h1>
    <p class="hero-subtitle">Optimize Water Usage • Maximize Crop Yield • Sustainable Farming</p>
</div>
""", unsafe_allow_html=True)

# Feature Cards
st.markdown("""
<div class="features-container">
    <div class="features-grid">
        <div class="feature-card">
            <span class="feature-icon">🎯</span>
            <h3 class="feature-title">97.5% Accuracy</h3>
            <p class="feature-description">Advanced machine learning models trained on real crop and soil data to provide precise irrigation recommendations.</p>
        </div>
        <div class="feature-card">
            <span class="feature-icon">🧠</span>
            <h3 class="feature-title">Smart Analysis</h3>
            <p class="feature-description">Analyzes 8 key parameters including temperature, humidity, rainfall, and soil nutrients for context-aware guidance.</p>
        </div>
        <div class="feature-card">
            <span class="feature-icon">💰</span>
            <h3 class="feature-title">Resource Efficiency</h3>
            <p class="feature-description">Reduce water waste by up to 30% while improving crop yield and protecting soil health.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Stats Section
st.markdown("""
<div class="stats-container">
    <div class="stats-grid">
        <div class="stat-item">
            <span class="stat-number">97.5%</span>
            <span class="stat-label">Model Accuracy</span>
        </div>
        <div class="stat-item">
            <span class="stat-number">2</span>
            <span class="stat-label">Crop Types</span>
        </div>
        <div class="stat-item">
            <span class="stat-number">8</span>
            <span class="stat-label">Parameters</span>
        </div>
        <div class="stat-item">
            <span class="stat-number">100%</span>
            <span class="stat-label">R² Score</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# How It Works Section
st.markdown('<h2 class="section-title">How It Works</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">From field measurements to actionable irrigation decisions in three simple steps</p>', unsafe_allow_html=True)

st.markdown("""
<div class="steps-grid">
    <div class="step-card">
        <div class="step-number">1</div>
        <h3 class="step-title">Input Data</h3>
        <p class="step-description">Enter your crop type and current field conditions including temperature, humidity, rainfall, and soil nutrients (N, P, K, pH).</p>
    </div>
    <div class="step-card">
        <div class="step-number">2</div>
        <h3 class="step-title">AI Analysis</h3>
        <p class="step-description">Our machine learning models process all parameters to calculate precise weekly water requirements and irrigation urgency.</p>
    </div>
    <div class="step-card">
        <div class="step-number">3</div>
        <h3 class="step-title">Get Recommendations</h3>
        <p class="step-description">Receive clear guidance: "Irrigate Now", "Irrigate Soon", or "No Irrigation Needed" with optimal timing suggestions.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Who Is It For Section
st.markdown('<h2 class="section-title">Who Is It For?</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Designed for everyone in the agricultural ecosystem</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🚜</span>
        <h3 class="feature-title">Farmers</h3>
        <p class="feature-description">Make data-driven irrigation decisions and reduce water costs while improving crop health and yield.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🔬</span>
        <h3 class="feature-title">Researchers</h3>
        <p class="feature-description">Experiment with different parameters and understand how various conditions affect irrigation requirements.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">👨‍🌾</span>
        <h3 class="feature-title">Advisors</h3>
        <p class="feature-description">Support farmers with data-backed recommendations combining local expertise with AI insights.</p>
    </div>
    """, unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="cta-section">
    <h2 class="cta-title">Ready to Optimize Your Irrigation?</h2>
    <p class="cta-subtitle">Start making smarter irrigation decisions today with AI-powered insights</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Get Started - Try Irrigation Advisor", use_container_width=True):
        st.switch_page("pages/2_Irrigation_Advisor.py")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; padding: 2rem;'>© 2024 Smart Irrigation Advisor | Empowering Sustainable Agriculture 🌱| Made With Love - Monica Sharma </p>", unsafe_allow_html=True)