# Run: python3 loops/break.py
# Break Statement Examples
# The break statement exits a loop prematurely

# Break in for loop
for i in range(10):
    if i == 5:
        print("Breaking out at i = 5")
        break
    print(i)
print()

# Break when searching for an item
fruits = ["apple", "banana", "cherry", "date"]
search_fruit = "cherry"
for fruit in fruits:
    if fruit == search_fruit:
        print(f"Found {search_fruit}!")
        break
    print(f"Checking {fruit}...")
print()

# Break in while loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        print("Exiting while loop")
        break
print()

# Break when finding first even number
numbers = [3, 7, 2, 9, 4]
for num in numbers:
    if num % 2 == 0:
        print(f"Found first even number: {num}")
        break
    print(f"{num} is odd")
print()

# Break in nested loop
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            print(f"Breaking inner loop at i={i}, j={j}")
            break
        print(f"i={i}, j={j}")
    print(f"Finished inner loop for i={i}")
print()

# Break with user input simulation
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    attempts += 1
    password = "correct" if attempts == 2 else "wrong"
    if password == "correct":
        print("Password accepted!")
        break
    else:
        print(f"Wrong! Attempt {attempts}")
