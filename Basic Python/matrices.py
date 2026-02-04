from numpy import *

# 2d array
arr1 = array([
    [1, 2, 3, 7, 8, 9],
    [4, 5, 6, 10, 11, 12]
])

print(arr1)
print(arr1.dtype) # type of values
print(arr1.ndim) # number of dimensions
print(arr1.shape) # number of rows & columns
print(arr1.size) # number of values

# Converting 2d array into 1d array
arr2 = arr1.flatten()
print(arr2)
print(arr2.dtype)
print(arr2.ndim) 
print(arr2.shape)
print(arr2.size)

# 1d array to 2d array
arr3 = arr2.reshape(3, 4) # 3 rows, 4 columns
print(arr3)
print(arr3.dtype)
print(arr3.ndim) 
print(arr3.shape)
print(arr3.size)

# 1d to 3d
arr4 = arr2.reshape(2, 2, 3) # 2 2d arrays, each with 2 rows and 3 values/columns
print(arr4)
print(arr4.dtype)
print(arr4.ndim) 
print(arr4.shape)
print(arr4.size)

# Converting 2d array into matrix format
arr5 = array([
    [1, 2, 3],
    [4, 5, 6]
])

# Method 1
# matrix() provides more operations to perform
mat1 = matrix(arr5)
print(mat1)

# Method 2
mat2 = matrix('1 2 3 4 ; 5 6 7 8') # 2 rows, 4 columns
print(mat2)

mat3 = matrix('1 2; 3 4; 5 6; 7 8') # 4 rows, 2 columns
print(mat3)

mat4 = matrix('1 2 3; 4 5 6; 7 8 9') # 3 rows, 3 columns
print(mat4)

print(diagonal(mat4)) # print diagonal elements
print(mat4.min()) # minimum element
print(mat4.max()) # maximum element

# Adding two matrices
add1 = mat4 + mat4
print(add1)

# Mulitplying two matrices
mul1 = mat4 * mat4 # automatic matrix multiplication; not normal multiplication
print(mul1)
