from cs50 import SQL

# Open database
db = SQL("sqlite:///roster.db")

# Create table
db.create_table(student) 
