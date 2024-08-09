### Input ###

# What is its function? #

# The "input()" function is used to receive information entered by the user from the console and then assign this information to variables.

# Example 1 #

# We can use "input()" to prompt the user to enter some information without doing anything with that information.

input("Please, do not touch anything: ")

# In this example, the "input()" function is used to ask the user to enter some information.
# The message "Please, do not touch anything: " is displayed on the console to prompt the user to enter some information.
# After the user enters the information and presses Enter, nothing happens since this information is not being assigned to any variable.
# As a result, the program will continue as if nothing happened.

# Example 2 #

# We can use "input()" to prompt the user to enter some information and store it in a variable.

user_name = input("Enter your name: ")
print("Hello,", user_name, "!")

# In this example, the "input()" function is used to ask the user to enter their name.
# The message "Enter your name: " is displayed on the console to prompt the user to enter their name.
# After the user enters their name and presses Enter, the entered value is assigned to the variable "user_name".
# Then, the "print()" function is used to display a message that includes the name entered by the user.
# As a result, it will print a message with the name provided by the user.

# Example 3 #

# We can use "input()" to prompt the user to enter some information and store it in a variable.
# We can see in this example that "int()" is used to force the variable to be of integer type.

age = int(input("Enter your age: "))

print("Your age is", age, "years")

# In this example, the "input()" function is used to ask the user to enter their age.
# The message "Enter your age: " is displayed on the console to prompt the user to enter their age.
# After the user enters their age and presses Enter, the entered value is converted to an integer using the "int()" function.
# The resulting integer value is assigned to the variable "age".
# Then, the "print()" function is used to display a message that includes the age entered by the user.
# As a result, it will print a message with the age provided by the user.

# Marc Delgado Ferreres