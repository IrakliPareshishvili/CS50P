def main():
    greeting = input("Please type greeting: ")
    target_value = value(greeting)
    print(f"${target_value}")



def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()


