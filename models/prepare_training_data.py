import pandas as pd

# Load datasets
commits = pd.read_csv("data/commits.csv")
issues = pd.read_csv("data/issues.csv")
deadlines = pd.read_csv("data/deadlines.csv")
documentation = pd.read_csv("data/documentation.csv")
communication = pd.read_csv("data/communication.csv")

rows = 100
combined_data = []

for i in range(rows):
    commit = commits.iloc[i]

    issue = issues.iloc[i % len(issues)]
    deadline = deadlines.iloc[i % len(deadlines)]
    document = documentation.iloc[i % len(documentation)]
    message = communication.iloc[i % len(communication)]

    # Create a simple target label
    risk = "LOW"

    if issue["Priority"] == "Critical":
        risk = "HIGH"
    elif deadline["Status"] == "Delayed":
        risk = "MEDIUM"

    combined_data.append([
        commit["Commits"],
        commit["Lines_Added"],
        commit["Files_Changed"],
        issue["Bugs"],
        deadline["Days_Left"],
        document["Completion_Percentage"],
        message["Messages"],
        risk
    ])

training_data = pd.DataFrame(
    combined_data,
    columns=[
        "Commits",
        "Lines_Added",
        "Files_Changed",
        "Bugs",
        "Days_Left",
        "Documentation",
        "Messages",
        "Risk"
    ]
)

training_data.to_csv("models/training_dataset.csv", index=False)

print("Training dataset created successfully!")