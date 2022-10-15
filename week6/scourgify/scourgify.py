import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


filename_before = sys.argv[1]
filename_after = sys.argv[2]
if not filename_before.endswith(".csv") or not filename_after.endswith(".csv"):
    sys.exit("Not a CSV file")


data = []
try:
    file = open(filename_before)
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    reader = csv.DictReader(file)
    for row in reader:
        name, house = row["name"], row["house"]
        last_name, first_name = name.split(',')
        last_name = last_name.strip()
        first_name = first_name.strip()
        data.append({
            "first": first_name,
            "last": last_name,
            "house": house
        })
    file.close()

with open(filename_after, "w") as csvfile:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for line in data:
        writer.writerow(line)