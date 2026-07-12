import pandas as pd

# Load documentation dataset
docs = pd.read_csv("data/documentation.csv")

# Calculate metrics
total_documents = len(docs)
complete = len(docs[docs["Status"] == "Complete"])
incomplete = len(docs[docs["Status"] == "Incomplete"])
missing = len(docs[docs["Status"] == "Missing"])

# Risk Analysis
if missing > 30:
    risk = "HIGH"
elif missing > 15:
    risk = "MEDIUM"
else:
    risk = "LOW"

# Print Report
print("===== Documentation Agent =====")
print(f"Total Documents: {total_documents}")
print(f"Complete: {complete}")
print(f"Incomplete: {incomplete}")
print(f"Missing: {missing}")
print(f"Risk Level: {risk}")