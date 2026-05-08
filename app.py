# HR Management Streamlit App

## Folder Structure

```text
hr_management_app/
│
├── app.py
├── logo.png
├── requirements.txt
│
├── attendance.py
├── weekly_report.py
├── payroll.py
└── appraisal.py
```

---

# 1. app.py

```python
import streamlit as st
from PIL import Image

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="HR Management System",
    page_icon="🏢",
    layout="wide"
)

# ==========================================
# LOAD LOGO
# ==========================================
logo = Image.open("logo.png")

# ==========================================
# CUSTOM STYLING
# ==========================================
st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
    }

    h1, h2, h3 {
        color: black;
    }

    .main-title {
        color: orange;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
    }

    .card {
        background-color: #f9f9f9;
        padding: 30px;
        border-radius: 15px;
        border-left: 8px solid orange;
        margin-bottom: 20px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    }

    .footer {
        text-align: center;
        color: gray;
        margin-top: 30px;
    }

    div.stButton > button {
        background-color: orange;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 25px;
        font-size: 16px;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# HEADER
# ==========================================
col1, col2 = st.columns([1, 5])

with col1:
    st.image(logo, width=100)

with col2:
    st.markdown('<p class="main-title">HR MANAGEMENT SYSTEM</p>', unsafe_allow_html=True)

st.write("---")

# ==========================================
# SIDEBAR MENU
# ==========================================
st.sidebar.image(logo, width=150)
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Attendance",
        "Weekly Report",
        "Payroll",
        "Appraisal"
    ]
)

# ==========================================
# HOME PAGE
# ==========================================
if menu == "Home":

    st.markdown(
        """
        <div class="card">
        <h2>Welcome to the HR Management System</h2>
        <p>
        This system helps HR teams manage:
        </p>
        <ul>
            <li>Employee Attendance</li>
            <li>Weekly Reports</li>
            <li>Payroll Processing</li>
            <li>Performance Appraisal</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            """
            <div class="card">
            <h3>Attendance Module</h3>
            <p>Track employee attendance and punctuality.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
            <h3>Payroll Module</h3>
            <p>Manage salaries, deductions, and payslips.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="card">
            <h3>Weekly Report</h3>
            <p>Monitor weekly staff activities and reports.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="card">
            <h3>Appraisal Module</h3>
            <p>Evaluate employee performance and growth.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================
# ATTENDANCE PAGE
# ==========================================
elif menu == "Attendance":

    st.title("📅 Attendance Management")

    st.info("Attendance application goes here.")

    st.write("You can connect your attendance system here.")

# ==========================================
# WEEKLY REPORT PAGE
# ==========================================
elif menu == "Weekly Report":

    st.title("📝 Weekly Report")

    employee = st.text_input("Employee Name")
    report = st.text_area("Weekly Report")

    if st.button("Submit Report"):
        st.success(f"Weekly report submitted for {employee}")

# ==========================================
# PAYROLL PAGE
# ==========================================
elif menu == "Payroll":

    st.title("💰 Payroll System")

    employee = st.text_input("Employee Name")
    salary = st.number_input("Monthly Salary", min_value=0)

    if st.button("Generate Payroll"):
        st.success(f"Payroll generated for {employee}")
        st.write(f"Monthly Salary: ₦{salary:,.2f}")

# ==========================================
# APPRAISAL PAGE
# ==========================================
elif menu == "Appraisal":

    st.title("⭐ Employee Appraisal")

    employee = st.text_input("Employee Name ")
    rating = st.slider("Performance Rating", 1, 10)
    comment = st.text_area("Manager Comment")

    if st.button("Submit Appraisal"):
        st.success(f"Appraisal submitted for {employee}")
        st.write(f"Performance Rating: {rating}/10")

# ==========================================
# FOOTER
# ==========================================
st.write("---")
st.markdown(
    '<div class="footer">HR Management System © 2026</div>',
    unsafe_allow_html=True
)
```

---

# 2. requirements.txt

```text
streamlit
pandas
Pillow
```

---

# HOW TO RUN

Open terminal and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

# FEATURES INCLUDED

✅ Orange, black and white theme
✅ Logo support (`logo.png`)
✅ Sidebar navigation
✅ Attendance section
✅ Weekly report section
✅ Payroll section
✅ Employee appraisal section
✅ Modern HR dashboard layout

---

# HOW TO ADD YOUR EXISTING APPS

Replace these sections:

```python
st.info("Attendance application goes here.")
```

with your existing attendance app code.

You can also move each module into separate files and import them later.
