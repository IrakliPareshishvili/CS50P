def main():
    x, y, z = input("Expression: ").strip().split(" ")
    print(calculation(x,y,z))


def calculation(x,y,z):
    if y == "+":
        return float(int(x) + int(z))
    if y == "-":
        return float(int(x) - int(z))
    if y == "*":
        return float(int(x) * int(z))
    if y == "/" and z !=0:
        return float(int(x) / int(z))


if __name__ == "__main__":
    main()
