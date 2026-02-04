class Computer:
    pass # keeping class empty using pass (if not mentioned ---> error generated)

c1 = Computer() # stored as object in heap memory
print(id(c1))
c2 = Computer() # stored as different object in heap memory
print(id(c2))

class Mobile:
    def __init__(self): # special method (similar to constructor)
        self.name = 'Samsung'
        self.price = '1L'
    
    def config(self):
        print(f"Config: Name = {self.name}, Price = {self.price}")

    def compare(self, other):
        if self.price == other.price:
            return True
        else:
            return False

# self - a pointer - assigned each object when objects are passed 

m1 = Mobile() 
m2 = Mobile()
m1.name = 'Apple' # changing the value of attribute for object m1
m1.config()
m2.config()

# Compare the objects
if (m1 == m2): # inefficient
    print("Same")
else:
    print("Different")

if m1.compare(m2):
    print("Same")