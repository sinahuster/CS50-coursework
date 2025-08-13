import string

# get the greeting input from the user
greeting = str(input("Greeting: ")).strip()

# determine the first word of the greeting and remove any attached punctuation
first_word = greeting.split()[0].strip(string.punctuation)

# check with coniditon applies and the dollars associated 
if first_word.lower() == 'hello':
    dollars = 0
elif first_word.lower().startswith('h'):
    dollars = 20
else:
    dollars = 100

print(f"${dollars}")
