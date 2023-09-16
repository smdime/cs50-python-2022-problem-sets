def main():
    greeting = input("Greeting: ").strip().lower()
    result = value(greeting)
    print(f"${result}")

def value(greeting):
    if greeting.startswith("hello"):
        return 100
    elif greeting.startswith("h"):
        return 20
    else:
        return 0

if __name__ == "__main__":
    main()