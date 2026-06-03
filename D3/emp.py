class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_display(self):
        return self._salary
    
    def set_display(self, amount):
        if amount > 0:
            self._salary = amount
        else:
            print("Invalid salary ")

emp = Employee("yuvraj", 50000)
print(emp.name)
print(emp.get_display())
emp.set_display(60000)
emp.set_display(-100)