# No fixed size for arrays - dynamic nature
# Array can hold values of same data type
# Needs array module to be imported
from array import *

val = array('i', [5, 10, 8, 2, 12, 1])
print(val)

# val = array('i', [5, 10, 8.5, 2, 12, 1]) # returns type error
# print(val)

print(val.buffer_info()) # returns (address, size of array)
print(val.typecode) # returns 'i' for integer
val.reverse()
print(val) # returns reversed array
print(val[1]) # returns 2nd value from reversed array

for i in range(6): # when length of array is knwon
    print(val[i]) # returns all values one by one
print()

for i in range(len(val)): # when length is unknown
    print(val[i])
print()

# or

for v in val:
    print(v)
print()

newVal1 = array(val.typecode, (a for a in val)) # assigning values from val into new array called newVal
for v in newVal1: 
    print(v)
print()

newVal2 = array(val.typecode, (a * a for a in val)) # assigning squared values from val into new array called newVal
for v in newVal2: 
    print(v)
print()

charVal = array('u', ['a', 'e', 'i', 'o', 'u'])
print(charVal)

# Getting array vales from users

arr = array('i', []) # creating empty array
n = (int(input("Enter length of array: ")))
for i in range(n):
    x = int(input("Enter the value: "))
    arr.append(x) # adding values to the array
print(arr)

# Printing index of an element in array
key = int(input("Enter value to search: "))

i = 0
for a in arr:
    if a == key:
        print("Value present at index position: ", i)
        break
    i += 1

# or

print("Value present at index position: ", arr.index(key))