# Run: python3 conditionals/else.py
# Else Statement Examples
# The else statement executes code if the if condition is false

# Simple if-else
age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If-else with numbers
number = 10
if number > 0:
    print("The number is positive")
else:
    print("The number is zero or negative")

# If-else with strings
password = "welcome123"
if password == "secret":
    print("Password is correct")
else:
    print("Password is incorrect")

# If-else with boolean
is_logged_in = False
if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in first")

# If-else with conditions
score = 65
if score >= 70:
    print("You passed the test")
else:
    print("You failed the test, try again")

# If-else with multiple variables
balance = 50
amount = 100
if balance >= amount:
    print("Transaction approved")
else:
    print("Insufficient funds")
