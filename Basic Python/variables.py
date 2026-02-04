# In python no need to define data type
# Variable is a container to store value  
variable = 10 # variable declaration and definition

# Operations can be performed on variables 
# Examples
fisrt_name = "Prachi"
last_name = "Pawar"
concatName = fisrt_name + last_name
print(concatName)

# In older versions of python, in python shell '_' specifies the previous output
# Access characers of string variable
name = 'Prachi'
print(name[4]) # returns h
# indexing starts from 0
# if index number doesot match with length of string ---> error generated (out of bound)
# using negative index ---> characters are accesed from end
print(name[-4]) # returns a

# Accessing specfic characters 
print(name[0:3]) # returns characters from 0th index till before 3rd index
print(name[1:5]) # returns characters from 1st index till before 5th index
# Alternatives
print(name[1:]) # returns all characters from 1st index
print(name[:3]) # returns all characters before 3rd index
# if index after ':' is more than the length of string ---> returns characters from specific index to end  

# len() - returns the number of characters in string
print(len(name))

# Getting address of the variable
print(id(name))
a = 10
b = a
print(id(a))
print(id(b))
# Python is memory efficient as if the value in the two different variables is same, then both points to same memory address
c = 10
print(id(c)) 
# In python variable cannot be purely made constant but can referred as constant 

# type() - returns data type of variable
print(type(name)) # returns 'str'
print(type(a)) # returns 'int'