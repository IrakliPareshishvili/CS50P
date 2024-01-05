def main():
    text = input("Input a text: ")
    print(convert(text))


def convert(text):
    result = text.replace(":)", "🙂").replace(":(", "🙁")
    return result


main()
