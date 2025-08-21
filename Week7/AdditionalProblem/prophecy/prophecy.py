from cs50 import SQL

# Open database
db = SQL("sqlite:///roster.db")

# Create table
student = db.execute("CREATE TABLE students(id INTEGER, name TEXT, PRIMARY KEY(id))")
house = db.execute("CREATE TABLE houses(id INTEGER, name TEXT, PRIMARY KEY(id))")

