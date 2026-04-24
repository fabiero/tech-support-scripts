import csv
import re
from datetime import datetime

# Read users
active = []
inactive = []

with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["status"] == "active":
            active.append(row)
        else:
            inactive.append(row)

# Validate emails using regex
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

print("===== SUPPORT REPORT =====")
print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Total users:", len(active) + len(inactive))
print("Active:", len(active))
print("Inactive:", len(inactive))

print("\n===== EMAIL VALIDATION =====")
with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        valid = re.findall(email_pattern, row["email"])
        if valid:
            print(row["name"], "→ ✓ Valid email")
        else:
            print(row["name"], "→ ✗ Invalid email")

# Write report
with open("report.csv", "w", newline="") as f:
    fieldnames = ["id", "name", "email", "status"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(active + inactive)

print("\nReport saved to report.csv!")
