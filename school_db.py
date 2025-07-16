import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("school_database.db")
cursor = conn.cursor()

# -----------------------
# Create Students Table
# -----------------------
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender TEXT CHECK(Gender IN ('Male', 'Female', 'Other')),
    Address TEXT,
    ContactNumber TEXT,
    Email TEXT UNIQUE
)
''')
print("✅ Students table created.")
conn.commit()

# -------------------------------
# Create AcademicRecords Table
# -------------------------------
cursor.execute('''
CREATE TABLE IF NOT EXISTS AcademicRecords (
    RecordID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER NOT NULL,
    Subject TEXT NOT NULL,
    Grade TEXT CHECK(Grade IN ('A', 'B', 'C', 'D', 'E', 'F')),
    AcademicYear TEXT NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
)
''')
print("✅ AcademicRecords table created.")
conn.commit()

# --------------------------------
# Create TeachersAndStaff Table
# --------------------------------
cursor.execute('''
CREATE TABLE IF NOT EXISTS TeachersAndStaff (
    StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Role TEXT NOT NULL,
    Department TEXT,
    DateOfHire DATE NOT NULL,
    ContactNumber TEXT,
    Email TEXT UNIQUE
)
''')
print("✅ TeachersAndStaff table created.")
conn.commit()

# --------------------------------------------
# Clear tables to avoid duplicate constraint issues
# --------------------------------------------
cursor.execute("DELETE FROM AcademicRecords")
cursor.execute("DELETE FROM Students")
cursor.execute("DELETE FROM TeachersAndStaff")
conn.commit()
print("🧹 Existing data cleared.")

# ----------------------------
# Insert Sample Student Data
# ----------------------------
students_data = [
    ('John', 'Doe', '2005-03-14', 'Male', '123 Maple Street', '0701000001', 'john.doe@example.com'),
    ('Mary', 'Smith', '2006-08-22', 'Female', '456 Pine Road', '0701000002', 'mary.smith@example.com'),
    ('David', 'Ochieng', '2004-12-10', 'Male', '789 Elm Avenue', '0701000003', 'david.ochieng@example.com'),
    ('Grace', 'Nabunya', '2007-06-05', 'Female', '321 Oak Street', '0701000004', 'grace.nabunya@example.com'),
    ('Alex', 'Mugisha', '2005-09-30', 'Other', '654 Cedar Lane', '0701000005', 'alex.mugisha@example.com')
]
cursor.executemany('''
INSERT OR IGNORE INTO Students (FirstName, LastName, DateOfBirth, Gender, Address, ContactNumber, Email)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', students_data)
print("✅ Sample student data inserted.")
conn.commit()

# -------------------------------
# Insert Sample Academic Records
# -------------------------------
academic_data = [
    (1, 'Mathematics', 'A', '2024'),
    (1, 'English', 'B', '2024'),
    (2, 'Science', 'A', '2024'),
    (2, 'Mathematics', 'C', '2024'),
    (3, 'English', 'B', '2023'),
    (3, 'Science', 'D', '2023'),
    (4, 'Mathematics', 'A', '2024'),
    (4, 'English', 'A', '2024'),
    (5, 'Science', 'B', '2024'),
    (5, 'English', 'C', '2024')
]
cursor.executemany('''
INSERT OR IGNORE INTO AcademicRecords (StudentID, Subject, Grade, AcademicYear)
VALUES (?, ?, ?, ?)
''', academic_data)
print("✅ Sample academic records inserted.")
conn.commit()

# -----------------------------------
# Insert Sample Teachers and Staff
# -----------------------------------
staff_data = [
    ('Samuel', 'Kato', 'Teacher', 'Mathematics', '2018-01-15', '0702000001', 'samuel.kato@example.com'),
    ('Linda', 'Namakula', 'Teacher', 'English', '2019-03-10', '0702000002', 'linda.namakula@example.com'),
    ('Peter', 'Wanyama', 'Admin', 'Admissions', '2017-07-22', '0702000003', 'peter.wanyama@example.com'),
    ('Sarah', 'Akello', 'Teacher', 'Science', '2020-05-05', '0702000004', 'sarah.akello@example.com'),
    ('James', 'Mugabe', 'Principal', 'Administration', '2015-11-30', '0702000005', 'james.mugabe@example.com')
]
cursor.executemany('''
INSERT OR IGNORE INTO TeachersAndStaff (FirstName, LastName, Role, Department, DateOfHire, ContactNumber, Email)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', staff_data)
print("✅ Sample teachers and staff data inserted.")
conn.commit()

# --------------------
# Close the connection
# --------------------
conn.close()
print("🎉 All tables created, data inserted, and connection closed successfully.")
