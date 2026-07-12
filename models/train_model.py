import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load datasets
commits = pd.read_csv("data/commits.csv")
issues = pd.read_csv("data/issues.csv")
deadlines = pd.read_csv("data/deadlines.csv")
documentation = pd.read_csv("data/documentation.csv")
communication = pd.read_csv("data/communication.csv")

# Create a simple training dataset
training_data = pd.DataFrame({
    "Commits": commits["Commits"][:100],
    "Lines_Added": commits["Lines_Added"][:100],
    "Files_Changed": commits["Files_Changed"][:100],
})

# Dummy target labels
training_data["Risk"] = [
    0 if x < 4 else 1 if x < 7 else 2
    for x in training_data["Commits"]
]

X = training_data[["Commits", "Lines_Added", "Files_Changed"]]
y = training_data["Risk"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "models/software_failure_model.pkl")

print("AI Model Trained Successfully!")
print("Model saved as software_failure_model.pkl")