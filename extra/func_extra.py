# DEFINE

# Function that performs a task
def display_info():
    name = "Alice"
    age = 25
    print(f"Name: {name}")
    print(f"Age: {age}")

display_info()
print()

# Function with multiple statements
def welcome_user():
    print("Welcome to our application!")
    print("Please log in to continue")
    print("---")

welcome_user()
print()

# Function that uses variables
def calculate():
    x = 10
    y = 5
    result = x + y
    print(f"The sum is: {result}")

calculate()
print()

# Defining and calling multiple times
def say_hello():
    print("Hi there!")

say_hello()
say_hello()
say_hello()
print()

# Function with internal function calls
def outer_function():
    def inner_function():
        print("I'm inside the inner function")

    print("I'm in the outer function")
    inner_function()

outer_function()



# PARAMETERS
# Function with string parameter
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old")

introduce("Alice", 25)
introduce("Charlie", 30)
print()

# Function with default parameter
def greet_with_greeting(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_with_greeting("Alice")
greet_with_greeting("Bob", "Hi")
print()

# Function with multiple default parameters
def describe_car(brand="Unknown", year=2020, color="Unknown"):
    print(f"Car: {year} {brand} in {color}")

describe_car()
describe_car("Toyota")
describe_car("Honda", 2022)
describe_car("Ford", 2023, "Red")
print()

# Function with variable number of parameters (*args)
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"Sum: {total}")

sum_numbers(1, 2, 3)
sum_numbers(5, 10, 15, 20)
print()

# Function with keyword parameters
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")



# RETURN
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
