def main ():

    amount_left = 50
    while amount_left > 0:
        print(f"Amount Due: {amount_left}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount_left -= coin

    print(f"Change Owed: {-amount_left}")

if __name__ == "__main__":
    main()
