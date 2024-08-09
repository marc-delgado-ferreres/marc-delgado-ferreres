### While Loop ###

# What is its purpose #

# The "while" loop is used to repeat a block of code as long as a condition is true.
# It allows you to execute the block of code repeatedly until the condition evaluates to "False".

# Example 1 #

counter = 0

while counter < 5:
    print("Counter:", counter)
    counter += 1

# In this example, the "while" loop is used to repeat a block of code as long as the variable "counter" is less than 5.
# First, the condition "counter < 5" is evaluated, and if it is "True", the block of code inside the "while" loop is executed.
# If the condition is met, the condition remains "True", and the loop repeats as long as this condition continues to be "True".
# If the condition is not met, the condition becomes "False" and the loop stops.
# As a result, the value of the counter is printed in each iteration, from 0 to 4:
# Counter: 0
# Counter: 1
# Counter: 2
# Counter: 3
# Counter: 4

# Example 2 #

first = 0
second = 1
print("Counter: {}".format(first))
print("Counter: {}".format(second))

while True:
    result = first + second
    print("Counter: {}".format(result))
    first = second
    second = result

# In this example, the "while" loop is used to repeat a block of code indefinitely, recreating the Fibonacci sequence.
# First, the condition "True" is evaluated, and the block of code inside the "while" loop is executed.
# If the condition is met, the condition remains "True", and the loop repeats as long as this condition continues to be "True".
# Since the condition is always "True", this block of code repeats indefinitely.
# As a result, the values of the variables "first" and "second" are printed first, followed by the sum of the last and second-to-last printed values, indefinitely:
# Counter: 0
# Counter: 1
# Counter: 1
# Counter: 2
# Counter: 3
# Counter: 5
# Counter: 8
# Counter: 13
# Counter: 21
# Counter: 34
# Counter: 55
# Counter: 89
# Counter: 144
# Counter: 233
# Counter: 377
# Counter: 610
# Counter: 987
# Counter: 1597
# Counter: 2584
# ...

# Be cautious with creating infinite loops, as they can cause problems if the code is not properly controlled.

# Marc Delgado Ferreres