### Operators ###

# What is their function? #

# Operators are special symbols used to perform operations on variables and values.
# They allow for mathematical calculations, comparisons, and data manipulations.

# Arithmetic Operators #

# Arithmetic operations are basic mathematical operations used to perform numerical calculations.

# Addition #

addition = 75 + 25
print(addition)

# The "+" operator is used to add.
# The result is stored in the variable "addition".
# As a result, the value of "addition" will be:
# 100

addition += 100
print(addition)

# The "+=" operator is used to add a value to a variable.
# The result is stored in the variable "addition".
# As a result, the value of "addition" will be:
# 200

# Subtraction #

subtraction = 125 - 25
print(subtraction)

# The "-" operator is used to subtract.
# The result is stored in the variable "subtraction".
# As a result, the value of "subtraction" will be:
# 100

subtraction -= 100
print(subtraction)

# The "-=" operator is used to subtract a value from a variable.
# The result is stored in the variable "subtraction".
# As a result, the value of "subtraction" will be:
# 0

# Multiplication #

multiplication = 4 * 25
print(multiplication)

# The "*" operator is used to multiply.
# The result is stored in the variable "multiplication".
# As a result, the value of "multiplication" will be:
# 100

multiplication *= 2
print(multiplication)

# The "*=" operator is used to multiply a variable by a value.
# The result is stored in the variable "multiplication".
# As a result, the value of "multiplication" will be:
# 200

# Division #

# When performing a division, the result will always be a floating-point number.

division = 2500 / 25
print(division)

# The "/" operator is used to divide.
# The result is stored in the variable "division".
# As a result, the value of "division" will be:
# 100.0

division /= 4
print(division)

# The "/=" operator is used to divide a variable by a value.
# The result is stored in the variable "division".
# As a result, the value of "division" will be:
# 25.0

# Integer Division #

# When performing integer division, the result returns only the integer part, discarding any decimal part.

integer_division = 200 // 12
print(integer_division)

# The "//" operator is used for integer division.
# The result is stored in the variable "integer_division".
# As a result, the value of "integer_division" will be:
# 16

integer_division //= 2
print(integer_division)

# The "//=" operator is used to perform integer division on a variable by a value.
# The result is stored in the variable "integer_division".
# As a result, the value of "integer_division" will be:
# 8

# Modulus #

modulus = 120 % 25
print(modulus)

# The "%" operator is used to obtain the remainder of a division.
# The result is stored in the variable "modulus".
# As a result, the value of "modulus" will be:
# 20

modulus %= 15
print(modulus)

# The "%=" operator is used to obtain the remainder of dividing a variable by a value.
# The result is stored in the variable "modulus".
# As a result, the value of "modulus" will be:
# 5

# Comparison Operators #

# Comparison operations are used to compare two values or variables and evaluate whether a certain condition is met.
# These operations return a boolean value indicating whether the condition is true or false.

# Equality #

# The "==" operator is used to compare if the values are equal.

equality = (100 == 25)
print(equality)

# The result is stored in the variable "equality".
# As a result, the value of "equality" will be "False".

equality = (100 == 100)
print(equality)

# The result is stored in the variable "equality".
# As a result, the value of "equality" will be "True".

# Greater Than or Less Than #

# The ">" operator is used to compare if the first value is greater than the second.

greater_than_less_than = (10 > 25)
print(greater_than_less_than)

# The result is stored in the variable "greater_than_less_than".
# As a result, the value of "greater_than_less_than" will be False.

greater_than_less_than = (25 > 10)
print(greater_than_less_than)

# The result is stored in the variable "greater_than_less_than".
# As a result, the value of "greater_than_less_than" will be True.

# The "<" operator is used to compare if the second value is greater than the first.

greater_than_less_than = (25 < 10)
print(greater_than_less_than)

# The result is stored in the variable "greater_than_less_than".
# As a result, the value of "greater_than_less_than" will be False.

greater_than_less_than = (10 < 25)
print(greater_than_less_than)

# The result is stored in the variable "greater_than_less_than".
# As a result, the value of "greater_than_less_than" will be True.

# Greater Than or Equal To or Less Than or Equal To #

# The ">=" operator is used to compare if the first value is greater than or equal to the second.

greater_than_or_equal_to_less_than_or_equal_to = (10 >= 25)
print(greater_than_or_equal_to_less_than_or_equal_to)

# The result is stored in the variable "greater_than_or_equal_to_less_than_or_equal_to".
# As a result, the value of "greater_than_or_equal_to_less_than_or_equal_to" will be False.

greater_than_or_equal_to_less_than_or_equal_to = (25 >= 10)
print(greater_than_or_equal_to_less_than_or_equal_to)

# The result is stored in the variable "greater_than_or_equal_to_less_than_or_equal_to".
# As a result, the value of "greater_than_or_equal_to_less_than_or_equal_to" will be True.

greater_than_or_equal_to_less_than_or_equal_to = (25 >= 25)
print(greater_than_or_equal_to_less_than_or_equal_to)

# The result is stored in the variable "greater_than_or_equal_to_less_than_or_equal_to".
# As a result, the value of "greater_than_or_equal_to_less_than_or_equal_to" will be True.

# The "<=" operator is used to compare if the second value is greater than or equal to the first.

greater_than_or_equal_to_less_than_or_equal_to = (25 <= 10)
print(greater_than_or_equal_to_less_than_or_equal_to)

# The result is stored in the variable "greater_than_or_equal_to_less_than_or_equal_to".
# As a result, the value of "greater_than_or_equal_to_less_than_or_equal_to" will be False.

greater_than_or_equal_to_less_than_or_equal_to = (10 <= 25)
print(greater_than_or_equal_to_less_than_or_equal_to)

# The result is stored in the variable "greater_than_or_equal_to_less_than_or_equal_to".
# As a result, the value of "greater_than_or_equal_to_less_than_or_equal_to" will be True.

greater_than_or_equal_to_less_than_or_equal_to = (25 <= 25)
print(greater_than_or_equal_to_less_than_or_equal_to)

# The result is stored in the variable "greater_than_or_equal_to_less_than_or_equal_to".
# As a result, the value of "greater_than_or_equal_to_less_than_or_equal_to" will be True.

# Not Equal To #

# The "!=" operator is used to compare if the values are different.

not_equal_to = (25 != 25)

# The result is stored in the variable "not_equal_to".
# As a result, the value of "not_equal_to" will be False.

not_equal_to = (25 != 10)

# The result is stored in the variable "not_equal_to".
# As a result, the value of "not_equal_to" will be True.

# Logical Operators #

# Logical operations are used to combine or modify logical expressions and evaluate complex conditions.

# Logical And #

# The "and" operator is used to evaluate if both expressions are true.

logical_and = False and False

# In this example, the expression "False and False" is evaluated.
# As a result, the variable "logical_and" will be False, since both expressions are not true.

logical_and = True and False

# In this example, the expression "True and False" is evaluated.
# As a result, the variable "logical_and" will be False, since both expressions are not true.

logical_and = True and True

# In this example, the expression "True and True" is evaluated.
# As a result, the variable "logical_and" will be True, since both expressions are true.

# Logical Or #

# The "or" operator is used to evaluate if at least one of the expressions is true.

logical_or = False or False

# In this example, the expression "False or False" is evaluated.
# As a result, the variable "logical_or" will be False, since none of the expressions is true.

logical_or = True or False

# In this example, the expression "True or False" is evaluated.
# As a result, the variable "logical_or" will be True, since at least one of the expressions is true.

logical_or = True or True

# In this example, the expression "True or True" is evaluated.
# As a result, the variable "logical_or" will be True, since at least one of the expressions is true.

# Logical Not #

# The "not" operator is used to negate the value of an expression.

logical_not = not True

# In this example, the expression "not True" is evaluated.
# As a result, the variable "logical_not" will be False, as it negates the true value "True".

logical_not = not False

# In this example, the expression "not False" is evaluated.
# As a result, the variable "logical_not" will be True, as it negates the false value "False".

# Marc Delgado Ferreres