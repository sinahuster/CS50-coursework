greeting = str(input("Greeting: "))

dollars = 0

for word in greeting:
    if word == 'hello':
        break
    else:
        for char in word:
            if char == 'h':
                dollars = 20
                break
            else:
                dollars = 100
                break
print()
