import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/advanced_software_failure_model.pkl")

# Example project data
sample = pd.DataFrame({
    "Commits": [7],
    "Lines_Added": [420],
    "Files_Changed": [9],
    "Bugs": [8],
    "Days_Left": [5],
    "Documentation": [65],
    "Messages": [32]
})

prediction = model.predict(sample)

risk = {
    0: "LOW",
    1: "MEDIUM",
    2: "HIGH"
}

print("========== ADVANCED AI PREDICTION ==========")
print("Predicted Project Risk:", risk[prediction[0]])