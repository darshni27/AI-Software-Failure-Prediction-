import pandas as pd

# Load issue dataset
issues = pd.read_csv("data/issues.csv")

# Calculate metrics
total_issues = len(issues)
open_issues = len(issues[issues["Status"] == "Open"])
closed_issues = len(issues[issues["Status"] == "Closed"])
critical_issues = len(issues[issues["Priority"] == "Critical"])

# Risk Analysis
if critical_issues > 40 or open_issues > 80:
    risk = "HIGH"
elif critical_issues > 20 or open_issues > 40:
    risk = "MEDIUM"
else:
    risk = "LOW"

# Print Report
print("===== Issue Tracking Agent =====")
print(f"Total Issues: {total_issues}")
print(f"Open Issues: {open_issues}")
print(f"Closed Issues: {closed_issues}")
print(f"Critical Issues: {critical_issues}")
print(f"Risk Level: {risk}")