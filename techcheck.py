def check_disk(usage):
    if usage >= 90:
        return "CRITICAL"
    elif usage >= 70:
        return "WARNING"
    else:
        return "OK"

servers = ["Server1", "Server2", "Server3"]
usages = [95, 75, 45]

print("===== TECH SUPPORT SYSTEM CHECK =====")
for i in range(3):
    status = check_disk(usages[i])
    print(servers[i], "Disk:", usages[i], "%", status)
print("===== CHECK COMPLETE =====")
