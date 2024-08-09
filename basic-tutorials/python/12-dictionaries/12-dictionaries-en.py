### Dictionaries ###

# What is their purpose #

# Dictionaries in Python are data structures that allow you to store key-value pairs.
# Each element in a dictionary is stored with its corresponding key and associated value.
# Dictionaries are useful for representing information organized into key-value pairs.

# Dictionary of person information #

person = {
    "name": "Juan",
    "age": 30,
    "profession": "engineer"
}
print(person)

# This will print:
# {'name': 'Juan', 'age': 30, 'profession': 'engineer'}

# Accessing elements in the dictionary #

name_person = person["name"]
age_person = person["age"]
profession_person = person["profession"]
print(name_person)
print(age_person)
print(profession_person)

# Keys are used to access the corresponding values in the dictionary.
# The values are assigned to the variables "name_person", "age_person", and "profession_person".
# This will print:
# Juan
# 30
# engineer

# Modifying elements in the dictionary #

person["age"] = 31
print(person)

# The value associated with the key "age" in the "person" dictionary is modified.
# This will print:
# {'name': 'Juan', 'age': 31, 'profession': 'engineer'}

# Adding elements to the dictionary #

person["city"] = "Madrid"
print(person)

# A new key-value pair is added to the "person" dictionary.
# This will print:
# {'name': 'Juan', 'age': 31, 'profession': 'engineer', 'city': 'Madrid'}

# Removing elements from the dictionary #

del person["profession"]
print(person)

# The key-value pair associated with the key "profession" is removed from the "person" dictionary.
# This will print:
# {'name': 'Juan', 'age': 31, 'city': 'Madrid'}

# Functions in dictionaries #

# To work with dictionaries, there are various dedicated functions.
# These functions allow you to perform actions such as retrieving keys, values, and key-value pairs.

# Creating a copy of the dictionary #

person_copy = person.copy()
print(person_copy)

# A copy of the "person" dictionary is created.
# This will print:
# {'name': 'Juan', 'age': 31, 'city': 'Madrid'}

# Getting a list of all keys #

keys = person.keys()
print(keys)

# A list of all keys in the "person" dictionary is obtained.
# This will print:
# dict_keys(['name', 'age', 'city'])

# Getting a list of all values #

values = person.values()
print(values)

# A list of all values in the "person" dictionary is obtained.
# This will print:
# dict_values(['Juan', 31, 'Madrid'])

# Getting a list of all key-value pairs #

items = person.items()
print(items)

# A list of all key-value pairs in the "person" dictionary is obtained.
# This will print:
# dict_items([('name', 'Juan'), ('age', 31), ('city', 'Madrid')])

# Marc Delgado Ferreres