# Run: python3 booleans/boolean_variables.py
# Boolean Variables Examples
# Booleans represent True or False values

# Creating boolean variables
is_student = True
is_raining = False
print(is_student)
print(is_raining)

# Boolean type
print(type(True))
print(type(False))

# Comparison operators return booleans
x = 10
y = 5
result1 = x > y      # True
result2 = x == y     # False
result3 = x != y     # True
print(result1)
print(result2)
print(result3)

# Boolean in conditionals
if is_student:
    print("This person is a student")

# Boolean operations
a = True
b = False
print(a and b)       # False
print(a or b)        # True
print(not a)         # False

# Truthiness in Python
value = 0
if not value:
    print("0 is considered False in a boolean context")

value = "Hello"
if value:
    print("Non-empty strings are considered True")
