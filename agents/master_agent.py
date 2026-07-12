# Master Agent

code_risk = "MEDIUM"
issue_risk = "HIGH"
schedule_risk = "LOW"
documentation_risk = "HIGH"
communication_risk = "MEDIUM"

risk_score = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3
}

total_score = (
    risk_score[code_risk]
    + risk_score[issue_risk]
    + risk_score[schedule_risk]
    + risk_score[documentation_risk]
    + risk_score[communication_risk]
)

average_score = total_score / 5

if average_score >= 2.5:
    overall_risk = "HIGH"
elif average_score >= 1.5:
    overall_risk = "MEDIUM"
else:
    overall_risk = "LOW"

print("========== SOFTWARE PROJECT RISK REPORT ==========")
print(f"Code Quality Agent       : {code_risk}")
print(f"Issue Tracking Agent     : {issue_risk}")
print(f"Schedule Agent           : {schedule_risk}")
print(f"Documentation Agent      : {documentation_risk}")
print(f"Communication Agent      : {communication_risk}")
print("------------------------------------------")
print(f"Overall Project Risk : {overall_risk}")