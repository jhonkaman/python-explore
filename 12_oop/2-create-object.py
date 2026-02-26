# Create (Instantiate) an Object

# Run: python3 12_oop/2-create-object.py

# Creating an object (instance) means calling the class like a function to make a copy of it.

class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(dog1.name)
print(dog2.name)
