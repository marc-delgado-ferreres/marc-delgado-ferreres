### Control Structure ###

# What is its purpose #

# The "if" and "else" statements are used to make decisions based on a condition.
# They allow you to execute one block of code if the condition is true and another block of code if the condition is false.

# If #

# The "if" statement is used to execute a block of code if a condition is true.
# The block of code within the "if" statement is executed only if the condition is met. If the condition is not met, the "if" block is skipped.

if False == True:
    print("False == True is True")
if True == False:
    print("True == False is True")
if True == True:
    print("True == True is True")
if False == False:
    print("False == False is True")

# In this example, we can see four consecutive "if" statements.
# The first and second "if" statements are not met, so their respective blocks are not executed.
# The third "if" statement is met, so its block is executed, and "True == True is True" is printed.
# The fourth "if" statement is met, so its block is executed, and "False == False is True" is printed.

# Else #

# The "else" statement is used in conjunction with "if" to provide an alternative block of code that is executed when the "if" condition is not met.
# The block of code within the "else" statement is executed only if the "if" condition is not met.

if False == True:
    print("False == True is True")
if True == False:
    print("True == False is True")
else:
    print("Discard")

# In this example, we can see three statements, two "if" statements and one "else" statement.
# The first and second "if" statements are not met, so their respective blocks are not executed.
# The third "else" statement is executed by default, so its block is executed, and "Discard" is printed.

# Elif #

# The "elif" statement is short for "else if" and is used to check multiple conditions in sequence.
# It can be used after an "if" or another "elif" to provide additional blocks of code that are executed when certain conditions are met.
# Only the block of code corresponding to the first condition that is met will be executed.

if False == True:
    print("False == True is True")
elif True == False:
    print("True == False is True")
elif True == True:
    print("True == True is True")
elif False == False:
    print("False == False is True")

# In this example, we can see four statements: one "if" statement and three "elif" statements.
# The first "if" statement is not met, so its block is not executed.
# The second "elif" statement is not met, so its block is not executed.
# The third "elif" statement is met, so its block is executed, and "True == True is True" is printed.
# The fourth "elif" statement is not executed because a previous block has already been activated, and the remaining are "elif" statements.

# Marc Delgado Ferreres