# Multi-dimentional arrays cannot be implemented using core python ---> use numpy library
from numpy import * # needs to be installed manually
# use pip (pip install packages) ---> `pip3 install numpy` using pip version 3
arr1 = array([1, 2, 3, 4, 5, 6])
print(arr1)
print()

arr2 = array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6], float)
print(arr2)
print()

# There are 6 ways to create an array - array(), linspace(), logspace(), arange(), zeros(), ones()
# Method 1
a1 = array([1, 2, 3, 4, 5])
print(a1)
print(a1.dtype)

a2 = array([1, 2, 3, 4, 5.0]) # other values are considered as float
print(a2)
print(a2.dtype) # returns float

# Method 2
a3 = linspace(1, 16, 4) # (start, stop (range included), break value to divide range into parts)
print(a3)

a4 = linspace(1, 16) # divides by default into 50 parts
print(a4)

# Method 3
a5 = arange(1, 15, 2) # (start, stop, skip by value)
print(a5)

# Method 4
a6 = logspace(1, 40, 5) # (start, stop, divide into value based on log values)
print(a6)
print('%.2f' %a6[3]) # returns value which has 2 digits after point

# Method 5
a7 = zeros(5) # arrays of size 5 with values 0
print(a7)

# Method 6
a7 = ones(5, int) # arrays of size 5 with values 1
print(a7)

# Adding a number to each element in an array
arr = array([10, 20, 30, 40, 50])
print(arr)
arr = arr + 5
print("Added value: ", arr)

# Adding two arrays (vectorized operation)
arr3 = array([10, 20, 30, 40, 50])
arr4 = array([5, 10, 15, 20, 25])
arr5 = arr1 + arr2
print(arr5)

# Trigonometric operations
print(sin(arr5))
print(cos(arr5))
print(log(arr5))
print(tan(arr5))

# Arithmetic operations
print(sqrt(arr5))
print(sum(arr5))
print(min(arr5))
print(max(arr5))

arr6 = array([33, 21, 11, 54, 33, 1])
print(arr6)
print(sort(arr6))

# Concatenating arrays
print(concatenate([arr3, arr4]))

# Copying an array - shallow copy, deep copy
print(arr6)
arr7 = arr6
print(arr7)

# pointing to same address
print(id(arr6))
print(id(arr7))

# pointing to different addresses
arr7 = arr6.view() 
print(id(arr6))
print(id(arr7))

arr6[0] = 20

print(arr6)
print(arr7)

# Shallow copy - if value is changed in first array, that value is updated in copied array too ---> use view()
# Deep copy - if value is changed in first array, that value is not updated in copied array ---> use copy()
arr7 = arr6.copy()
print(id(arr6))
print(id(arr7))

arr6[0] = 22

print(arr6)
print(arr7)