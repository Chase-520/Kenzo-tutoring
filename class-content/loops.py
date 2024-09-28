# ==========================
# Class Content: Loops in Python
# ==========================

# 1. Introduction to Loops
# Loops are used to repeat a block of code multiple times.
# Two main types of loops in Python: `for` loop and `while` loop.

# ==========================
# 2. The `for` Loop
# ==========================

# A `for` loop is used to iterate over a sequence (list, tuple, string, or range of numbers).

"""
list

what does it look like?
[something]
[item1,item2,item3]

what are items?
items can be anything
item can be an integer --> 1 or -556
item can also be boolean --> True, False
float and string can also be item --> 4.08 , "this is a string"

code:
lst = ["a","b","c"]

index:
Index is the order of the item inside the list
list     ["a","b","c","d","e"]
index      0 , 1 , 2 , 3 , 4


"""
# # code:
# lst = ["a","b","c","d","e"]
# print(lst[2:4])

"""
for loops
what it looks like

for -->key word
in  -->key word

for item in lst:
    print(item)
"""
# Example 1: Loop through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Example 2: Loop through a range of numbers
for i in range(3):
    print(i)  # prints numbers 0 to 4

# Looping through strings
for alphabet in "hello":
    print(alphabet)

# Nested `for` loop
for i in range(3):
    for j in range(2):
        print(i, j)

# ==========================
# Loop Control Statements
# ==========================

# `break`: Exits the loop completely.
for i in range(5):
    if i == 3:
        break
    print(i)

# `continue`: Skips the current iteration.
for i in range(5):
    if i == 3:
        continue
    print(i)

# `else` block: Runs when the loop finishes normally (no `break`).
for i in range(5):
    print(i)
else:
    print("Loop finished!")

# ==========================
# 3. The `while` Loop
# ==========================

# A `while` loop runs as long as a condition is `True`.
# Example 1: Basic `while` loop
count = 0
while count < 5:
    print(count)
    count += 1

# Example 2: Using a `while` loop with user input
# This loop will keep asking for input until 'quit' is typed.
user_input = ""
while user_input != "quit":
    user_input = input("Type 'quit' to stop: ")

# ==========================
# Loop Control Statements in `while` Loops
# ==========================

# `break`: Exits the loop completely.
while True:
    response = input("Type 'exit' to stop: ")
    if response == "exit":
        break

# `continue`: Skips to the next iteration.
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)

# `else` block: Runs when the loop finishes without `break`.
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop finished!")

# ==========================
# 4. Comparing `for` and `while` Loops
# ==========================

# Example: Infinite loop using `while` (WARNING: this will run forever)
# while True:
#     print("This will run forever!")

# ==========================
# 5. Practice Problems
# ==========================

# Problem 1: Print the numbers from 1 to 10 using a `for` loop.
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# Problem 2: Print the even numbers from 1 to 20 using a `while` loop.
print("\nEven numbers from 1 to 20:")
num = 2
while num <= 20:
    print(num)
    num += 2

# Problem 3: Ask the user to enter a number greater than 100.
print("\nEnter a number greater than 100:")
num = 0
while num <= 100:
    num = int(input("Enter a number greater than 100: "))
print(f"You entered: {num}")

# ==========================
# 6. Summary
# ==========================
# - `for` loops are used to iterate over sequences like lists, strings, ranges.
# - `while` loops repeat as long as a condition is true.
# - Loop control statements: `break`, `continue`, and `else`.
