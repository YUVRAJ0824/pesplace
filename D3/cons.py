class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def Intro(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
#obj
student1 = Student("yuv", 21, "A")
student2 = Student("raj", 22, "B")
student1.Intro()
student2.Intro()