import sqlite3

conn = sqlite3.connect("school_database.db")
cursor = conn.cursor()

# Query to get only teachers
query = '''
SELECT StaffID, FirstName, LastName, Role, Department, DateOfHire, ContactNumber, Email
FROM TeachersAndStaff
WHERE Role = 'Teacher'
'''

cursor.execute(query)
teachers = cursor.fetchall()

print("📋 List of Teachers:")
for teacher in teachers:
    print(teacher)

conn.close()
