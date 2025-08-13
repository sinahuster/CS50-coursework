import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

# check the command line arguements and therefore determine the font
if len(sys.argv) == 1:
    font = random.choice(fonts)
elif len(sys.argv) == 3 and (argv[1] == '-f' or argv[1] == '--font'):
    font = sys.argv[2]
else:
    print("Invalid usage")
    sys.exit(1)

#set the font
f = figlet.setFont(font=font)

# ask for the text
text = str(input("Input: "))

# print the text in the new font 
print(f"Output: {figlet.renderText(text)}")
