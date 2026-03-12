# Instance Attributes

# Run: python3 12_oop/4-instance-attributes.py

# Instance attributes are variables that belong to individual objects and store data unique to each instance.

class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

dog1 = Dog("Buddy", 5, "brown")
dog2 = Dog("Max", 3, "white")
print(f"{dog1.name} is {dog1.color}")
print(f"{dog2.name} is {dog2.color}")
