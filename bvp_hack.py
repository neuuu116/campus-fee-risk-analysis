import mysql.connector

# 1️⃣ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASS",   # <-- put your MySQL password
    database="new_db"    # <-- database where students table exists
)

cursor = conn.cursor(dictionary=True)

# 2️⃣ Fetch student data
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

def evaluate_student(student):
    pending_fee = student["total_fee"] - student["fee_paid"]

    if pending_fee == 0:
        risk = "No Risk"
        plan = "No plan needed"
    elif pending_fee < 30000:
        risk = "Low Risk"
        plan = "Only kind reminder needed"
    elif pending_fee < 80000:
        risk = "Medium Risk"
        plan = "2-installment payment plan"
    else:
        risk = "High Risk"
        plan = "3-installment plan + admin review"

    return pending_fee, risk, plan
 
for student in students:
    pending, risk, plan = evaluate_student(student)

    print("Student ID   :", student["id"])
    print("Student Name :", student["name"])
    print("Pending Fee  :", pending)
    print("Risk Level   :", risk)
    print("Suggested Plan:", plan)
    print("-" * 40)

cursor.close()
conn.close()
