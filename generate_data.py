import pandas as pd
import random
from datetime import datetime, timedelta

# Number of records
records = 1000

developers = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack", "Kevin", "Liam", "Mia", "Noah", "Olivia", "Peter", "Rachel", "Sam", "Sophia", "Tom"]

# Generate Commit Data
commit_data = []

start_date = datetime(2026, 1, 1)

for i in range(records):
    date = start_date + timedelta(days=random.randint(0, 60))

    commit_data.append([
        date.strftime("%Y-%m-%d"),
        random.choice(developers),
        random.randint(1, 10),
        random.randint(50, 500),
        random.randint(10, 150),
        random.randint(1, 15)
    ])

commits = pd.DataFrame(
    commit_data,
    columns=[
        "Date",
        "Developer",
        "Commits",
        "Lines_Added",
        "Lines_Deleted",
        "Files_Changed"
    ]
)

commits.to_csv("data/commits.csv", index=False)


print("Commit dataset created successfully!")
# Generate Issue Data

issue_data = []

priorities = ["Low", "Medium", "High", "Critical"]
statuses = ["Open", "Closed", "In Progress"]

for i in range(200):
    issue_data.append([
        f"ISS{i+1}",
        random.choice(priorities),
        random.choice(statuses),
        random.randint(1, 10),
        random.choice(developers)
    ])

issues = pd.DataFrame(
    issue_data,
    columns=[
        "Issue_ID",
        "Priority",
        "Status",
        "Bugs",
        "Assigned_To"
    ]
)

issues.to_csv("data/issues.csv", index=False)

print("Issue dataset created successfully!")
# Generate Deadline Data

deadline_data = []

tasks = [
    "Login Module",
    "Payment System",
    "Database Design",
    "API Development",
    "Testing",
    "UI Development",
    "Deployment"
]

for i in range(100):
    task = random.choice(tasks)
    days_left = random.randint(-10, 60)

    if days_left < 0:
        status = "Delayed"
    elif days_left < 10:
        status = "At Risk"
    else:
        status = "On Track"

    deadline_data.append([
        task,
        "2026-03-01",
        status,
        days_left
    ])

deadlines = pd.DataFrame(
    deadline_data,
    columns=[
        "Task",
        "Deadline",
        "Status",
        "Days_Left"
    ]
)

deadlines.to_csv("data/deadlines.csv", index=False)

print("Deadline dataset created successfully!")
# Generate Documentation Data

documentation_data = []

documents = [
    "README",
    "API Documentation",
    "User Manual",
    "Design Document",
    "Test Documentation"
]

for i in range(100):
    document = random.choice(documents)
    status = random.choice(["Complete", "Incomplete", "Missing"])
    last_updated = f"2026-0{random.randint(1,6)}-{random.randint(1,28)}"
    completion = random.randint(20, 100)

    documentation_data.append([
        document,
        status,
        last_updated,
        completion
    ])

documentation = pd.DataFrame(
    documentation_data,
    columns=[
        "Document",
        "Status",
        "Last_Updated",
        "Completion_Percentage"
    ]
)

documentation.to_csv("data/documentation.csv", index=False)

print("Documentation dataset created successfully!")
# Generate Communication Data

communication_data = []

sentiments = ["Positive", "Neutral", "Negative"]

for i in range(200):
    communication_data.append([
        f"2026-0{random.randint(1,6)}-{random.randint(1,28)}",
        random.choice(developers),
        random.randint(1,50),
        random.choice(sentiments)
    ])

communication = pd.DataFrame(
    communication_data,
    columns=[
        "Date",
        "Developer",
        "Messages",
        "Sentiment"
    ]
)

communication.to_csv("data/communication.csv", index=False)

print("Communication dataset created successfully!")