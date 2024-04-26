"""
Answer to Q1:
super() is used to access constructor, instance methods, and class methods.
"""

# Answer to Q2.
# super() doesn't work for constructor [ _init_ ] in multiple inheritance. It only works with methods.

class Animal:
    def __init__(self, name: str, colour: str):
        self.name = name
        self.colour = colour

    def makesSound(self, sound):
        return f"{self.name} makes {sound} sound."

class HouseholdAnimal:
    def __init__(self, legs: int, weight: float, age: int):
        self.legs = legs
        self.weight = weight
        self.age = age

    def bornBaby(self, fact):
        return f"Does it bear baby? {fact.capitalize()}."

class Milking(Animal, HouseholdAnimal):
    def __init__(self, name, colour, legs: int, weight, age, origin: str):
        Animal.__init__(self, name, colour)
        HouseholdAnimal.__init__(self, legs, weight, age)
        self.origin = origin

    def makesSound(self, sound):
        return super().makesSound(sound)        # Method accessing with super()
    
class Goat(Animal, HouseholdAnimal):    # We can use singe inheritance Goat(Milking). Then in total it will be HYBRID inheritance .
    def __init__(self, name: str, colour: str, legs: int, weight: float, age: int, origin: str):
        Animal.__init__(self, name, colour)
        HouseholdAnimal.__init__(self, legs, weight, age)
        self.origin = origin

    def makesSound(self, sound):        # Overriding method of Animal() class.
        return f"{self.name} {sound}s frequently."



shindi = Milking("Lalu", "pattern", 4, 300, 6, "India")
print(shindi.makesSound("moo"))
print(shindi.bornBaby("yes"))
print(shindi.age)


chagol = Goat("Jomunapari", "Brown", 4, 100, 4, "Bangladesh")
print(chagol.makesSound("bleet"))
print(chagol.bornBaby("yes"))
print(chagol.weight)

