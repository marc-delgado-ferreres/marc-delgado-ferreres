# Import the randint function from the os modules
from random import randint

# Import the system function from the os modules
from os import system

# Displays a welcome message when the game starts
def welcome_message():
    print("Welcome to the Dice Game!")

# Allows the user to choose dice to play with.
def request_user_dice():
    dice_types = {1: "D6", 2: "D4", 3: "D8", 4: "D10", 5: "D12", 6: "D120"}
    user_dice = []
    while True:
        try:
            selected_dice = int(input('''\nDice Options:
1. [D6] Six-sided dice
2. [D4] Four-sided dice
3. [D8] Eight-sided dice
4. [D10] Ten-sided dice
5. [D12] Twelve-sided dice
6. [D120] One hundred and twenty-sided dice
7. Continue...

Choose the dice you want to add: '''))
            if 1 <= selected_dice <= 7:
                if selected_dice == 7:
                    if not user_dice:
                        system("cls")
                        print("ERROR: You must select at least one die.")
                        if len(user_dice) > 0:
                            display_user_dice(user_dice, dice_types)
                        continue
                    else:
                        break
                user_dice.append(selected_dice)
                user_dice.sort() # Order the dice from largest to smallest
                display_user_dice(user_dice, dice_types)
            else:
                system("cls")
                print("ERROR: You must enter a valid option.")
                if len(user_dice) > 0:
                    display_user_dice(user_dice, dice_types)
        except ValueError:
            system("cls")
            print("ERROR: You must enter an integer.")
            if len(user_dice) > 0:
                display_user_dice(user_dice, dice_types)

    roll_dice(user_dice, dice_types)

# Displays the list of dice selected by the user
def display_user_dice(user_dice, dice_types):
    system("cls")
    print("\nList of selected dice")
    for i, dice in enumerate(user_dice):
        print("{}. [{}]".format(i + 1, dice_types[dice]))

# Rolls the selected dice and displays the results
def roll_dice(user_dice, dice_types):
    system("cls")
    print("\nRolling the dice:")
    dice_results = []
    for dice in user_dice:
        faces = {1: 6, 2: 4, 3: 8, 4: 10, 5: 12, 6: 120}
        dice_result = randint(1, faces[dice])
        dice_results.append(dice_result)
    display_dice_results(user_dice, dice_results, dice_types)

# Displays the results of rolling the dice
def display_dice_results(user_dice, dice_results, dice_types):
    for i in range(len(user_dice)):
        dice = dice_types[user_dice[i]]
        result = dice_results[i]
        print("{}. [{}]: {}".format(i + 1, dice, result))

# Starts the dice game
def start_game():
    welcome_message()
    request_user_dice()

# Start the game
if __name__ == "__main__":
    start_game()

# Marc Delgado Ferreres