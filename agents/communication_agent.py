import pandas as pd

# Load communication dataset
communication = pd.read_csv("data/communication.csv")

# Calculate metrics
total_messages = communication["Messages"].sum()
positive = len(communication[communication["Sentiment"] == "Positive"])
neutral = len(communication[communication["Sentiment"] == "Neutral"])
negative = len(communication[communication["Sentiment"] == "Negative"])

# Risk Analysis
if negative > 70:
    risk = "HIGH"
elif negative > 40:
    risk = "MEDIUM"
else:
    risk = "LOW"

# Print Report
print("===== Communication Agent =====")
print(f"Total Messages: {total_messages}")
print(f"Positive Messages: {positive}")
print(f"Neutral Messages: {neutral}")
print(f"Negative Messages: {negative}")
print(f"Risk Level: {risk}")