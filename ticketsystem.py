tickets = []

def add_ticket(user, issue, priority):
    ticket = {
        "id": len(tickets) + 1,
        "user": user.strip().capitalize(),
        "issue": issue.strip(),
        "priority": priority.upper(),
        "status": "Open"
    }
    tickets.append(ticket)
    print("Ticket", ticket["id"], "created for", ticket["user"])

def show_tickets():
    print("\n===== ALL TICKETS =====")
    for t in tickets:
        print("ID:", t["id"], "| User:", t["user"], "| Issue:", t["issue"], "| Priority:", t["priority"], "| Status:", t["status"])

def resolve_ticket(ticket_id):
    for t in tickets:
        if t["id"] == ticket_id:
            t["status"] = "Resolved"
            print("Ticket", ticket_id, "resolved!")
            return
    print("Ticket not found!")

def save_tickets():
    with open("tickets_log.txt", "w") as f:
        for t in tickets:
            f.write(str(t) + "\n")
    print("Tickets saved to tickets_log.txt!")

# Run the system
add_ticket("  frida  ", "Cannot login", "high")
add_ticket("john", "Slow computer", "medium")
add_ticket("mary", "Password reset", "low")
show_tickets()
resolve_ticket(1)
show_tickets()
save_tickets()
