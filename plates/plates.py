def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6 < len(s) or len(s) < 2:
        return False
    if not s[0:2].isalpha():
        return False
    if not s.isalnum():
        return False
    n = 0
    while n < len(s):
        if s[n].isnumeric():
            if s[n] == "0":
                return False
            else:
                break
        n += 1
    for i in range(len(s) - 1):
        if s[i].isnumeric() and s[i+1].isalpha():
                    return False
    return True


main()