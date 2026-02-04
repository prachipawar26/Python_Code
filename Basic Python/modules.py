# GADP
# create a file as module
# importing calc module which is user defined

from calc import *

a = 9
b = 7

c1 = add(a, b)
c2 = sub(a, b)
c3 = mul(a, b)
c4 = div(a, b)

print("Addition = {}, Substraction = {}, Multiplication = {}, Division = {}".format(c1, c2, c3, c4))

# Special Variable: __name__
print("Value of __name__ in modules.py: ", __name__) # returns name of module - __main__