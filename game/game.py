import random

def main():
    value = positive_int("Level: ")
    x = random.randint(1, value)
    while True:
        guess = positive_int("Guess: ")
        if guess < x:
            print("Too small!")
        elif guess > x:
            print("Too large!")
        else:
            print("Just right!")
            break

def positive_int(n):
    while True:
        try:
            value = int(input(n))
            if value <= 0:
                continue
            return value
        except ValueError:
            pass

if __name__ == "__main__":
    main()