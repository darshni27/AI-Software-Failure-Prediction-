import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/software_failure_model.pkl")

# Example project data
new_project = pd.DataFrame({
    "Commits": [6],
    "Lines_Added": [350],
    "Files_Changed": [8]
})

# Predict
prediction = model.predict(new_project)

risk_levels = {
    0: "LOW",
    1: "MEDIUM",
    2: "HIGH"
}

print("===== AI Prediction =====")
print("Predicted Project Risk:", risk_levels[prediction[0]])