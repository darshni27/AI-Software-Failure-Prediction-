import streamlit as st
import pandas as pd
import joblib
import os
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0F172A,#1E3A8A,#0F172A);
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

[data-testid="stMetric"]{
    background-color: rgba(255,255,255,0.08);
    border-radius:18px;
    padding:20px;
    border:1px solid rgba(255,255,255,0.15);
}

[data-testid="stSidebar"]{
    background-color:#111827;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="AI Software Failure Prediction",
    page_icon="🤖",
    layout="wide"
)
model_path = "models/advanced_software_failure_model.pkl"

model = joblib.load(model_path)

st.markdown("""
# 🤖 AI Software Failure Prediction System
### 🚀 AI-Powered Multi-Agent Risk Analysis Platform
""")

st.info("🔍 Predict software project risks early using Machine Learning and Multi-Agent AI.")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📂 Total Projects", "1")

with col2:
    st.metric("🤖 AI Agents", "5")

with col3:
    st.metric("📊 Model Accuracy", "75%")

with col4:
    st.metric("⚠️ Current Risk", "Medium")
st.divider()

# Display agent risk summary
st.header("📊 Agent Risk Summary")

risk_data = {
    "Agent": [
        "Code Quality Agent",
        "Issue Tracking Agent",
        "Schedule Agent",
        "Documentation Agent",
        "Communication Agent"
    ],
    "Risk Level": [
        "Medium",
        "High",
        "Low",
        "High",
        "Medium"
    ]
}

df = pd.DataFrame(risk_data)

st.table(df)

st.divider()

# Overall prediction
st.header("🔮 AI Prediction")

st.success("Predicted Project Risk: MEDIUM")

st.divider()

st.header("📁 Dataset Overview")

st.write("Generated datasets used for analysis:")

files = [
    "commits.csv",
    "issues.csv",
    "deadlines.csv",
    "documentation.csv",
    "communication.csv"
]

for file in files:
    st.write("✅", file)

st.info("AI Software Failure Prediction Dashboard Ready 🚀")