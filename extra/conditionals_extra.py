# IF

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



# ELSE
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



# ELIF
# Grade range with multiple elif
grade = 85
if grade >= 90 and grade <= 100:
    print("Excellent!")
elif grade >= 80 and grade < 90:
    print("Good job!")
elif grade >= 70 and grade < 80:
    print("Average, but you passed")
elif grade >= 60 and grade < 70:
    print("Passing grade")
else:
    print("You failed")

# Day of week example
day = 3  # 1-7 representing Mon-Sun
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Weekend!")

# Traffic light example
color = "yellow"
if color == "red":
    print("Stop!")
elif color == "yellow":
    print("Slow down")
elif color == "green":
    print("Go!")
else:
    print("Invalid color")

# Season based on month
month = 7  # July
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
else:
    print("Fall")
