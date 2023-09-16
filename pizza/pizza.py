import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
elif len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            data = list(reader)
            table = tabulate(data, headers="keys", tablefmt="grid")
            print(table)
    except FileNotFoundError:
        sys.exit("File does not exist")