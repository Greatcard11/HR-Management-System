import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="HR Management System",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>

    .stApp {
        background-color: white;
    }

    /* HEADER */
    .main-title {
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        color: #00000;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #6b7280;
        font-size: 18px;
        margin-bottom: 40px;
    }

    /* CARD DESIGN */
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 18px;
        border-left: 6px solid #ff6b00;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 25px;
        border: 1px solid #f3f4f6;
        transition: 0.3s;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 6px 20px rgba(0,0,0,0.12);
    }

    .card h3 {
        color: #00000;
        margin-bottom: 10px;
    }

    .card p {
        color: #4b5563;
        line-height: 1.6;
        font-size: 15px;
    }
/* BUTTONS */
div.stLinkButton > a {
    background: #ff6b00 !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 12px 18px !important;
    font-weight: bold !important;
    text-align: center !important;
    width: 100% !important;
    display: block !important;
    text-decoration: none !important;
    opacity: 1 !important;
    visibility: visible !important;
}

    /* REMOVE EXTRA TOP SPACE */
    .block-container {
        padding-top: 1.5rem;
    }

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGO
# =========================================
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("logo.png", width=400)

# =========================================
# HEADER
# =========================================
st.markdown(
    '<div class="main-title">HR MANAGEMENT SYSTEM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Smart HR Operations & Employee Analytics Platform</div>',
    unsafe_allow_html=True
)

# =========================================
# LINKS
# =========================================
links = {
    "Attendance": "https://staff-attendance.streamlit.app/",
    "Employee Performance": "https://your-performance-app.streamlit.app/",
    "Appraisal": "https://your-appraisal-app.streamlit.app/",
    "KPI": "https://your-kpi-app.streamlit.app/"
}

# =========================================
# HOME PAGE
# =========================================
col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">
        <h3>📅 Attendance Management</h3>
        <p>
            Track employee attendance records, punctuality,
            daily check-ins and workforce presence.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Open Attendance System",
        links["Attendance"]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>📝 Employee Appraisal</h3>
        <p>
            Conduct employee appraisals, staff evaluations,
            reviews and assessment processes efficiently.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Open Appraisal System",
        links["Appraisal"]
    )

with col2:

    st.markdown("""
    <div class="card">
        <h3>📈 Employee Performance</h3>
        <p>
            Analyze employee productivity, targets,
            work efficiency and overall performance.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Open Performance System",
        links["Employee Performance"]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>📊 KPI Dashboard</h3>
        <p>
            Monitor HR KPIs, employee metrics,
            business growth and workforce insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Open KPI Dashboard",
        links["KPI"]
    )
