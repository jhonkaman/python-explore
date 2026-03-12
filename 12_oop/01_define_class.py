# Define a Class

# Run: python3 12_oop/1-define-class.py

# A class is a blueprint for creating objects that bundles data and functions together.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 5)
print(f"Dog name: {dog1.name}, age: {dog1.age}")
