### Tuples ###

# What is their purpose #

# Tuples in Python are data structures similar to lists, but they are immutable.
# This means that once a tuple is created, its elements cannot be modified.
# Tuples are used to store ordered collections of elements, just like lists,
# but they are useful for storing data that should not change.

# Tuple of numbers #

numbers = (1, 2, 3, 4, 5)
print(numbers)

# This will print:
# (1, 2, 3, 4, 5)

# Tuple of vowels #

vowels = ("a", "e", "i", "o", "u")
print(vowels)

# This will print:
# ("a", "e", "i", "o", "u")

# Tuple of different types of data #

different_data = ("apple", 240, True)
print(different_data)

# This will print:
# ("apple", 240, True)

# Empty tuple #

empty_tuple = ()
print(empty_tuple)

# This will print:
# ()

# Accessing tuple elements #

index_zero_numbers = numbers[0]
index_one_vowels = vowels[1]
index_two_different_data = different_data[2]
print(index_zero_numbers)
print(index_one_vowels)
print(index_two_different_data)

# Indexes are used to access an element within a tuple.
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

# Negative indexes are used to access an element from the end of the tuple.
# Index -1 corresponds to the last element, index -2 corresponds to the second-to-last element, etc.
# The values are assigned to the variables "index_one_negative_numbers", "index_two_negative_vowels", and "index_three_negative_different_data".
# This will print:
# 5
# o
# apple

# Dimensional tuples #

# It is possible to create a tuple whose elements are other tuples.
# This is known as a dimensional tuple.

# Creating a dimensional tuple #

dimensional_tuple = (("1", "2", "3", "4"), ("a", "b", "c", "d"), ("A", "B", "C", "D"))
print(dimensional_tuple)

# This will print:
# (("1", "2", "3", "4"), ("a", "b", "c", "d"), ("A", "B", "C", "D"))

# Accessing elements of the dimensional tuple #

index_one_index_one_dimensional_tuple = dimensional_tuple[0][0]
index_two_index_two_dimensional_tuple = dimensional_tuple[1][1]
index_three_index_three_dimensional_tuple = dimensional_tuple[2][2]
print(index_one_index_one_dimensional_tuple)
print(index_two_index_two_dimensional_tuple)
print(index_three_index_three_dimensional_tuple)

# Indexes are used to access an element within a tuple.
# To access a tuple within the tuple, you use one index.
# Then, to access an element within the selected tuple, you use another index.
# The values are assigned to the variables "index_one_index_one_dimensional_tuple", "index_two_index_two_dimensional_tuple", and "index_three_index_three_dimensional_tuple".
# This will print:
# 1
# b
# C

index_one_negative_index_one_negative_dimensional_tuple = dimensional_tuple[-1][-1]
index_two_negative_index_two_negative_dimensional_tuple = dimensional_tuple[-2][-2]
index_three_negative_index_three_negative_dimensional_tuple = dimensional_tuple[-3][-3]
print(index_one_negative_index_one_negative_dimensional_tuple)
print(index_two_negative_index_two_negative_dimensional_tuple)
print(index_three_negative_index_three_negative_dimensional_tuple)

# Negative indexes are used to access an element from the end of the tuple.
# Index -1 corresponds to the last element, index -2 corresponds to the second-to-last element, etc.
# The values are assigned to the variables "index_one_negative_index_one_negative_dimensional_tuple", "index_two_negative_index_two_negative_dimensional_tuple", and "index_three_negative_index_three_negative_dimensional_tuple".
# This will print:
# D
# c
# 2

# Marc Delgado Ferreres