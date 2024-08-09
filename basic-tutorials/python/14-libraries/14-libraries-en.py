### Libraries ###

# Libraries in Python are collections of modules and functions that provide additional functionalities.
# These functionalities go beyond the predefined functions in the standard library.
# To use a library, you must first import it into your code.

# Importing an entire library #

import math

# We import the entire "math" library, which provides advanced mathematical functions.

# Importing specific functions #

from math import sqrt, radians

# We import the "sqrt" and "radians" functions directly from the "math" library.
# This allows us to use these functions without needing to write "math." before each call.

# Importing with an alias #

from math import ceil as round_up  

# We import the "ceil" function from the "math" library and assign it the alias "round_up".
# Now we can call the function using "round_up" instead of "ceil".

# Using library functions #

# Example 1: Calculate the square root of a number
number = 25
square_root = math.sqrt(number)
print("The square root of", number, "is:", square_root)

# Example 2: Calculate the sine of an angle in radians
angle_radians = math.radians(30)
sine = math.sin(angle_radians)
print("The sine of", angle_radians, "radians is:", sine)

# Example 3: Round a number up
decimal_number = 4.7
rounded_up_number = round_up(decimal_number)
print("The number", decimal_number, "rounded up is:", rounded_up_number)

# List of most famous libraries #

# - math: Provides advanced mathematical functions.
# - os: Provides functions for interacting with the operating system.
# - datetime: Provides classes for working with dates and times.
# - random: Provides functions for generating random numbers.
# - requests: Used for making HTTP requests.
# - numpy: Provides data structures and functions for numerical operations.
# - pandas: Provides data structures and tools for data analysis.
# - matplotlib: Used for creating graphical visualizations.
# - tensorflow: Machine learning and neural network library.
# - tkinter: Used for creating graphical user interfaces (GUIs).

# Libraries can greatly expand Python's capabilities and simplify the development of more complex applications.

# Marc Delgado Ferreres