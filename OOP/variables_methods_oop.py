# Types of variables - class variables, instance variables
# Static variables and class variables are same
# Types of methods - class methods, instance methods, static methods
# Type of instance methods - accessor methods, mutator methods
# only fetch the values ---> use accessor (getter); changing values ---> use mutator (setter)

class Car:
    wheels = 4 # class variable

    def __init__(self):
        # instance variales - different for each object
        self.brand = "Porsche"
        self.price = "10Cr"
        self.mileage = 100

    def display(self):
        print("Brand: {}, Mileage: {}, Wheels {}, Price {}".format(self.brand, self.mileage, self.wheels, self.price))

c1 = Car()
c2 = Car()
c3 = Car()
c4 = Car()

c1.mileage = 50
c2.price = "12Cr"
c2.wheels = 8
Car.wheels = 10 # chanes for all objects as variable is shared

c1.display()
c2.display()
c3.display()
c4.display()

class Student:
    school = "XYZ"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): # instance method - since passing self
        return (self.m1 + self.m2 + self.m3) / 3
    
    def get_m1(self):
        return self.m1
    
    def set_m1(self, value):
        self.m1 = value

    # to work with class variable, use class as parameter in method
    @classmethod # decorator
    def get_school_name(cls):
        return cls.school
    
    @staticmethod # decorator
    def info(): # static method
        print("This is student class...")


s1 = Student(34, 67, 32)
s2 = Student(89, 59, 22)

print(s1.avg())
print(s2.avg())

print(s1.m1)
print(Student.get_school_name()) # won't work if @classmethod not specified unless passed the parameter

Student.info()