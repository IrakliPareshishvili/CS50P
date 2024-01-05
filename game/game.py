from random import randint


def main():
    random_number = get_level()
    guess_number(random_number)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                random_number = randint(1,level)
                return random_number
        except ValueError:
            pass


def guess_number(random_number):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < random_number:
                    print("Too Small!")
                elif guess > random_number:
                    print("Too Large!")
                else:
                    print("Just Right!")
                    return
        except ValueError:
            pass

if __name__ == "__main__":
    main()
