# Run: python3 conditionals/if.py
# If Statement Examples
# The if statement executes code only if a condition is true

# Simple if statement
age = 20
if age >= 18:
    print("You are an adult")

# If with variable
score = 85
if score >= 80:
    print("Great job! You passed with a high score")

# If with multiple conditions (AND)
temperature = 75
humidity = 60
if temperature > 70 and humidity < 80:
    print("The weather is nice")

# If with multiple conditions (OR)
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# If with NOT
is_raining = False
if not is_raining:
    print("It's not raining, go outside!")

# If with comparison
x = 15
if x % 2 == 0:
    print("The number is even")
else:
    if x % 2 == 1:
        print("The number is odd")

# Nested if
user_age = 25
has_license = True
if user_age >= 18:
    print("You are old enough to drive")
    if has_license:
        print("You can legally drive!")
    else:
        print("You need to get a license first")
