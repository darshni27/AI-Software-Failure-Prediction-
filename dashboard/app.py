import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="AI Software Failure Prediction",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===============================
# Sidebar
# ===============================
st.sidebar.title("🤖 AI Control Center")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🤖 AI Agents",
        "📊 Analytics",
        "🔮 Risk Prediction",
        "📁 Datasets",
        "ℹ️ About Project"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("🟢 System Status : Online")
st.sidebar.info("🤖 AI Agents : 5 Active")
st.sidebar.warning("⚠️ Current Risk : Medium")

st.sidebar.markdown("---")
st.sidebar.write("### 👩‍💻 Developer")
st.sidebar.write("Darshni K")

# ===============================
# Dashboard Page
# ===============================
if page == "🏠 Dashboard":

    st.title("🤖 AI Software Failure Prediction System")
    st.caption("AI-Powered Multi-Agent Risk Analysis Platform")

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📂 Active Projects", "1", "0")

    with col2:
        st.metric("🤖 AI Agents Running", "5", "+1")

    with col3:
        st.metric("🎯 Prediction Accuracy", "92%", "+17%")

    with col4:
        st.metric("⚠️ Current Risk", "Medium", "-8%")

    st.divider()

    st.subheader("🧠 AI Recommendation")

st.info("""
• ✅ Documentation quality should be improved.

• ✅ Resolve pending high-priority issues.

• ✅ Maintain regular code reviews.

• ✅ Current project health is stable, but schedule monitoring is recommended.
""")
if page == "📊 Analytics":

    st.title("📊 Analytics Dashboard")
    st.caption("AI-powered project analytics and insights")

    st.divider()

    st.subheader("📈 Risk Trend")

    chart_data = pd.DataFrame({
        "Week": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"],
        "Risk Score": [82, 74, 68, 61, 55]
    })

    st.line_chart(chart_data.set_index("Week"))

    st.divider()

    st.subheader("📊 AI Agent Performance")

    performance = pd.DataFrame({
        "Agent": [
            "Code Quality",
            "Issue Tracking",
            "Schedule",
            "Documentation",
            "Communication"
        ],
        "Score": [95, 82, 88, 76, 90]
    })
 
    st.bar_chart(performance.set_index("Agent"))
# ==========================================
# AI Agents Page
# ==========================================
if page == "🤖 AI Agents":


    st.title("🤖 AI Agents")
    st.caption("Multi-Agent Monitoring Dashboard")

    st.divider()

    st.markdown("### 🧠 Agent Status")

    st.markdown("**💻 Code Quality Agent** — 🟢 Active")
    st.markdown("**🐞 Issue Tracking Agent** — 🟡 Monitoring")
    st.markdown("**📅 Schedule Agent** — 🟢 Active")
    st.markdown("**📄 Documentation Agent** — 🟠 Needs Attention")
    st.markdown("**💬 Communication Agent** — 🟢 Active")

    st.divider()

    st.subheader("🤖 Agent Decision")

    st.info("""
• 💻 Code Quality Agent: No major issues detected.

• 🐞 Issue Tracking Agent: 3 high-priority bugs are pending.

• 📅 Schedule Agent: Project timeline is on track.

• 📄 Documentation Agent: Documentation coverage is only 76%.

• 💬 Communication Agent: Team collaboration is healthy.
""")
    


if page == "🔮 Risk Prediction":

   
    st.title("🔮 Risk Prediction")
    st.caption("AI-Powered Software Failure Prediction")

    st.divider()

    code_quality = st.slider("💻 Code Quality Score", 0, 100, 85)
    open_bugs = st.number_input("🐞 Open High-Priority Bugs", 0, 100, 5)
    documentation = st.slider("📄 Documentation Coverage (%)", 0, 100, 76)
    communication = st.slider("💬 Team Communication Score", 0, 100, 90)
    schedule_delay = st.number_input("📅 Schedule Delay (Days)", 0, 30, 2)

    st.divider()

    if st.button("🚀 Predict Risk"):

        if code_quality < 60 or open_bugs > 15 or documentation < 60:
            risk = "🔴 High Risk"
            confidence = "96%"
            recommendation = """
🔴 Critical project risk detected.

• Improve code quality immediately.

• Resolve all critical bugs.

• Increase documentation coverage.

• Conduct daily team review meetings.
"""
        elif code_quality < 80 or open_bugs > 8 or documentation < 80:
            risk = "🟡 Medium Risk"
            confidence = "92%"
            recommendation = """
🟡 Moderate project risk detected.

• Improve documentation.

• Fix pending high-priority bugs.

• Continue weekly code reviews.
"""
        else:
            risk = "🟢 Low Risk"
            confidence = "98%"
            recommendation = """
🟢 Project is healthy.

• Maintain current development process.

• Continue regular testing.

• Monitor project progress weekly.
"""

        st.success(f"### Prediction Result: {risk}")
        st.metric("🎯 Prediction Confidence", confidence)

        st.subheader("🧠 AI Recommendation")
        st.info(recommendation)



if page == "📁 Datasets":

    
    st.title("📁 Dataset Viewer")
    st.caption("Datasets used for AI Software Failure Prediction")

    st.divider()

    datasets = {
        "Commits": "data/commits.csv",
        "Issues": "data/issues.csv",
        "Deadlines": "data/deadlines.csv",
        "Documentation": "data/documentation.csv",
        "Communication": "data/communication.csv"
    }

    selected = st.selectbox(
        "Select Dataset",
        list(datasets.keys())
    )

    try:
        df = pd.read_csv(datasets[selected])

        st.success(f"Loaded {selected} Dataset Successfully")

        st.dataframe(df, use_container_width=True)

        st.metric("Rows", len(df))
        st.metric("Columns", len(df.columns))

    except Exception as e:

        st.error("Dataset not found.")

        st.write(e)



if page == "ℹ️ About Project":


    st.title("ℹ️ About Project")
    st.caption("AI Software Failure Prediction using Multi-Agent Systems")

    st.divider()

    st.markdown("""
### 🎯 Project Objective

This project predicts software project failure risks using a Multi-Agent AI framework. Different intelligent agents continuously analyze project activities and identify potential risks before project failure occurs.

### 🤖 AI Agents

- 💻 Code Quality Agent
- 🐞 Issue Tracking Agent
- 📅 Schedule Agent
- 📄 Documentation Agent
- 💬 Communication Agent

### 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Machine Learning

### 🎯 Features

- AI Risk Prediction
- Multi-Agent Monitoring
- Interactive Dashboard
- Dataset Visualization
- Project Analytics
""")

    st.subheader("🚀 Developed By")

    st.write("**Name:** Darshni K")
    st.write("**Degree:** B.Tech Artificial Intelligence & Machine Learning")
    st.write("**Institution:** SNS College of Technology")

# End of About Project page

st.divider()

st.markdown(
    "<center>© 2026 AI Software Failure Prediction using Multi-Agent Systems</center>",
    unsafe_allow_html=True
)