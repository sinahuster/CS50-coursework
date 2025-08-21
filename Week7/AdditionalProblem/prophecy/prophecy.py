from cs50 import SQL

# Open database
db = SQL("sqlite:///new_roster.db")

# Create table
db.execute("CREATE TABLE students(id INTEGER, name TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE houses(id INTEGER, house TEXT, house_head TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE house_assignements(student_id INTEGER, house_id INTEGER, FORGEIN KEY(student_id) REFERENCES student(id), FORGEIN KEY(house_id) REFERENCES houses(id))")

# Check table contents
print(db.execute("SELECT * FROM students"))
print(db.execute("SELECT * FROM houses"))
print(db.execute("SELECT * FROM house_assignments"))
