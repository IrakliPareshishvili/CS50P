digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    length = len(s)
    if (not s.isalnum()) or s.isdigit() or length > 6 or length < 2:
        return False
    for i in range (10):
        if s[0] == digits[i] or s[1] == digits[i]:
            return False
    number_position = 0
    for j in range (2, length):
        check = False
        for i in range (10):
            if s[j] == digits[i]:
                check = True
                if number_position == 0:
                    if s[j] == "0":
                        return False
                    number_position = j
        if number_position > 0  and not check:
            return False
    return True

if __name__ == "__main__":
    main()




