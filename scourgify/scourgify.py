import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    try:
        with open(sys.argv[1]) as input_file:
            reader = csv.DictReader(input_file)
            with open(sys.argv[2],"w",newline="") as output_file:
                writer = csv.DictWriter(output_file, fieldnames=["first","last","house"])
                writer.writeheader()

                for row in reader:
                    last,first = row["name"].split(", ")
                    writer.writerow({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")