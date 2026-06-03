class Shape:
    def __init__(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2
#a=pi*r^2
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h
#a=w*h   
#a=1/2(bh)

class triangle(Shape):
    def __init__(self, b, h):
        self.b, self.h = b, h

    def area(self):
        return 0.5 * self.b * self.h

shapes = [Circle(5), Rectangle(4, 6), triangle(4, 5)]
for s in shapes:
    print(f"area: {s.area()}")