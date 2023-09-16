txt = input("camelCase: ").strip()
print("snakecase: ", end="")
for c in txt:
    if c.isupper():
        print("_", c.lower(), sep="", end="")
    else:
        print(c, end="")
print()