import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_list = re.findall(r'(^um|\Wum\W|\bum\b)', string=s, flags=re.IGNORECASE)
    return len(um_list)


if __name__ == "__main__":
    main()
