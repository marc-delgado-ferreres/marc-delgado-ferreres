# Import the ascii_letters, digits and punctuation functions from the string module
from string import ascii_letters, digits, punctuation

# Import the choice function from the random module
from random import choice

# This function allows the user to configure password options (letters, numbers, symbols).
def password_settings():
    letters = False
    numbers = False
    symbols = False
    while True:
        print("Password Options:\n")
        print("1. [{}] Letters (Aa)".format("Yes" if letters else "No"))
        print("2. [{}] Digits (123)".format("Yes" if numbers else "No"))
        print("3. [{}] Symbols (@&$!#?)".format("Yes" if symbols else "No"))
        print("4. Continue...")
        try:
            option = int(input("\nSelect an option (1/2/3/4): "))

            if option == 1:
                letters = not letters
            elif option == 2:
                numbers = not numbers
            elif option == 3:
                symbols = not symbols
            elif option == 4:
                break
            else:
                print("ERROR: You must select a valid option (1/2/3/4).\n")
        except ValueError:
            print("ERROR: You must select a valid option (1/2/3/4).\n")
    return letters, numbers, symbols

# This function allows the user to configure the desired password length.
def length_settings():
    while True:
        try:
            length = int(input("\nPassword length (4-100): "))
            if 4 <= length <= 100:
                return length
            else:
                print("ERROR: Length must be in the range of 4 to 100 characters.")
        except ValueError:
            print("ERROR: You must enter a valid integer for the length.\n")

# This function generates a password based on the options selected by the user.
def generate_password(letters, numbers, symbols, length):
    password_chars = ""
    if letters:
        password_chars += ascii_letters
    if numbers:
        password_chars += digits
    if symbols:
        password_chars += punctuation
    if not password_chars:
        print("ERROR: You must select at least one character type (letters, numbers, or symbols) to generate the password.\n")
        return
    password = ''.join(choice(password_chars) for _ in range(length))
    print("\nGenerated Password: {}".format(password))

# This function starts the main program.
def start_program():
    print("Password Generator\n")
    letters, numbers, symbols = password_settings()
    length = length_settings()
    generate_password(letters, numbers, symbols, length)

# Start the program
if __name__ == "__main__":
    start_program()

# Marc Delgado Ferreres