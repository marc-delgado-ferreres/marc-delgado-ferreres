### Functions ###

# What is their purpose #

# Functions in Python are reusable blocks of code that perform a specific task.
# They allow you to organize and modularize your code, avoiding repetition and improving readability.
# Functions are defined using the keyword "def", followed by the function name and its parameters.

# Defining a function #

def greet(name):
    print("Hello, {}!".format(name))

# Calling a function #

greet("Juan")
greet("Maria")

# The "greet" function is defined to take a parameter "name" and print a personalized greeting.
# Then the function is called twice with different names.
# This will print:
# Hello, Juan!
# Hello, Maria!

# Parameters and arguments #

def add(a, b):
    result = a + b
    return result

result_addition = add(5, 3)
print(result_addition)

# The "add" function is defined to take two parameters "a" and "b", sum the values, and return the result.
# Then the function is called with the arguments 5 and 3, and the result is printed.
# This will print:
# 8

# Default parameters #

def greet(name="User"):
    print("Hello, {}!".format(name))

greet()
greet("Juan")

# The "greet" function is defined with a default parameter "name" that is "User".
# Then the function is called twice, once with no arguments and once with the argument "Juan".
# This will print:
# Hello, User!
# Hello, Juan!

# Passing arguments by position and by name #

def introduce(name, age):
    print("My name is {} and I am {} years old.".format(name, age))

introduce("Juan", 30)
introduce(age=25, name="Maria")

# The "introduce" function is defined to take two parameters "name" and "age".
# Then the function is called twice, once with positional arguments and once with keyword arguments.
# This will print:
# My name is Juan and I am 30 years old.
# My name is Maria and I am 25 years old.

# Returning multiple values #

def divide(number1, number2):
    quotient = number1 // number2
    remainder = number1 % number2
    return quotient, remainder

quotient, remainder = divide(10, 3)
print("Quotient: {}, Remainder: {}".format(quotient, remainder))

# The "divide" function is defined to take two numbers and return the quotient and remainder of the division.
# Then the function is called with the numbers 10 and 3, and the values are unpacked into the variables "quotient" and "remainder".
# This will print:
# Quotient: 3, Remainder: 1

# Lambda functions #

double = lambda x: x * 2

result_double = double(4)
print(result_double)

# A lambda (anonymous) function is defined to multiply a number by 2.
# Then the function is called with the number 4 and the result is printed.
# This will print:
# 8

# Built-in functions #

# Python has numerous built-in functions in its standard library that can be used directly.

# List of built-in functions #

# There is a vast array of functions in the Python standard library.
# Some of the most commonly used functions are:

# - abs(): returns the absolute value of a number.
# - ascii(): returns an ASCII representation of an object with escapes.
# - bin(): converts an integer to its binary representation.
# - bool(): converts a value to a boolean value.
# - chr(): converts a Unicode value to its corresponding character.
# - float(): converts a value to a floating-point number.
# - format(): formats a string with values.
# - hex(): converts an integer to its hexadecimal representation.
# - input(): reads a line of input from the console.
# - int(): converts a value to an integer.
# - len(): returns the length of an object (string, list, tuple, etc.).
# - list(): creates a list from an iterable.
# - max(): returns the maximum value in an iterable.
# - min(): returns the minimum value in an iterable.
# - oct(): converts an integer to its octal representation.
# - open(): opens a file in various modes.
# - ord(): converts a character to its Unicode integer value.
# - print(): prints values to the console.
# - range(): generates a sequence of integers.
# - reversed(): returns a reversed iterator of an iterable.
# - round(): rounds a number to a specific number of decimal places.
# - slice(): creates a slice object for indexing sequences.
# - sorted(): sorts elements in an iterable.
# - str(): converts a value to a string.
# - sum(): calculates the sum of elements in an iterable.
# - tuple(): creates a tuple from an iterable.
# - type(): returns the type of an object.

# Marc Delgado Ferreres