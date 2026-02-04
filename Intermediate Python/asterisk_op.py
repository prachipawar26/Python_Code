# Different use of asterisk (*) Opertor

# Multiplication
a = 2 * 4
print(a)

# Exponentiation
b = 2 ** 4
print(b)

# Create lists/tuples/strings with repeated elements
zeros = [0] * 10
print(zeros)

ones = (1, 2) * 5
print(ones)

string = "AB" * 7
print(string)

# Used for args and kwargs
# Used for unpacking lists/dictionaries

nums = [1, 2, 3, 4, 5, 6]
*beginning, last = nums
print(beginning) # returns a list
print(last)

# Merging - results in a list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

# Merging two dictionaries
d_a = {'a': 1, 'b': 2}
d_b = {'c': 3, 'd': 4}

new_d = {**d_a, **d_b}
print(new_d)