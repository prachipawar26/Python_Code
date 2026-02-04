# *args is used for multiple (0 or more) positional arguments
# **kwargs is used for multiple (0 or more) keyworded arguments
# *args is a tuple inside the function 
# **kwargs is a dictionary inside the function 
def my_func(a, b, *args, **kwargs):
    print(a, b)
    for a in args:
        print(a)
    for k in kwargs:
        print(k, kwargs[k])

my_func(1, 2, 3, 4, 5, six=6, seven=7)
my_func(1, 2, 3, four=4, five=5, six=6, seven=7)
my_func(1, 2)

# Umpacking Aguments
def func(a, b, c):
    print(a, b, c)

l = [0, 1, 2]
t = (3, 4, 5)
d = {'a':1, 'b':2, 'c':3}

# length of the actual parameters must match the formal parameters while unpacking
# keyworded actual parameters should also match the formal paramters

func(*l)
func(*t)
func(**d)