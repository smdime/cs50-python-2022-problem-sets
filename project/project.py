import random
import sys

class Dice:
    def __init__(self, dice, sides):
        self.dice = dice
        self.sides = sides

    def __str__(self):
        return f"You chose a {self.dice} {self.sides}-sided dice."

def main():
    print("Welcome to the Dice Roller!\n")
    while True:
        input("Need help deciding, what's your question: ")
        dice = get_dice()
        sides = get_sides()
        roll = roll_dice(dice, sides)
        total = get_sum(roll)
        print(Dice(dice, sides))
        print(f"You got a total of {total}. ", end="")
        if total > sides:
            yes = [
                    "It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes."
            ]
            print(random.choice(yes))
        else:
            no = [
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."
            ]
            print(random.choice(no))

        play_again = input("Roll again? ").lower()
        if play_again == "yes" or play_again == "y":
            continue
        else:
            break


def get_dice():
    while True:
        try:
            dice = int(input("Enter your preferred number of dice: "))
            if dice <= 0:
                raise ValueError("Invalid input. Must be a number > 0.")
            else:
                return dice
        except ValueError:
            sys.exit("Invalid input. Must be a number > 0.")

def get_sides():
    while True:
        try:
            sides = int(input("Enter your preferred number of sides: "))
            if sides <= 0:
                raise ValueError("Invalid input. Must be a number > 0.")
            else:
                return sides
        except ValueError:
            sys.exit("Invalid input. Must be a number > 0.")

def roll_dice(dice, sides):
    return [random.randint(1, sides) for _ in range(dice)]

def get_sum(rolls):
    return sum(rolls)

if __name__ == "__main__":
    main()
