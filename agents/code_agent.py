import pandas as pd

# Load commit dataset
commits = pd.read_csv("data/commits.csv")

# Calculate metrics
total_commits = commits["Commits"].sum()
average_commits = commits["Commits"].mean()
total_lines_added = commits["Lines_Added"].sum()
total_lines_deleted = commits["Lines_Deleted"].sum()
average_files_changed = commits["Files_Changed"].mean()

# Simple Risk Analysis
if average_commits < 3:
    risk = "HIGH"
elif average_commits < 6:
    risk = "MEDIUM"
else:
    risk = "LOW"

# Print Report
print("===== Code Quality Agent =====")
print(f"Total Commits: {total_commits}")
print(f"Average Commits: {average_commits:.2f}")
print(f"Lines Added: {total_lines_added}")
print(f"Lines Deleted: {total_lines_deleted}")
print(f"Average Files Changed: {average_files_changed:.2f}")
print(f"Risk Level: {risk}")