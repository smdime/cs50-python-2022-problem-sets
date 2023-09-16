import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
elif len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
    try:
        with open(sys.argv[1]) as file:
            number_of_lines = 0
            for lines in file:
                lines = lines.lstrip()
                if not lines.startswith("#") and lines != "":
                    number_of_lines += 1
        print(number_of_lines)
    except FileNotFoundError:
        sys.exit("File does not exist")