# To use math function use python math modules
import math as m # 'as' used to set alias name for imported module

print(m.sqrt(25)) # returns square root of number
print(m.floor(9.9)) # returns floor value of number - lowest integer
print(m.ceil(23.54)) # returns ceiling value of number - highest integer
print(m.pow(3, 2)) # exponentiation
print(m.pi) # pi value
print(m.e) # e value

from math import sqrt, pow # only import specific functions; eliminates need to write module name everytime

print(sqrt(68))
print(pow(9, 4))

# To explore math functions ---> type help('math') in python shell