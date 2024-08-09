### Lists ###

# What is their purpose #

# Lists in Python are data structures that allow you to store multiple elements in a single place. 
# Each element in a list has a position or index that starts from 0.
# Lists are useful for storing collections of related elements, such as numbers, strings, or other objects.

# List of numbers #

numbers = [1, 2, 3, 4, 5]
print(numbers)

# This will print:
# [1, 2, 3, 4, 5]

# List of vowels #

vowels = ["a", "e", "i", "o", "u"]
print(vowels)

# This will print:
# ["a", "e", "i", "o", "u"]

# List of different types of data #

different_data = ["apple", 240, True]
print(different_data)

# This will print:
# ["apple", 240, True]

# Empty list #

empty_list = []
print(empty_list)  

# This will print:
# []

# Accessing list elements #

index_zero_numbers = numbers[0]
index_one_vowels = vowels[1]
index_two_different_data = different_data[2]
print(index_zero_numbers)
print(index_one_vowels)
print(index_two_different_data)

# Indexes are used to access an element within a list.
# Index 0 corresponds to the first element, index 1 corresponds to the second element, etc.
# The values are assigned to the variables "index_zero_numbers", "index_one_vowels", and "index_two_different_data".
# This will print:
# 1
# e
# True

index_one_negative_numbers = numbers[-1]
index_two_negative_vowels = vowels[-2]
index_three_negative_different_data = different_data[-3]
print(index_one_negative_numbers)
print(index_two_negative_vowels)
print(index_three_negative_different_data)

# Negative indexes are used to access elements from the end of the list.
# Index -1 corresponds to the last element, index -2 corresponds to the second-to-last element, etc.
# The values are assigned to the variables "index_one_negative_numbers", "index_two_negative_vowels", and "index_three_negative_different_data".
# This will print:
# 5
# o
# apple

# Modifying list elements #

numbers[2] = 10
print(numbers)

# The element at index 2 of the "numbers" list is modified and assigned the value 10.
# This will print:
# [1, 2, 10, 4, 5]

# Getting the length of the list #

length = len(numbers)
print(length)

# The "len()" function is used to get the number of elements in the "numbers" list.
# The length value is assigned to the variable "length".
# This will print:
# 5

# Creating a list from a range #

range_list = list(range(0, 21, 2))
print(range_list)

# Generates a list of even numbers from 0 to 20 using the "range()" function
# Then converts it to a list with "list()".
# This will print:
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Slicing #

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alphabet)

# You can access a range of elements in a list using slicing notation.
# This helps you select a specific part of a list by creating a new one.

alphabet_a_j = alphabet[0:11]
print(alphabet_a_j)

# Gets a list of elements from index 0, which contains "a", to index 11, which represents "k".
# The last element is never included in the new list.
# This will print:
# ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

alphabet_q_x = alphabet[-10:-2]
print(alphabet_q_x)

# Gets a list of elements from index -10, which contains "q", to index -2, which represents "y".
# The last element is never included in the new list.
# This will print:
# ["q", "r", "s", "t", "u", "v", "w", "x"]

alphabet_reverse = alphabet[::-1]
print(alphabet_reverse)

# Gets a list with the elements of the original list sorted in reverse order.
# This will print:
# ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]

# Functions for lists #

# To work efficiently with lists, there are various functions dedicated to them.
# These functions allow you to perform actions such as adding, removing, sorting, and accessing elements in a list. 
# These functions make it easier to manipulate lists and perform common operations.

# Creating a test list #

test_list = ["a", "b", "a", "c", "c", "e", "e"]
print(test_list)

# Function "append()" #

# Add an element to the end of the list.

test_list.append("f")
print(test_list)

# Adds "f" to the end of the list.
# This will print:
# ["a", "b", "a", "c", "c", "e", "e", "f"]

# Function "insert()" #

# Insert an element at a specific position.

test_list.insert(5, "d")  
print(test_list)  

# Inserts the element "d" at index 5.
# This will print:
# ["a", "b", "a", "c", "c", "d", "e", "e", "f"]

# Function "remove()" #

# Remove the first occurrence of an element with a specific value.

test_list.remove("e")  
print(test_list)  

# Removes the first occurrence of "e".
# This will print:
# ["a", "b", "a", "c", "c", "d", "e", "f"]

# Function "pop()" #

# Removes and returns the element at a specific index. 
# If no index is provided, it removes the last element.

removed_value = test_list.pop(4)  
print(removed_value)
print(test_list)

# Removes the element at index 4 and stores its value.
# This will print:
# c
# ["a", "b", "a", "c", "d", "e", "f"]

removed_value = test_list.pop()  
print(removed_value)
print(test_list)

# Removes the last element and stores its value.
# This will print:
# f
# ["a", "b", "a", "c", "d", "e"]

# Function "index()" #

# Find the index of the first occurrence of an element with a specific value.

index = test_list.index("a")  
print(index)  

# Gets the first index of the element "a".
# This will print:
# 0

# Function "count()" #

# Count the number of times an element appears in the list.

count = test_list.count("a")  
print(count)  

# Counts how many times the element "a" appears.
# This will print:
# 2

# Function "sort()" #

# Sort the list in ascending order.

test_list.sort()  
print(test_list)  

# This will print:
# ["a", "a", "b", "c", "d", "e"]

# Sort the list in descending order.

test_list.sort(reverse=True)  
print(test_list)  

# This will print:
# ["e", "d", "c", "b", "a", "a"]

# Function "copy()" #

# Create a copy of the list.

copied_list = test_list.copy()  
print(copied_list)  

# This will print:
# ["e", "d", "c", "b", "a", "a"]

# Function "clear()" #

# Empty the list.

test_list.clear()  
print(test_list)  

# This will print:
# []

# Function "extend()" #

# Extend a list with the elements of another list.

test_list.extend([1, 2, 3])  
print(test_list)  

# This will print:
# [1, 2, 3]

test_list.extend([4, 5, 6])  
print(test_list)  

# This will print:
# [1, 2, 3, 4, 5, 6]

# Dimensional lists #

# It is possible to create a list whose elements are other lists.
# This is known as a dimensional list.

# Creating a dimensional list #

dimensional_list = [["1", "2", "3", "4"], ["a", "b", "c", "d"], ["A", "B", "C", "D"]]
print(dimensional_list)

# This will print:
# [["1", "2", "3", "4"], ["a", "b", "c", "d"], ["A", "B", "C", "D"]]

# Accessing elements of the dimensional list #

index_one_index_one_dimensional_list = dimensional_list[0][0]
index_two_index_two_dimensional_list = dimensional_list[1][1]
index_three_index_three_dimensional_list = dimensional_list[2][2]
print(index_one_index_one_dimensional_list)
print(index_two_index_two_dimensional_list)
print(index_three_index_three_dimensional_list)

# Indexes are used to access an element within a list.
# To access a list within the list, you use one index.
# Then, to access an element within the selected list, you use another index.
# The values are assigned to the variables "index_one_index_one_dimensional_list", "index_two_index_two_dimensional_list", and "index_three_index_three_dimensional_list".
# This will print:
# 1
# b
# C

index_one_negative_index_one_negative_dimensional_list = dimensional_list[-1][-1]
index_two_negative_index_two_negative_dimensional_list = dimensional_list[-2][-2]
index_three_negative_index_three_negative_dimensional_list = dimensional_list[-3][-3]
print(index_one_negative_index_one_negative_dimensional_list)
print(index_two_negative_index_two_negative_dimensional_list)
print(index_three_negative_index_three_negative_dimensional_list)

# Negative indexes are used to access elements from the end of the list.
# Index -1 corresponds to the last element, index -2 corresponds to the second-to-last element, etc.
# The values are assigned to the variables "index_one_negative_index_one_negative_dimensional_list", "index_two_negative_index_two_negative_dimensional_list", and "index_three_negative_index_three_negative_dimensional_list".
# This will print:
# D
# c
# 2

# Modifying elements of the dimensional list #

dimensional_list[1][-1] = "hello"
print(dimensional_list)

# The element at index -1 of the list at index 1 of the "dimensional_list" is modified and assigned the value "hello".
# This will print:
# [["1", "2", "3", "4"], ["a", "b", "c", "hello"], ["A", "B", "C", "D"]]

# Marc Delgado Ferreres