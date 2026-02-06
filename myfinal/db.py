import sqlite3 as sqlite
import pandas as pd

# Step 1: Connect to SQLite database
conn = sqlite.connect('student.db')
print("Connected to DB:", conn)

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create the student table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL
    )
''')

# Step 4: Check if table is empty
cursor.execute("SELECT COUNT(*) FROM student")
result = cursor.fetchone()


# Step 5: Insert sample data (correct column names)
cursor.executemany("INSERT INTO student (Name, Email) VALUES (?, ?)", [
        ('Dipak Sharma', 'dipak@gmail.com'),
        ('Tejas Patil', 'tejas@gmail.com'),
        ('Ayushi', 'ayushi@gmail.com')
    ])
conn.commit()
print("Sample data inserted.")

# Step 6: Fetch and display data
cursor.execute("SELECT * FROM student")
data = cursor.fetchall()

print("\nStudent Records:")
print("-" * 40)
for student in data:
    print(f"ID: {student[0]}, Name: {student[1]}, Email: {student[2]}")

# Step 7: (Optional) Convert to DataFrame
df = pd.DataFrame(data, columns=['ID', 'Name', 'Email'])
print("\nData as Pandas DataFrame:")
print(df)

# Step 8: Close the connection
conn.close()
