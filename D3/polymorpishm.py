class Duck:
    def sound(self):
        print("Quack quack")

# polymorphism
class Person:
    def sound(self):
        print("Hello!")

        
def make_sound(obj):
    obj.sound()

make_sound(Duck())
make_sound(Person())

print(len("hello"))
print(len([1, 2, 3]))
print(3 + 5)
print("A" + "B")
