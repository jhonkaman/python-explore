# Run: python3 loops/continue.py
# Continue Statement Examples
# The continue statement skips the current iteration and goes to the next

# Continue in for loop
for i in range(5):
    if i == 2:
        print("Skipping i = 2")
        continue
    print(i)
print()

# Continue to skip even numbers
for num in range(10):
    if num % 2 == 0:
        continue
    print(f"{num} is odd")
print()

# Continue in while loop
count = 0
while count < 5:
    count += 1
    if count == 3:
        print("Skipping count = 3")
        continue
    print(f"Count: {count}")
print()

# Continue to skip negative numbers
numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        print(f"Skipping negative: {num}")
        continue
    print(f"Processing: {num}")
print()

# Continue to skip specific items
fruits = ["apple", "banana", "cherry", "blueberry"]
for fruit in fruits:
    if fruit == "banana":
        print("Skipping banana (allergic)")
        continue
    print(f"Eating {fruit}")
print()

# Continue with length check
words = ["hi", "hello", "h", "goodbye", "see", "you"]
for word in words:
    if len(word) < 3:
        print(f"'{word}' is too short, skipping")
        continue
    print(f"'{word}' is acceptable")
print()

# Continue in nested loop
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            print(f"Skipping j=2 in iteration i={i}")
            continue
        print(f"i={i}, j={j}")
