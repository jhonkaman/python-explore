# Run: python3 operators/logical_operators.py
# Logical Operators Examples
# Logical operators combine conditional statements

# AND operator
x = 10
y = 5
result = (x > 5) and (y < 10)
print("(10 > 5) and (5 < 10):", result)  # True

result = (x > 15) and (y < 10)
print("(10 > 15) and (5 < 10):", result)  # False

# OR operator
x = 10
y = 5
result = (x > 15) or (y < 10)
print("(10 > 15) or (5 < 10):", result)  # True

result = (x > 15) or (y > 10)
print("(10 > 15) or (5 > 10):", result)  # False

# NOT operator
is_raining = True
result = not is_raining
print("not True:", result)  # False

is_sunny = False
result = not is_sunny
print("not False:", result)  # True

# Combining multiple logical operators
age = 25
has_license = True
result = (age >= 18) and (has_license)
print("Age >= 18 and has license:", result)  # True

income = 30000
is_employed = True
result = (income > 25000) or (is_employed)
print("Income > 25000 or is employed:", result)  # True

# Complex conditions
x = 10
y = 20
z = 15
result = (x < y) and (y > z) and (z > x)
print("(10 < 20) and (20 > 15) and (15 > 10):", result)  # True
