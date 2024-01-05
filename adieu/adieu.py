import inflect
p = inflect.engine()


def main():
    names = []
    try:
        while True:
            name = input("Enter a name: ")
            names.append(name)
    except EOFError:
        adios(names)

def adios(names):
    output = p.join(names)
    print("Adieu, adieu, to " + output)

if __name__ == "__main__":
    main()
