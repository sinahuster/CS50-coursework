greeting = str(input("Greeting: "))

contains_hello = False
contains_h = False

for word in greeting:
    if word == 'hello':
        contains_hello = True 
    for character in word:
        if character is
