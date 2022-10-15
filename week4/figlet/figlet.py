from pyfiglet import Figlet
import sys

l = len(sys.argv)


if l == 1:
    string = input("String: ").strip()
    f = Figlet()
    print(f.renderText(string))
elif l == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in Figlet().getFonts():
    string = input("String: ").strip()
    f = Figlet(font=sys.argv[2])
    print(f.renderText(string))
else:
    sys.exit("Invalid Usage")



