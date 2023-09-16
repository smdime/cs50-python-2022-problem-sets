import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    bitcoin = get_bitcoin()
    amount = n * bitcoin
    print(f"${amount:,.4f}")

def get_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        return o["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit()

if __name__ == "__main__":
    main()