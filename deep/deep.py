def main():
    prompt = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if prompt == "42" or prompt == "forty-two" or prompt == "forty two":
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()
