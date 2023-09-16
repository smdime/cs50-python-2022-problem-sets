x = 50
y = 0
while x > 0:
    print("Amount Due:", x)
    y = int(input("Insert Coin: ").strip())
    if y != 25 and y != 10 and y != 5:
        continue
    else:
        x = x - y
print("Change Owed:", abs(x))
