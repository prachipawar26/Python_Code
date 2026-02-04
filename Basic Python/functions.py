# Functions helps define repeating tasks once and use multiple times
# use def functionName():
def greet(): # function definition
    print("Hello!")
    print("Good Morning!")

greet() # explicit calling of function

# Function can serve two ways - perform a task or return value
# Function to add two numbers
# formal arguments - passed in function definition
def add(a, b): # parameterized (arguments) function
    c = a + b
    print("Addition: ", c)

add(4, 5) 
# actual arguments - passed in function call

# Function to substract two numbers
def sub(a, b): # parameterized (arguments) function
    return a - b

result = sub(4, 5)
print("Substraction: ", result)

# returning two values
def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d

result1, result2 = add_sub(5, 4) # accepting two values
print("Addition: ", result1, "Substraction: ", result2)

# Best practice is to have different functions to different tasks

# Function arguments
def update(x):
    # x = 8
    print(id(x))
    print("x = ", x)

a = 10
print(id(a))
update(a) # passing 10 not a



def updates(x):
    x = 8
    print(id(x))
    print("x = ", x) # updates to value 8 but a remains 10 as object link is broken
a = 10
print(id(a))
print("a = ", a)

updates(a)
print("a = ", a)

# by default function is passed by object reference (address) but as the values changes, the address changes

# updates the original list as well
def modify(list):
    print(id(list))

    list[1] = 25
    print(id(list))
    print("x = ", list)

lst = [10, 20, 30]
print(id(lst))
modify(lst)
print("lst = ", lst)

# Types of actual arguments - position, keyword, default, variable length
# position arguments - needs to follow sequence while passing parameter
def person1(name, age):
    print("Name: ", name)
    print("Age: ", age)

person1('Prachi', 20) # correct positioning
# person(20, 'Prachi') # would work but is fatal for variables as sequencing is incorrect

# keyword arguments - mentioning the variable name (when sequence is not known)
person1(age=20, name='Prachi') # works even if positioning is wrong

# default argument - sets a default value to a formal argument suggesting if that actual argument is not passed, the function still works
def person2(name, age = 18): # if actual argument not passed for age then default value will be 18
    print("Name: ", name)
    print("Age: ", age)

person2('Prachi')

# variable length arguments - number of arguments are not fixed
def sum(p, *q):
    # r = p + q # generates error ad int + tuple 
    r = p
    for i in q:
        r += i
    print(r)

sum(5, 7, 34, 22) # 5 will be assigned to p and rest to q as tuple

# keyworded variable length arguments
def person(name, **data):
    print("Name: ", name)
    print("Data: ", data)
    for i, j in data.items(): # getting key-value pair
        print(i, j)

person('Prachi', age=20, city='Mumbai', mob=1234567890) # multiple data passed into data

# Passing list of elements & get list of elements
def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

lst = [10, 15, 20, 25, 30, 35, 40, 45, 50]
even, odd = count(lst)
print("Even List: {}, Odd List: {}".format(even, odd))

# Functions are object in python
# Anonymous Functions (Lambda) - used when function only used  once, have name for no function, have one expression
sqr = lambda s : s * s
res = sqr(5)
print(res)

add_num = lambda a, b : a + b
res_add = add_num(5, 6)
print(res_add)

# filter(), map(), reduce()
# filter()
nums = [3, 2, 1, 4, 5, 8, 2, 9]
evens = list(filter(lambda n : n % 2 == 0, nums))
print(evens)

# map()
doubles = list(map(lambda n : n * 2, evens))
print(doubles)

l1 = [1, 2, 3, 4, 5]
l2 = map(lambda x : x * 2, l1)
print(list(l2))
# or 
l3 = [x * 2 for x in l1]
print(l3)

from functools import reduce

# reduce()
sums = reduce(lambda n, m : n + m, doubles)
print(sums)

# sorted()
points2D = [(1, 2), (15, 1), (15, -1), (10, 4)]
points2D_sorted1 = sorted(points2D) # sorted by left values by default
print(points2D_sorted1)
points2D_sorted2 = sorted(points2D, key=lambda x : x[1]) # sorted by right values
print(points2D_sorted2)
points2D_sorted3 = sorted(points2D, key=lambda x : x[0] + x[1]) # sorted by sum of values
print(points2D_sorted3) 
