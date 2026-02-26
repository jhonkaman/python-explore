# For Loop Examples

# Run: python3 06_loops/1_for.py

# The for loop iterates over a sequence of items

# For loop with range
for i in range(5):
    print(i)
print()

# For loop with range starting and ending
for i in range(1, 6):
    print(i)
print()

# For loop with range and step
for i in range(0, 10, 2):
    print(i)
print()

# For loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print()

# For loop with string
word = "Python"
for letter in word:
    print(letter)
print()

# For loop with index
colors = ["red", "green", "blue"]
for index in range(len(colors)):
    print(f"{index}: {colors[index]}")
print()

# For loop with enumerate
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Index {index}: {name}")
print()

# For loop with multiplication table
number = 5
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")
print()

# Nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()
