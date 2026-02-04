a = 10 # global variable - can be used everywhere (outside & inside function or class)

def something1():
    a = 15 # local variale - can only be used inside function
    print("Inside function", a)

something1()
print("Outside function", a) # will not change

# preference will always given to local variable

b = 10

def something2():
    global b # to specify that a can be globally used
    b = 15
    print("Inside function", b)

something2()
print("Outside function", b) # will change

# Changing value of global variable defined outside function without using global keyword
c = 10
print(id(c))

def something3():
    c = 15
    x = globals()['c'] # get only global variable c
    print(id(x))
    print("Before change", x)
    print("Inside function", c)
    globals()['c'] = 15 # changing global variable without affecting local variable

something3()
print("Outside function", c) # will change


