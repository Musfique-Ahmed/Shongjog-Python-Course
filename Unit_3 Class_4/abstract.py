from abc import ABC, abstractmethod

class Animal(ABC):
    def legs(self):
        print("It has 4 Legs!")

    @abstractmethod #decoretor
    def make_sound(self):
        print("Shut UP")

class Cat(Animal):
    def make_sound(self):
        return "Meao Meao"
    
class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")
    

cat = Cat()
cat.legs()
print(cat.make_sound())

dog = Dog()
dog.legs()
print(dog.make_sound())
