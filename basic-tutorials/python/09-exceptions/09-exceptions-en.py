### Exceptions ###

# What is its purpose #

# Exceptions, along with "try" and "except" statements, are used to handle errors and exceptional situations during the execution of a program.

# Try #

# The main function of the "try" block is to attempt to execute a block of code where an exception might occur. 
# The code that may generate an exception is placed within the try block.

# Except #

# The function of the "except" block is to capture and handle exceptions that occur within the try block. 
# If an exception occurs in the try block, the program will look for a corresponding except block that can handle that specific exception. 
# The except block contains the code that will be executed when the exception is caught.

# Example 1 #

try:
    first_number = 10
    second_number = 10
    result = first_number // second_number
    print("The result of integer division is: {}".format(result))
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except NameError:
    print("Error: Variable not defined")

# In this example, the "try" block is used to execute code that performs integer division between two numbers.
# Since there is no error, the "try" block works perfectly. The program prints: 
# The result of the division is: 1

# Example 2 #

try:
    first_number = 10
    second_number = 0
    result = first_number / second_number
    print("The result of integer division is: {}".format(result))
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except NameError:
    print("Error: Variable not defined")

# In this example, the "try" block is used to execute code that performs division between two numbers.
# Since there is a "ZeroDivisionError," the "try" block does not work. The program prints: 
# Error: Cannot divide by zero

# Example 3 #

try:
    first_number = number
    second_number = 10
    result = first_number / second_number
    print("The result of integer division is: {}".format(result))
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except NameError:
    print("Error: Variable not defined")

# In this example, the "try" block is used to execute code that performs division between two numbers.
# Since there is a "NameError," the "try" block does not work. The program prints: 
# Error: Variable not defined

# Marc Delgado Ferreres