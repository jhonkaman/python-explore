# Run: python3 functions/define_function.py
# Define Function Examples
# Functions are reusable blocks of code

# Simple function with no parameters
def greet():
    print("Hello, World!")

greet()
print()

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
