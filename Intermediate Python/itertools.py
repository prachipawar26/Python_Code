from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat # count(), cycle(), repeat() ---> infinite iterators

a = [1, 2]
b = [3, 4]

# Product
prod1 = product(a, b)
print(prod1)
print(list(prod1))

c = [5]

prod2 = product(b, c, repeat=2) # using repeact ---> each product is repeated twice
print(list(prod2))

d = [1, 2, 3]

# Permutation
per1 = permutations(d)
print(list(per1))

per2 = permutations(d, 2) # 2 ---> length of permutation
print(list(per2))

# Combination
com1 = combinations(d, 2) # 2nd parameter mandatory
print(list(com1))

com2 = combinations_with_replacement(d, 2) # combination of same elements is included 
print(list(com2))

# Accumulate
acc1 = accumulate(d) # returns (by default) gradual sums of items in list; [(1, 1 + 2 = 3, 2 + 3 = 6) ---> (1, 3, 6)] 
print(d)
print(list(acc1)) 

import operator as op

acc2 = accumulate(d, func=op.mul) # returns gradual operation specified on items in list; returns gradual multiplied items' list; [(1, 1 * 2 = 2, 2 * 3 = 6) ---> (1, 2, 6)]
print(d)
print(list(acc2)) 

e = [1, 2, 5, 4, 3]

acc3 = accumulate(e, func=max) # returns max item in list at each point
print(e)
print(list(acc3))

# GroupBy
grp1 = groupby(e, key=lambda x : x < 3) # grouping by values less than 3
for key, val in grp1:
    print(key, list(val))

people = [
    {'name': 'ABC', 'age': 25},
    {'name': 'XYZ', 'age': 24},
    {'name': 'PQR', 'age': 24},
    {'name': 'MNO', 'age': 25},
    {'name': 'STU', 'age': 27}
    ]

grp2 = groupby(people, key=lambda x : x['age'])
for key, val in grp2:
    print(key, list(val))

# Count
for i in count(10): # starts count at 10
    print(i)
    if i == 15: # if not specified, loop will run infinitely
        break

# Cycle
count = 0
for i in cycle(d):
    print(i)
    count += 1
    if count == 10: # if not specified, loop will run infinitely
        break

# Repeat
count = 0
for i in repeat(1): # repeats infinitely
    print(i)
    count += 1
    if count == 5:
        break

for i in repeat(1, 6): # repeats only 6 times
    print(i)