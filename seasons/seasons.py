from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birth_date)
    except:
        sys.exit("Invalid date")

    date_of_birth = date(int(year), int(month), int(day))
    current_date = date.today()
    sub = current_date - date_of_birth
    minutes = sub.days * 24 * 60
    result = p.number_to_words(minutes, andword="")
    print(result.capitalize() + " minutes")



def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day



if __name__ == "__main__":
    main()
