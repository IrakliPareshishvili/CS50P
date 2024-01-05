import emoji

def main():
    user_input = input("Type your text: ")
    print(convert(user_input))

def convert(x):
    return emoji.emojize(x, language="alias")


if __name__ == "__main__":
    main()
