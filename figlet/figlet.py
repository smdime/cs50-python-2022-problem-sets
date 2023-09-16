import sys
from pyfiglet import Figlet

arg = sys.argv[1:]

if len(arg) != 2:
    sys.exit("Invalid usage")
elif arg[0] == '-f' or arg[0] == '--font':
    f = arg[1]
    if f in Figlet().getFonts():
        s = input("Input: ").strip()
        figlet = Figlet(font=f)
        print("Output:\n", figlet.renderText(s), sep="")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")