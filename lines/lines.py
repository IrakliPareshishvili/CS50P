import sys

def main():
    command_line()
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File does not exist")

    counter = 0
    for line in lines:
        if check_line(line) == False:
            counter += 1

    print(counter)


def command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_line(line):
    if line.isspace():
        return True
    elif line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()



