# Run: python3 functions/return_values.py
# Return Values Examples
# Functions can return data to the caller

# Function that returns a simple value
def get_age():
    return 25

age = get_age()
print(f"Age: {age}")
print()

# Function that returns a string
def get_greeting():
    return "Hello, Python!"

message = get_greeting()
print(message)
print()

# Function that returns the result of a calculation
def multiply(a, b):
    result = a * b
    return result

product = multiply(4, 5)
print(f"4 × 5 = {product}")
print()
