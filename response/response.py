import validators

def main():
    email = input("What's your email address? ").strip().lower()
    valid = validate(email)

    if valid:
        print("Valid")
    else:
        print("Invalid")

def validate(email):
    return validators.email(email)

if __name__ == "__main__":
    main()
