# Run: python3 conditionals/elif.py
# Elif Statement Examples
# The elif (else if) statement handles multiple conditions

# Simple if-elif-else
score = 78
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

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
