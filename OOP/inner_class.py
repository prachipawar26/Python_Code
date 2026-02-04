# inner class used when a class is only used for another class
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.laptop = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.laptop.show() # calling inner class method

    class Laptop:
        def __init__(self):
            self.brand = "Lenovo"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

    # object of inner class should be created inside __init__ of outer class


s1 = Student('Prachi_1', 9)
s2 = Student('Prachi_2', 3)

s1.show()
print(s1.laptop.brand) # to get variable of inner class

lap1 = s1.laptop
lap2 = s2.laptop

print(id(lap1))
print(id(lap2))

# creating object of inner class here
lap3 = Student.Laptop()