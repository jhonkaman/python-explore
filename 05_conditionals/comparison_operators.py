# Comparison Operators Examples

# Run: python3 05_conditionals/comparison_operators.py

# Comparison operators compare two values and return True or False

# Equal to (==)
x = 5
y = 5
print("5 == 5:", x == y)  # True

# Not equal to (!=)
x = 5
y = 3
print("5 != 3:", x != y)  # True

# Greater than (>)
x = 10
y = 3
print("10 > 3:", x > y)  # True

# Less than (<)
x = 3
y = 10
print("3 < 10:", x < y)  # True

# Greater than or equal to (>=)
x = 10
y = 10
print("10 >= 10:", x >= y)  # True

# Less than or equal to (<=)
x = 5
y = 10
print("5 <= 10:", x <= y)  # True

# Comparing strings
name1 = "Alice"
name2 = "Bob"
print("'Alice' == 'Alice':", name1 == name1)  # True
print("'Alice' == 'Bob':", name1 == name2)    # False

# Comparing multiple conditions
age = 25
print("Is age between 18 and 65?:", 18 <= age <= 65)  # True

# Comparing different types
num = 5
string = "5"
print("5 == '5':", num == string)  # False (different types)
print("5 == 5.0:", 5 == 5.0)       # True (numeric comparison)
