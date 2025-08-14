import sys

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0.0

try:
    # Infinite loop until exited by user
    while True:
        item = input("Item: ").strip().title()

        # Check if the item is in the menu, if yes add to total, if not,
        # ignore and repeat
        if item in menu:
            total += float(menu[item])
            print(f"Total: ${total:.2f}")
        else:
            continue

# If user exits, print a new line
except EOFError:
    print("\n")
    sys.exit(0)


