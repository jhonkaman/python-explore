# The self Keyword

# Run: python3 12_oop/6-self-keyword.py

# The self keyword refers to the specific instance of the class and allows access to its attributes and methods.

class Dog:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"This dog's name is {self.name}"

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(dog1.info())
print(dog2.info())
