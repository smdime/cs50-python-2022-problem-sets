import random

def main():
    n = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(n)
        problem = f"{x} + {y} = "
        z = x + y
        tries = 0
        while tries < 3:
            answer = input(problem)
            try:
                answer = int(answer)
                if answer == z:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{x} + {y} = {z}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                raise ValueError
            return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y

if __name__ == "__main__":
    main()