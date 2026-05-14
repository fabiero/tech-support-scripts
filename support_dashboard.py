import sqlite3
import csv
import logging
from datetime import datetime

logging.basicConfig(filename="dashboard.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def connect_db():
    try:
        conn = sqlite3.connect("support.db")
        logging.info("Connected to database")
        return conn
    except Exception as e:
        logging.error("Connection failed: " + str(e))
        return None

def show_summary(conn):
    print("\n===== SUPPORT SUMMARY =====")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*) as total,
            SUM(CASE WHEN status='open' THEN 1 ELSE 0 END) as open_tickets,
            SUM(CASE WHEN status='resolved' THEN 1 ELSE 0 END) as resolved,
            SUM(CASE WHEN priority='high' THEN 1 ELSE 0 END) as high_priority
        FROM tickets
    """)
    row = cursor.fetchone()
    print("Total Tickets:     ", row[0])
    print("Open Tickets:      ", row[1])
    print("Resolved Tickets:  ", row[2])
    print("High Priority:     ", row[3])

def show_user_report(conn):
    print("\n===== USER TICKET REPORT =====")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.name, u.city,
               COUNT(t.id) as total,
               SUM(CASE WHEN t.status='open' THEN 1 ELSE 0 END) as open_tickets,
               SUM(CASE WHEN t.priority='high' THEN 1 ELSE 0 END) as high_priority
        FROM users u
        LEFT JOIN tickets t ON u.id = t.user_id
        GROUP BY u.name
        ORDER BY open_tickets DESC
    """)
    rows = cursor.fetchall()
    print(f"{'Name':<10} {'City':<10} {'Total':<8} {'Open':<8} {'High':<8}")
    print("-" * 45)
    for row in rows:
        print(f"{row[0]:<10} {row[1]:<10} {row[2]:<8} {row[3]:<8} {row[4]:<8}")

def show_category_report(conn):
    print("\n===== CATEGORY REPORT =====")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.name, c.response_time,
               COUNT(t.id) as total,
               SUM(CASE WHEN t.status='open' THEN 1 ELSE 0 END) as open_tickets
        FROM categories c
        LEFT JOIN tickets t ON c.id = t.category_id
        GROUP BY c.name
        ORDER BY open_tickets DESC
    """)
    rows = cursor.fetchall()
    print(f"{'Category':<12} {'Response':<12} {'Total':<8} {'Open':<8}")
    print("-" * 42)
    for row in rows:
        print(f"{row[0]:<12} {row[1]:<12} {row[2]:<8} {row[3]:<8}")

def export_open_tickets(conn):
    print("\n===== EXPORTING OPEN TICKETS =====")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.name, u.email, t.issue, t.priority, c.name as category
        FROM tickets t
        JOIN users u ON t.user_id = u.id
        LEFT JOIN categories c ON t.category_id = c.id
        WHERE t.status = 'open'
        ORDER BY t.priority
    """)
    rows = cursor.fetchall()
    with open("open_tickets.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "email", "issue", "priority", "category"])
        writer.writerows(rows)
    print("Exported", len(rows), "open tickets to open_tickets.csv!")
    logging.info("Exported " + str(len(rows)) + " open tickets")

def main():
    print("========================================")
    print("   TECH SUPPORT DASHBOARD")
    print("   Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("========================================")
    conn = connect_db()
    if not conn:
        print("ERROR: Could not connect to database!")
        return
    try:
        show_summary(conn)
        show_user_report(conn)
        show_category_report(conn)
        export_open_tickets(conn)
        print("\n===== DASHBOARD COMPLETE =====")
        logging.info("Dashboard completed successfully")
    except Exception as e:
        print("ERROR:", str(e))
        logging.error("Dashboard error: " + str(e))
    finally:
        conn.close()
        logging.info("Database connection closed")

main()
