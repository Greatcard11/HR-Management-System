import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="HR Management System",
    page_icon="logo.png",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>

    .stApp {
        background-color: #000000;
        color: white;
    }

    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #ff7a00;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #d1d5db;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .card {
        background-color: #111111;
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #ff7a00;
        box-shadow: 0px 4px 15px rgba(255,122,0,0.2);
        margin-bottom: 20px;
    }

    .card h3 {
        color: #ff7a00;
        margin-bottom: 10px;
    }

    .card p {
        color: #f1f1f1;
        font-size: 15px;
    }

    .stButton > button {
        background-color: #ff7a00;
        color: white;
        border-radius: 10px;
        border: none;
        height: 45px;
        width: 100%;
        font-weight: bold;
        font-size: 15px;
    }

    .stButton > button:hover {
        background-color: #e66d00;
        color: white;
    }

    section[data-testid="stSidebar"] {
        background-color: #111111;
    }

    .sidebar-title {
        color: #ff7a00;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGO
# =========================================
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

    st.title("📅 Attendance Management System")

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
