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

# Function that returns multiple values
def get_coordinates():
    x = 10
    y = 20
    return x, y

x_pos, y_pos = get_coordinates()
print(f"Coordinates: ({x_pos}, {y_pos})")
print()

# Function with conditional return
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

result = check_age(25)
print(result)
result = check_age(15)
print(result)
print()

# Function that returns a list
def get_favorite_fruits():
    fruits = ["apple", "banana", "cherry"]
    return fruits

my_fruits = get_favorite_fruits()
print(f"Favorite fruits: {my_fruits}")
print()

# Function that returns based on calculation
def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

sale_price = calculate_discount(100, 20)
print(f"Final price after 20% discount: ${sale_price}")
print()

# Early return
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

result = find_first_even([1, 3, 4, 5])
print(f"First even number: {result}")
