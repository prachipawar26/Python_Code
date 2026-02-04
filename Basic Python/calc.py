# A module of functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def main():
    print('Hello')

# Special Variable: __name__
print("Value of __name__ in calc.py: ", __name__) # returns name of module - __calc__

if __name__ == "__main__":
    print('Hi, this is calc.py')