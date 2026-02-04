# Python supports Procedure, Functional and Object Oriented Programming

# Object Oriented Programming
# Everything is object in python
# Every object has attributes and behaviours
# Attribites are defined by variables and behaviours are defined by method (functions)

# Class & Object
# Class ---> a template or a blueprint or a design
# Object ---> instance of a class


class Computer:
    def __init__(self): # special method (similar to constructor)
        print("This is init") # printed everytime an object is created
    
    def config(self):
        print("This is i5, 16GB RAM, 1TB computer.")

# self ---> object passed into the method

com1 = Computer() # creating object of class computer
print(type(com1))
com1.config() # way to access the method of a class
Computer.config(com1) # other way to access the method of a class

com2 = Computer()
com2.config()

# int, str, and else are all objects in python

class Mobile:
    def __init__(self, cpu, ram): # special method (similar to constructor)
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print(f"Config: CPU = {self.cpu}, RAM = {self.ram}")

# self ---> object passed into the method

mob1 = Mobile('Snapdragon', 32) # passing values to method
mob2 = Mobile('Exynos', 16)
mob1.config()
mob2.config()
