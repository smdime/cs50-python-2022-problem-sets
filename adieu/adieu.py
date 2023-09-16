import inflect

p = inflect.engine()
names = []

try:
    while True:
        name = input("Name: ").strip().title()
        names.append(name)
except EOFError:
    num_names = len(names)
    if num_names == 1:
        output = f"Adieu, adieu, to {names[0]}"
    elif num_names == 2:
        output = f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        output = f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"

print()
print(output)
