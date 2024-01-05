import random


def main():
    level = get_level()
    score = tries(level)
    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except ValueError:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def calculation(x,y):
    counter = 1
    while counter <=3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                counter += 1
                print("EEE")
        except ValueError:
            counter += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

def tries(level):
    counter = 1
    score = 0
    while counter <=10:
        x,y = generate_integer(level)
        result = calculation(x,y)
        if result == True:
            score += 1
        counter += 1
    return score


if __name__ == "__main__":
    main()


