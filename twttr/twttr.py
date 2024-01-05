def main():
    text = input("Input: ").strip()
    print(f"Output: {shorten(text)}")

def shorten(word):
    for _ in word:
        if _ in ["a","e","i","o","u","A","E","I","O","U"]:
            word = (word.replace(_, ""))
    return(word)

if __name__ == "__main__":
    main()
