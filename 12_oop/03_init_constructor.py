# The __init__ Constructor Method

# Run: python3 12_oop/3-init-constructor.py

# The __init__ method is called automatically when you create an object to initialize its attributes.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Dog {self.name} has been created!")

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)
