import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load training dataset
data = pd.read_csv("models/training_dataset.csv")

# Convert Risk labels to numbers
risk_mapping = {
    "LOW": 0,
    "MEDIUM": 1,
    "HIGH": 2
}

data["Risk"] = data["Risk"].map(risk_mapping)

# Features and Target
X = data.drop("Risk", axis=1)
y = data["Risk"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Test accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "models/advanced_software_failure_model.pkl")

print("Advanced AI Model Trained Successfully!")