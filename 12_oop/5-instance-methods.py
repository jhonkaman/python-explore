# Instance Methods

# Run: python3 12_oop/5-instance-methods.py

# Instance methods are functions defined inside a class that operate on instance data using the self keyword.

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says: Woof!")

    def introduce(self):
        print(f"My name is {self.name}")

dog1 = Dog("Buddy")
dog1.bark()
dog1.introduce()
