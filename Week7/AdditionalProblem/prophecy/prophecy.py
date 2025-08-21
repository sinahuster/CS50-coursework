from cs50 import SQL

# This ensures the file exists
open("new_roster.db", "a").close()

# Open database
db = SQL("sqlite:///new_roster.db")

# Create table
db.execute("CREATE TABLE students(id INTEGER, name TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE houses(id INTEGER, house TEXT, house_head TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE house_assignments(student_id INTEGER, house_id INTEGER, FOREIGN KEY(student_id) REFERENCES students(id), FOREIGN KEY(house_id) REFERENCES houses(id))")

# Check table contents
print(db.execute("SELECT * FROM students"))
print(db.execute("SELECT * FROM houses"))
print(db.execute("SELECT * FROM house_assignments"))
