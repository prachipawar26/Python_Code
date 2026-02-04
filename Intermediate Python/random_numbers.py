import random # generate psuedo random numbers ---> reproducible

a = random.random() # returns random float
print(a)

b = random.uniform(1, 10) # generates random float in range 1 to 10
print(b)

c = random.randint(1, 10) # generates random int in range 1 to 10; upper bound included
print(c)

d = random.randrange(1, 10) # generates random int in range 1 to 10; upper bound excluded
print(d)

e = random.normalvariate(0, 1) # mean = 0, std dv = 1; generates random number from normal distribution
print(e)

l1 = list("ABCDEFGH")
f1 = random.choice(l1) # picks random element from the list
print(f1)

f2 = random.sample(l1, 5) # picks 5 elements as in a sample; sampling without replacement (only unique elements)
print(f2)

f3 = random.choices(l1, k=6) # picks 6 elements with replacement (repeated elements allowed)
print(f3)

# Random shuffle
random.shuffle(l1)
print(l1)

# Reproducibility
random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1) # helps random return exact same random value that is previously generated
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

# since random numbers generated from random module are reproducible ---> not recommended for security purposes
# use secrets module instead
import secrets # used for passwords, tokens, authentication

s1 = secrets.randbelow(10) # generates random int from range 0 to 10 (excluded)
print(s1)

s2 = secrets.randbits(4) # generates random int from range 0 to 15 (0000 to 1111)
print(s2)

s3 = secrets.choice(l1) # pick random choice (not reproducible)
print(s3)

# For arrays use numpy
import numpy as np

n1 = np.random.rand(3) # array of 3 random float
print(n1)

n2 = np.random.rand(3, 3) # 3x3 array of floats
print(n2)

n3 = np.random.randint(0, 10) # generates int value from range 0 to 10 (excluded)
print(n3)

n4 = np.random.randint(0, 10, 3) # 1d array of 3 int elements
print(n4)

n5 = np.random.randint(0, 10, (3, 4)) # 3x4 array of random ints
print(n5)

# Random shuffle
np.random.shuffle(n5) # shuffles between rows
print(n5)

np.random.seed(1)
print(np.random.rand(3, 3))

np.random.seed(1) # reproduces sames array
print(np.random.rand(3, 3))
