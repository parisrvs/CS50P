import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")


try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Something went wrong. Try after some time...")

r = r.json()
rate = float(r["bpi"]["USD"]["rate_float"])
amount = rate*n
print(f"${amount:,.4f}")