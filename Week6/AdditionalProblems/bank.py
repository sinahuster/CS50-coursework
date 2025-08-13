greeting = str(input("Greeting: ")).strip()

first_word = greeting.split()[0]

if first_word.lower() == 'hello':
    dollars = 0
elif first_word.lower().startswith('h'):
    dollars = 20
else:
    dollars = 100

print(f"${dollars}")
