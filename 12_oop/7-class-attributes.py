# Class Attributes

# Run: python3 12_oop/7-class-attributes.py

# Class attributes are shared by all instances of a class and are defined directly in the class body.

class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(f"Both are {Dog.species}")
print(f"dog1.species: {dog1.species}")
print(f"dog2.species: {dog2.species}")
