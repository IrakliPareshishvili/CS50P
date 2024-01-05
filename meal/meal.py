def main():
    input_time = input("Please input a time: ").strip()
    x = convert(input_time)
    print(meal_time(x))

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes)/60

def meal_time(x):
    if 7 <= x <= 8:
        return "breakfast time"
    elif 12 <= x <= 13:
        return "lunch time"
    elif 18 <= x <= 19:
        return "dinner time"
    else:
        return " "

if __name__ == "__main__":
    main()
