# Run: python3 loops/while.py
# While Loop Examples
# The while loop executes as long as a condition is true

# Simple while loop
count = 0
while count < 5:
    print(count)
    count += 1
print()

# While loop with user simulation
x = 10
while x > 0:
    print(f"Countdown: {x}")
    x -= 1
print("Blastoff!")
print()

# While loop with string
password = ""
while password != "secret":
    password = "secret"  # Simulating user input
    if password != "secret":
        print("Wrong password, try again")
    else:
        print("Access granted!")
print()

# While loop with list
numbers = [1, 2, 3, 4, 5]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1
print()

# While loop with sum
total = 0
number = 1
while number <= 10:
    total += number
    number += 1
print(f"Sum of 1 to 10: {total}")
print()

# While loop with condition
value = 100
while value > 10:
    print(value)
    value //= 2  # Divide by 2
print()

# While loop with multiple conditions
age = 0
while age >= 0 and age < 150:
    print(f"Age: {age}")
    age += 25
    if age >= 150:
        break
