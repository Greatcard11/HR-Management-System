import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="HR Management System",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"   # COLLAPSIBLE SIDEBAR
)

# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>

    /* MAIN BACKGROUND */
    .stApp {
        background-color: white;
        color: #111827;
    }

    /* HEADER */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        color: #ff6b00;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #6b7280;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* CARDS */
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 18px;
        border-left: 6px solid #ff6b00;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border: 1px solid #f3f4f6;
    }

    .card h3 {
        color: #ff6b00;
        margin-bottom: 10px;
    }

    .card p {
        color: #4b5563;
        font-size: 15px;
        line-height: 1.6;
    }

    /* BUTTONS */
    .stButton > button {
        background-color: #ff6b00;
        color: white;
        border-radius: 10px;
        border: none;
        height: 45px;
        width: 100%;
        font-weight: bold;
        font-size: 15px;
    }

    .stButton > button:hover {
        background-color: #e65f00;
        color: white;
    }

    /* LINK BUTTONS */
    div.stLinkButton > a {
        background-color: #ff6b00 !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 12px 18px !important;
        font-weight: bold !important;
        text-align: center !important;
        width: 100% !important;
    }

    div.stLinkButton > a:hover {
        background-color: #e65f00 !important;
        color: white !important;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    .sidebar-title {
        color: #ff6b00;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }

    /* RADIO BUTTON TEXT */
    .stRadio label {
        color: #111827 !important;
        font-weight: 500;
    }

    /* REMOVE TOP GAP */
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
    st.image("logo.png", width=120)

# =========================================
# LINKS
# =========================================
links = {
    "Attendance": "https://your-attendance-app.streamlit.app/",
    "Employee Performance": "https://your-performance-app.streamlit.app/",
    "Appraisal": "https://your-appraisal-app.streamlit.app/",
    "KPI": "https://your-kpi-app.streamlit.app/"
}

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
# SIDEBAR
# =========================================
st.sidebar.markdown(
    '<div class="sidebar-title">Navigation</div>',
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "",
    [
        "🏠 Home",
        "📅 Attendance",
        "📈 Employee Performance",
        "📝 Appraisal",
        "📊 KPI"
    ]
)

# =========================================
# HOME PAGE
# =========================================
if page == "🏠 Home":

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">
            <h3>📅 Attendance Management</h3>
            <p>
                Track employee attendance records, punctuality,
                and daily workforce presence.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button("Open Attendance System", links["Attendance"])

        st.markdown("""
        <div class="card">
            <h3>📝 Employee Appraisal</h3>
            <p>
                Conduct staff appraisals, evaluations,
                and performance reviews efficiently.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button("Open Appraisal System", links["Appraisal"])

    with col2:

        st.markdown("""
        <div class="card">
            <h3>📈 Employee Performance</h3>
            <p>
                Analyze employee productivity, targets,
                and overall work performance.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button("Open Performance System", links["Employee Performance"])

        st.markdown("""
        <div class="card">
            <h3>📊 KPI Dashboard</h3>
            <p>
                Monitor company HR KPIs, employee metrics,
                and organizational growth indicators.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button("Open KPI Dashboard", links["KPI"])

# =========================================
# ATTENDANCE PAGE
# =========================================
elif page == "📅 Attendance":

    st.title("📅 Attendance Management")

    st.components.v1.iframe(
        links["Attendance"],
        height=800
    )

# =========================================
# PERFORMANCE PAGE
# =========================================
elif page == "📈 Employee Performance":

    st.title("📈 Employee Performance")

    st.components.v1.iframe(
        links["Employee Performance"],
        height=800
    )

# =========================================
# APPRAISAL PAGE
# =========================================
elif page == "📝 Appraisal":

    st.title("📝 Employee Appraisal")

    st.components.v1.iframe(
        links["Appraisal"],
        height=800
    )

# =========================================
# KPI PAGE
# =========================================
elif page == "📊 KPI":

    st.title("📊 KPI Dashboard")

    st.components.v1.iframe(
        links["KPI"],
        height=800
    )
