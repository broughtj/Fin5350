class Animal:
    def __init__(self, kind, message):
        self.kind = kind
        self.message = message
        
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print(f"The {self.kind} says: {self.message}")
        
class Cat(Animal):
    def speak(self):
        print(f"The {self.kind} says: {self.message}")
        

## main
theDog = Dog("Dog", "Woof")
theDog.speak()

theCat = Cat("Cat", "Meow")
theCat.speak()