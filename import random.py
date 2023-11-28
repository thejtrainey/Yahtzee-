import random

def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

def is_yahtzee(dice_values):
    return all(value == dice_values[0] for value in dice_values)

for _ in range(777):
    dice = roll_dice()
    
    if is_yahtzee(dice):
        print(f"You rolled {dice} and it's a Yahtzee!")
