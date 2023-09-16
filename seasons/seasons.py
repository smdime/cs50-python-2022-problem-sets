from datetime import date
import inflect
import sys

def main():
    bdate = get_bdate()
    age_in_mins = calc_age(bdate)
    age_in_words = convert(age_in_mins)
    print(age_in_words)

def get_bdate():
    while True:
        try:
            input_bdate = input("Date of Birth: ")
            user_bdate = date.fromisoformat(input_bdate)
            return user_bdate
        except ValueError:
            sys.exit("Invalid date")

def calc_age(bdate):
    today = date.today()
    age_in_days = (today - bdate).days
    age_in_mins = age_in_days * 24 * 60
    return age_in_mins

def convert(age_in_mins):
    p = inflect.engine()
    age_in_words = p.number_to_words(age_in_mins, andword='')
    return f"{age_in_words.capitalize()} minutes"

if __name__ == "__main__":
    main()
