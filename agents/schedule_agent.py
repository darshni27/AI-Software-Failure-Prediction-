import pandas as pd

# Load deadline dataset
deadlines = pd.read_csv("data/deadlines.csv")

# Calculate metrics
total_tasks = len(deadlines)
delayed_tasks = len(deadlines[deadlines["Status"] == "Delayed"])
at_risk_tasks = len(deadlines[deadlines["Status"] == "At Risk"])
on_track_tasks = len(deadlines[deadlines["Status"] == "On Track"])

# Risk Analysis
if delayed_tasks > 30:
    risk = "HIGH"
elif delayed_tasks > 15:
    risk = "MEDIUM"
else:
    risk = "LOW"

# Print Report
print("===== Schedule Agent =====")
print(f"Total Tasks: {total_tasks}")
print(f"Delayed Tasks: {delayed_tasks}")
print(f"At Risk Tasks: {at_risk_tasks}")
print(f"On Track Tasks: {on_track_tasks}")
print(f"Risk Level: {risk}")