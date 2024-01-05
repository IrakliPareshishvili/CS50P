import requests
import sys

def main():
    if len(sys.argv) == 2:
        try:
            value = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()

    calculate_bitcoin_value(value, bitcoin_price)

def get_bitcoin_price():
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = r.json()
        bitcoin = response["bpi"]["USD"]["rate_float"]
        return bitcoin
    except requests.RequestException:
        print("RequestException")

def calculate_bitcoin_value(value, bitcoin_price):
    amount = bitcoin_price * value
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
