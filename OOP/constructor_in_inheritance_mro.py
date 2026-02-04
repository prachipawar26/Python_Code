# Constructor in Inheritance
class A:
    def __init__(self):
        print("Init Constructor of class A")

    def feature1(self):
        print("Feature 1")
    
    def feature2(self):
        print("Feature 2")

class B(A):
    def __init__(self): # __init__ of sub class is called first then __init__ of super class
        super().__init__() # to call __init__ of super class too
        print("Init Constructor of class B")

    def feature3(self):
        print("Feature 3")
    
    def feature4(self):
        print("Feature 4")

b1 = B() # constructor of class A will be called, when class B does not have its own __init__
# Sub class can access all features from super class but super class cannot access features of sub class

# Constructor in multiple inheritance - Method Resolution Order (MRO)
class C:
    def __init__(self):
        print("Init Constructor of class C")

    def feature1(self):
        print("Feature 5")
    
    def feature2(self):
        print("Feature 6")

class D:
    def __init__(self): 
        print("Init Constructor of class D")

    def feature3(self):
        print("Feature 7")
    
    def feature4(self):
        print("Feature 8")

class E(C, D):
    def __init__(self): 
        print("Init Constructor of class E")

    def feature9(self):
        print("Feature 9")
    
    def feature10(self):
        print("Feature 10")
        super().feature3() # to called method for super class

e1 = E()

# class inheriting two super classes, will first look for its own __init__
# features called will be from left to right in super classes