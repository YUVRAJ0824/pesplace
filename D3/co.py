class Dog:
    species = "Canis familiaris"
    

    def bark(self):
        return "woof"

dog1 =Dog()
dog2 = Dog()

print(dog1.species)
print(dog2.species)

print(dog1.bark())
print(dog2.bark())