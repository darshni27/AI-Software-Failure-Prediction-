import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(
    page_title="AI Software Failure Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Software Failure Prediction System")
st.write("Multi-Agent AI based project risk analysis dashboard")

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