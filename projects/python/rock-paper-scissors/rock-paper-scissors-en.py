# Import the randint function from the random module
from random import choice

# Import the system function from the os module
from os import system

# Clear the console to improve visual presentation
def clear_console():
    system("cls")

# Return a random choice among "rock", "paper", and "scissors"
def get_random_choice():
    choices = ("rock", "paper", "scissors")
    return choice(choices)

# Compare player and computer choices to determine the result
def compare_choices(player_choice, random_choice):
    results = {
        ("rock", "scissors"): "player",
        ("paper", "rock"): "player",
        ("scissors", "paper"): "player"
    }
    return "draw" if player_choice == random_choice else results.get((player_choice, random_choice), "random")

# Display the menu of options for the player to choose from
def show_menu():
    print("Rock Paper Scissors:\n")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit\n")

# Get the option chosen by the player and return it
def get_player_option():
    choices = ("rock", "paper", "scissors")
    menu_option = input("Choose an option: ")
    while menu_option not in ("1", "2", "3", "4"):
        print("ERROR: Invalid option.")
        menu_option = input("\nChoose an option: ")
    if menu_option == "4":
        return None
    return choices[int(menu_option) - 1]

# Display the game result
def show_result(result):
    if result == "draw":
        print("\nIt's a draw!")
    elif result == "player":
        print("\nYou won!")
    else:
        print("\nYou lost!")

# Display a welcome message at the start of the game
def welcome_message():
    print("Welcome to the Rock Paper Scissors game!\n")

# Display a farewell message at the end of the game
def farewell_message():
    print("\nThank you for playing Rock Paper Scissors!")

# Main function that starts the game and controls its flow
def start_game():
    welcome_message()
    while True:
        show_menu()
        player_choice = get_player_option()
        if player_choice is None:
            break
        random_choice = get_random_choice()
        print("\n{} vs {}".format(player_choice.title(), random_choice.title()))
        result = compare_choices(player_choice, random_choice)
        show_result(result)
        input("\nPress Enter to continue...")
        clear_console()
    farewell_message()

# Start the game
if __name__ == "__main__":
    start_game()

# Marc Delgado Ferreres