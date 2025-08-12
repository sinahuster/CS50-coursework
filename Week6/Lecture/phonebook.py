#people = {
#   "Yullia": "+1-617-495-1000",
#    "David": "+1-617-495-1000",
#    "John": "+1-949-468-2750",
#}

#name = input("Name: ")

#if name in people:
#    print(f"Number: {people[name]}")
#else:
#    print("Not found")



# names = ["Yullia", "David", "John"]

# name = input("Name: ")

# if name in names:
#    print("Found")
# else:
#     print("Not found")


import csv

name = input("Name: ")
number = input("Number: ")

with open("phonebook.csv", "a") as file:

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})
