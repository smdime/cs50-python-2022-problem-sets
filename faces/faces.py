def main():
    type = input()
    print(convert(type))

def convert(type):
    TypeA = type.replace(":)", "🙂")
    TypeB = TypeA.replace(":(", "🙁")
    return TypeB

main()

