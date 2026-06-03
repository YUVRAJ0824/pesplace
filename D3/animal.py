class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def speak(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def speak(self):
        print(f"{self.name} says: Meow!")


if __name__ == "__main__":
    dog = Dog("bruno", "labrador")
    cat = Cat("kitty")

    dog.eat()
    dog.speak()
    cat.speak()    
    cat.eat()
