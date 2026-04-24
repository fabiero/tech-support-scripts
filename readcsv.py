import csv

print("===== ALL USERS =====")
with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("ID:", row["id"], "| Name:", row["name"], "| Email:", row["email"], "| Status:", row["status"])

print("\n===== ACTIVE USERS ONLY =====")
with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["status"] == "active":
            print(row["name"], "-", row["email"])

print("\n===== INACTIVE USERS ONLY =====")
with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["status"] == "inactive":
            print(row["name"], "-", row["email"])
