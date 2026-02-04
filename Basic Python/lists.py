# Lists ---> ordered, mutable, allows duplicate values
# Assigning multiple values to a variable creates list
nums = [25, 30, 45, 38, 21]
# Accessing value at each index
print(nums[0]) # value at 1st position (0th index)
print(nums[4]) # value at 5th position (4th index)
# If index doesnot match ---> out of bound error

# Accessing multiple values
print(nums[1:4])

# List of strings
fruits = ['Apple', 'Orange', 'Grapes', 'Banana']
print(fruits[1])
print(fruits[1:3]) 

# Check if element present
if "Orange" in fruits:
    print("Yes")
else:
    print("No")

# List with different data types
mixed = [9.5, 'Prachi', 25, True]
print(mixed[3])
print(mixed[2:])

# List of list
combine = [nums, fruits, mixed]
print(combine)

# Operations of list - mutability (append()), insert, clear, pop, remove, count, reverse
nums.insert(2, 12) # insert 12 at 2nd index
print(nums)
nums.remove(38) # removes 38 from list
print(nums)
nums.pop(2) # removes values at 2nd index
print(nums)
nums.pop() # removes values at end
print(nums)
del nums[2:] # deletes values from 2nd index
print(nums)
nums.append(33) # appends value at end
print(nums)
nums.extend([29, 12, 99]) # adds multiple values at end
print(nums)
print('Min: ', min(nums))
print('Max: ', max(nums))
print('Sum: ', sum(nums))
# sort() ---> sorts list in place
# sorted() ---> sorts as new list
print(fruits)
new_fruits = sorted(fruits)
print(new_fruits)
nums.sort() # sort list
print('Sorted list: ', nums)
print(nums.count(30)) # returns number of times an element appears

# Concatenating two lists
new_concat = fruits + nums
print(new_concat)

# List of zeroes
z = [0] * 5
print(z)

# Creating modified list from existing list
a = [1, 2, 3, 4, 5, 6]

# List comprehension
b = [i * i for i in a] # expression to get a squared list of a
print(a)
print(b)

# modifying the copied list using assignment operations, modifies original list as well
# use cpy_list = list.cpoy() instead of cpy_list = list
