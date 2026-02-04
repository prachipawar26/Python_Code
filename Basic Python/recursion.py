def greet():
    print("Hello!")
    # greet() # recursion

# maximum recursion limit is 1000
# unnecessary recursion can cause breakdown or crash of system

greet()

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000) # changes values to 2000
print(sys.getrecursionlimit())
