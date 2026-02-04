# Data Types
"""
1. None
2. Numeric
3. List
4. Tuple
5. Set
6. String
7. Range
8. Map/Dictionary

## None - type of variable having no assigned value = None

## Numeric
1. int
2. float
3. complex
4. bool - 'True' or 'False'

## Sequence
1. List
2. Tuple
3. Set
4. String
5. Range

## Dictionary - key-value pairs (all keys have to be unique)
"""

a = 10
print(type(a)) # returns 'int'
b = 33.4
print(type(b)) # returns 'float'
c = a + 9j
print(type(c)) # returns 'complex'; imaginary part is specified using 'j' after a number instead of 'i'
d = True
print(type(d)) # returns 'bool'

# Type & Conversion
x1 = 5.6
y1 = int(x1)
print(y1)
print(type(y1)) # returns 'int'
x2 = 5
y2 = float(x2)
print(y2)
print(type(y2)) # returns 'float'

complexNum = complex(x1, x2)
print(complexNum)
print(type(complexNum))

print(True)
print(int(True))
print(type(int(True)))

l = [10, 20, 50, 30]
print(type(l))
s = {10, 20, 50, 30}
print(type(s))
str = "Prachi"
print(type(str)) # returns 'str'
print("Range: ", range(10))
print("List of Range: ", list(range(10)))
print(type(range(10))) # returns 'range'

d = {'1':'Samsung', '2':'Apple', '3':'Huawei'}
print(d.keys()) # returns keys in dictionary
print(d.values()) # returns values in dictionary
print(type(d)) # returns 'dict'