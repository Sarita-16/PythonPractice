class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return "Woof !"

class Cat(Animal):
    def speak(self):
        return "Meow !"

# Example
dog = Dog("Buddy")
cat = Cat("Mimo")
print(f"Dog : {dog.speak()}")
print(f"Cat : {cat.speak()}")