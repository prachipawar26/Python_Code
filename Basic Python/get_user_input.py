# use of input() to get the input

# Getting integer input
x = input("Enter number 1: ")
y = input("Enter number 2: ")
z = x + y 
print(z) # returns concatenated value (eg. x = 9, y = 5 ---> z = 95)
# input() gets input as string ---> x is str, y is str
print("Type of x: ", type(x))
print("Type of y: ", type(y))

# To perform addition or else
# Method 1 - wasting variables
a = int(x)
b = int(y)
z = a + b
print(z) # returns added value (eg. x = 9, y = 5 ---> z = 14)

# Method 2 - efficient 
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
z = x + y 
print(z)

# Getting character input (no native support)
ch = input("Enter a character: ")[0]
print(ch) # returns only first character of string

# eval() - evaluates expression entered
ip = eval(input("Enter the expression: "))
print(ip) # returns value after calculation

# Getting input values passed in .py file running from terminal
import sys
p = int(sys.argv[1])
q = int(sys.argv[2])
r = p + q
print(r)

# go into folder consisting .py file and run `python file_name.py value1 value2`
# e.g.: prachipawar@N-7066 Basic Python % python3 get_user_input.py 6 5 ---> returns 11