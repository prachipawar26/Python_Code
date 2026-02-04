# Function decorators
def div(a, b):
    print(a / b)

# The Decorator function
def smart_div(func):
    # The 'wrapper' function
    def inner(a, b):
        if a < b:
            # Swap values if 'a' is smaller than 'b'
            a, b = b, a
        return func(a, b)
    
    return inner

# Reassigning the function name to the decorated version
div = smart_div(div)

# Now, even though we pass (2, 4), the inner function swaps them to (4, 2)
div(2, 4)

@smart_div # function decorator
def div(a, b):
    print(a / b)

# This is now automatically the "smart" version
div(2, 4)

import functools

def se_decorator(func):
    @functools.wraps(func) # preserves information of used function
    def wrapper(*args, **kwargs):
        print('Start')
        res = func(*args, **kwargs)
        print('End')
        return res
    return wrapper

@se_decorator
def add5(x):
    return x + 5

print(add5(20))

# Decorator with arguments
def repeat(n):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n): # _ ---> throwaway variable name; just repeat without count
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator_repeat

@repeat(n = 3)
def greet(name):
    print(f"Hello, {name}")

greet('Prachi')

# Nested decorators
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        sign = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__!r}({sign})")
        res = func(*args, **kwargs)
        print(f"Calling {func.__name__!r} returned {res!r}")
        return res
    return wrapper

@debug
@se_decorator
def say_hello(name):
    greetings = f'Hi, {name}'
    print(greetings)
    return greetings

say_hello('Prachi')