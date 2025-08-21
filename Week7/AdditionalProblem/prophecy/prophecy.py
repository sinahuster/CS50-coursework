from cs50 import SQL

# Open database
db = SQL("sqlite:///roster.db")

# Create table
student = db.execute("CREATE TABLE student(id INTEGER, name TEXT)")
