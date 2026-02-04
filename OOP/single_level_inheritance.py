# Inhertance ---> parent-child relationship
# Types - single-level, multi-level, multiple
# A ---> super class; B ---> sub class
class A:
    def feature1(self):
        print("Feature 1")
    
    def feature2(self):
        print("Feature 2")

class B(A): # B inherits properties/methods of A
    def feature3(self):
        print("Feature 3")
    
    def feature4(self):
        print("Feature 4")

a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()
b1.feature1() # method of A
b1.feature2() # method of A