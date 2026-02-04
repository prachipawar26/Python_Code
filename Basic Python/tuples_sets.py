# Tuples ---> ordered, immutable, allows duplicate values
# Tuple are more efficient than lists (size of list is more than tuple)
# Tuple is similar to list and is immutable while list is mutable
nums = (21, 34, 55, 98, 21)
# Accessing tuple
print(nums[3]) # returns 98; 4th value

# Operations on tuple - count, index
print(nums.count(21)) # returns number of times an element appears
print(nums.index(34)) # returns index of specified value
# tuple is faster than list

# tuple with single element
t1 = ("B") 
print(type(t1))
t2 = ("A", ) # ',' is neccessary for element to be recognized as a tuple (else will be of type 'str')
print(type(t2))

t3 = "Prachi", 20, "Mumbai" # another way to initialize tuple
print(type(t3))
name, age, city = t3 # unpacking the elements of tuple
print(name)
print(age)
print(city)

# unpacking tuple
print(nums)
i1, *i2, i3 = nums # i1 ---> first element, i3 ---> last element, *i2 ---> all rest elements in between i1 and i3
print(i1)
print(i2)
print(i3)

# Sets ---> unordered, mutable, no duplicates
# Set is collection of unique elements
s1 = {42, 93, 24, 55, 16, 67}
print(s1) # returns elements in random sequence as it uses hashing
s2 = {42, 93, 42, 55, 42, 67}
print(s2) # return only unique elements, even if values are repeated; but element woth highest count is listed first

# Other ways to create set ---> element position will be arbitary
s3 = set([1, 2, 3])
print(s3)
s4 = set("Hello")
print(s4)

# Creating empty set:
s5 = set() # using s5 = {} will create empty dictionary
print(type(s5))

# Adding elements
s5.add(2)
s5.add(5)
s5.add(7)
s5.add(12)
s5.add(15)
s5.add(17)
s5.add(22)
s5.add(25)
s5.add(7) # will skip as already 7 exist in set
print(s5)

# Removing elements
s5.remove(25) # key does not match ---> error
print(s5)
s5.discard(22) # key does not match ---> no error
print(s5)
s5.pop() # removes arbitary value
print(s5)
s5.clear() # empty the set
print(s5)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7, 11}

# Union of two sets
u = odds.union(evens) 
print(u)

# Intersection of two sets
i1 = odds.intersection(evens)
print(i1)
i2 = odds.intersection(primes)
print(i2)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 4, 10, 11, 12, 13, 14, 15}

# Difference of two sets
d1 = setA.difference(setB)
print(d1)

d2 = setA.symmetric_difference(setB)
print(d2)

# Subset, Superset & Disjoint
print(setA.issubset(setB))
print(setA.issuperset(setB))
print(setA.isdisjoint(setB))

# Modify the set in place - update(), intersection_update(), difference_update(), symmetric_difference_update()
setA.update(setB)
print(setA)

setA.intersection_update(setB)
print(setA)

setA.difference_update(setB)
print(setA)

setA.symmetric_difference_update(setB)
print(setA)

# modifying the copied set using assignment operations, modifies original set as well
# use cpy_s = s.cpoy() or cpy_s = set(s) instead of cpy_s = s

# Frozenset ---> immuatble version of set
a = frozenset([1, 2, 3, 4])
print(type(a))
print(a)

# Set Comprehension
s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s_even = {i for i in s if i % 2 == 0}
print(s_even) # return unordered set of all evens from set s
