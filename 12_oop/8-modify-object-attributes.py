# Modify Object Attributes

# Run: python3 12_oop/8-modify-object-attributes.py

# You can change object attributes by assigning a new value to them after the object is created.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 5)
print(f"{dog1.name} is {dog1.age} years old")

dog1.name = "Charlie"
dog1.age = 6
print(f"{dog1.name} is {dog1.age} years old")
