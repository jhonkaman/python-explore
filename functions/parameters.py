# Run: python3 functions/parameters.py
# Parameters Examples
# Parameters allow functions to accept data

# Function with one parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
print()

# Function with multiple parameters
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(5, 3)
add(10, 20)
print()

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
