def main():
    camel_case = input("camelCase: ")
    print(f"snake_case: {check(camel_case)}")


def check(word):
    add_word = word.lower()
    snake_case = ""
    for _ in range (len(word)):
        if word[_] != add_word[_]:
            snake_case = snake_case + "_"
        snake_case = snake_case + add_word[_]
    return snake_case

if __name__ == "__main__":
    main()
