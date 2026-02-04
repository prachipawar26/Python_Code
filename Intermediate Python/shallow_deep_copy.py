# Shallow Copy - one level deep, only refernces of nested child objects
# Deep Copy - full independent copy
# does not change in original if changed in copy
num1 = 5

cpy_num1 = num1
print(cpy_num1)

cpy_num1 = 6
print(cpy_num1)
print(num1)

# updates in both original and copied list, since mutable data type
num2 = [0, 1, 2, 3, 4]

cpy_num2 = num2
cpy_num2[0] = -10

print(cpy_num2)
print(num2)

# Shallow Copy - does not change in original variable
import copy
num3 = [10, 20, 30, 40]
cpy_num3 = copy.copy(num3)
# or
cpy_num3_ = num3.copy()
# or
cpy_num3_1 = list(num3)
# or
cpy_num3_2 = num3[:]

cpy_num3[0] = 0
cpy_num3_[0] = -1
cpy_num3_1[0] = -2
cpy_num3_2[0] = -3
print(cpy_num3)
print(cpy_num3_)
print(cpy_num3_1)
print(cpy_num3_2)
print(num3)

# Nested list - changes in both copy and original
nums = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(nums)
cpy[0][1] = -10

print(cpy)
print(nums)

# Deep Copy - does not change original variable
nums_d = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy_d = copy.deepcopy(nums_d)
cpy_d[0][1] = -11

print(cpy_d)
print(nums_d)

# Using copy for class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# changes original parameter
p1 = Person('Prachi', 20)
p2 = p1

p2.age = 21
print(p2.age)
print(p1.age)

# does not change original parameter
p1_ = Person('Prachi1', 22)
p2_ = copy.copy(p1_)

p2_.age = 23
print(p2_.age)
print(p1_.age)

class Company:
    def __init__(self, boss, emp):
        self.boss = boss
        self.emp = emp

# Shallow copy
c = Company(p1, p1_)
c_clone = copy.copy(c)
c_clone.boss.age = 55

print(c_clone.boss.age)
print(c.boss.age)

# Deep Copy
c_clone_ = copy.deepcopy(c)
c_clone.boss.age = 56

print(c_clone_.boss.age)
print(c.boss.age)
