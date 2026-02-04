# Generators - memory efficient
# once a values is accessed, it cannot be accessed again in one go

def my_generator():
    yield 3
    yield 2
    yield 1

g = my_generator()
print(g)

# print(sum(g)) # returns sum of values in generator
# print(sorted(g)) # returns sorted order

for i in g:
    print(i)

# or 

# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value) 
# if yield next yield is not found ---> StopIteration error

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
for i in cd:
    print(i)

# Memory inefficient function
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# Memory efficient generator
def firstn_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1

import sys

print(sum(firstn(10)))
print('Size of normal function: ', sys.getsizeof(firstn(100)))
print(sum(firstn_gen(10)))
print('Size of generator function: ', sys.getsizeof(firstn_gen(100)))

# don't have to wait as elements are generated before use

# Generator with expression
mygen = (i for i in range(10) if i % 2 == 0)
print(list(mygen))