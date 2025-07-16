import sqlite3

# Connect to the existing database
conn = sqlite3.connect("school_database.db")
cursor = conn.cursor()

# ------------------------
# Fetch and display students
# ------------------------
print("\n📘 STUDENTS")
cursor.execute("SELECT * FROM Students")
students = cursor.fetchall()
for student in students:
    print(student)

# --------------------------------
# Fetch and display academic records
# --------------------------------
print("\n📗 ACADEMIC RECORDS")
cursor.execute("SELECT * FROM AcademicRecords")
records = cursor.fetchall()
for record in records:
    print(record)

# ------------------------------
# Fetch and display teachers and staff
# ------------------------------
print("\n📙 TEACHERS AND STAFF")
cursor.execute("SELECT * FROM TeachersAndStaff")
staff = cursor.fetchall()
for member in staff:
    print(member)

# ---------------------
# Close connection
# ---------------------
conn.close()
print("\n✅ Query complete and connection closed.")
