import csv
import sys

def main():
    command_line()
    output = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                split_name = row["name"].split(",")
                output.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
