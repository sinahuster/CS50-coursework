import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)
elif len(sys.argv) == 3 and (argv[1] == '-f' or argv[1] == '--font'):
    font = sys.argv[2]
else:
    print("Invalid usage")
    sys.exit(1)


text = str(input("Input: "))
f = figlet.setFonts(font=font)

print(f"Output: {figlet.renderText(text)}")
