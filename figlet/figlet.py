import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        user_input = input("Input: ")
        generated_font = choice(figlet.getFonts())
        figlet.setFont(font=generated_font)
        print(figlet.renderText(user_input))
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
        user_input = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(user_input))
    elif len(sys.argv) == 3 and (sys.argv[1] != "-f" or sys.argv[1] != "--font") and sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()




