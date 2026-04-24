import csv

active_users = []

with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["status"] == "active":
            active_users.append(row)

with open("active_users.csv", "w", newline="") as f:
    fieldnames = ["id", "name", "email", "status"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(active_users)

print("Active users saved to active_users.csv!")
print("Total active users:", len(active_users))
