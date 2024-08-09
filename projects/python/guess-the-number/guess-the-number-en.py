# Import the randint function from the random module
from random import randint

# Define a function to print the welcome message
def welcome_message():
    print("Welcome to the Guess the Number game!\n")

# Define a function to generate a random number between 1 and 100
def generate_random_number():
    print("I'm thinking of a number between 1 and 100. Try to guess it!")
    return randint(1, 100)

# Define a function to print a congratulations message based on the number of attempts
def congratulations_message(number_of_attempts):
    if number_of_attempts == 1:
        print("\nCongratulations, you guessed the number in only one attempt!")
    else:
        print("\nCongratulations, you guessed the number in {} attempts!".format(number_of_attempts))

# Define a function to get the user's guess and handle input validation
def get_user_guess():
    while True:
        try:
            user_guess = int(input("\nEnter a number between 1 and 100: "))
            if 1 <= user_guess <= 100:
                return user_guess
            else:
                print("ERROR: You must enter a number between 1 and 100.")
        except ValueError:
            print("ERROR: You must enter a valid number.")

# Define the main game function
def start_game():
    welcome_message()  # Print the welcome message
    random_number = generate_random_number()  # Generate a random number
    number_of_attempts = 0  # Initialize the number of attempts counter
    while True:
        number_of_attempts += 1  # Increment the attempts counter
        user_guess = get_user_guess()  # Get the user's guess
        if user_guess == random_number:  # Check if the guess is correct
            congratulations_message(number_of_attempts)  # Print congratulations message
            break  # Exit the game loop
        elif user_guess < random_number:
            print("\nThe number you're looking for is greater.")
        else:
            print("\nThe number you're looking for is smaller.")
    print("\nThank you for playing Guess the Number!")

# Start the match
if __name__ == "__main__":
    start_game()  # Start the game

# Marc Delgado Ferreres