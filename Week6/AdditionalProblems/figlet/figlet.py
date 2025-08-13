import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv[]) != 1 and len(sys.argv[]) != 3:
    print("Invalid usage")
    sys.exit(1)

