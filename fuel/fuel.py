while True:
    try:
        x,y = input("Fraction: ").split("/")
        z = round(int(x)/int(y)*100)
        if 100 >= z >=99:
            print("F")
        elif z <= 1:
            print("E")
        elif z > 100:
            continue
        else:
            print(f"{z}%")
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
