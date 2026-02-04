# Inhertance ---> parent-child relationship
# A ---> super class; B ---> sub class of A; C ---> sub class of B
class A:
    def feature1(self):
        print("Feature 1")
    
    def feature2(self):
        print("Feature 2")

class B: 
    def feature3(self):
        print("Feature 3")
    
    def feature4(self):
        print("Feature 4")

class C(A, B): # C inherits properties/methods of A & B both
    def feature5(self):
        print("Feature 5")
    
    def feature6(self):
        print("Feature 6")

a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature5()
c1.feature6()
c1.feature1() # method of A
c1.feature2() # method of A
c1.feature3() # method of B
c1.feature4() # method of B
