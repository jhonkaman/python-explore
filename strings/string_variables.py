# Run: python3 strings/string_variables.py
# String Variables Examples
# Strings are sequences of characters enclosed in quotes

# Creating string variables with double quotes
name = "Alice"
print(name)

# Creating string variables with single quotes
message = 'Hello, Python!'
print(message)

# Multi-line strings using triple quotes
bio = """My name is Alice.
I am learning Python.
Strings are fun!"""
print(bio)

# Accessing characters in a string (indexing)
word = "Python"
print(word[0])  # First character: P
print(word[5])  # Last character: n
print(word[-1])  # Last character using negative index: n

# String length
text = "Hello"
print(len(text))  # Output: 5

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# String repetition
result = "Ha" * 3
print(result)  # Output: HaHaHa

# String methods
lowercase = "HELLO".lower()
uppercase = "hello".upper()
print(lowercase)
print(uppercase)
