from cs50 import SQL

db = SQL("sqlite:///favourites.db")

favourite = input("Favourite: ")

rows = db.execute("SELECT COUNT(*) AS n FROM favourties WHERE language = ?")
row = rows[0]

print(row["n"])
