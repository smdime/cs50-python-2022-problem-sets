from project import Dice,, roll_dice, get_sum

def test_Dice_str():
    dice = Dice(2, 6)
    assert str(dice) == "You got a 2 6-sided dice."

def test_roll_dice():
    rolls = roll_dice(2, 6)
    assert len(rolls) == 2
    assert all(1 <= roll <= 6 for roll in rolls)

def test_get_sum():
    rolls = [2, 3, 4]
    assert get_sum(rolls) == 9
