import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")


try:
    file = open(filename)
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    reader = csv.DictReader(file)
    print(tabulate(reader, headers="keys", tablefmt="grid"))
    file.close()