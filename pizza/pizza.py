import csv
import sys
from tabulate import tabulate


def main():
    command_line()
    try:
        with open(sys.argv[1], "r") as file:
            table = csv.DictReader(file)
            print(tabulate(table, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


def command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
