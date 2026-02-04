# if statement - check if condition is true and perform code statements inside it
if(True): 
    print("It is True") # if condition inside if() is true ---> performs block {}

if(10 > 2):
    print("10 is greater than 2")

if 100 <= 50:
    print("100 is not lesser than 50") # will not return anything

# if-else statement - check if one condition is true; if false perform else block
if(10 < 2):
    print("If block: 10 is lesser than 2") # not true ---> no return 
else:
    print("Else block: 10 is greater than 2") # return if if() not true

# if-elif-else statement - check if one condition is true; if false perform elif block; if elif condition false perform else block
if 100 < 32:
    print("If block: 100 is lesser than 32") # not true ---> no return 
elif 100 >= 50:
    print("Elif block: 100 is greater than 50") # true ---> return

if(100 < 32):
    print("If block: 10 is greater than 32") # not true ---> no return 
elif(100 == 32):
    print("Elif block: 100 is not lesser than 32") # true ---> return
elif(100 > 32):
    print("Elif block: 100 is greater than 32")
else:
    print("Else block: error!")

# Nested if, elif, else
if 100 < 300:
    if 100 < 200:
        print("True") # this will print
    elif 100 > 200:
        print("False")
    else:
        print("Error!")