# # while loop
# i = 1 # initialization
# while(i < 6): # condition
#     print("Hello") # prints 'Hello' 5 times
#     i += 1 # iteration - incrementation

# i = 10
# while i >= 1: 
#     print(i) # prints 1 to 10 in reverse
#     i -= 1 # iteration - decrementation

# # if no increment or decrement provided given condition is true ---> block executes in infinity

# # Nested while loop
# i = 5
# j = 1
# while i > 1:
#     print("Prachi")
#     while(j <= 4):
#         print("Pawar")
#         j += 1
#     i -= 1

# i = 1
# while i <= 5:
#     print("Prachi", end=" ")
#     j = 1
#     while(j <= 5):
#         print("Hii", end=" ")
#         j += 1
#     i += 1
#     print()

# # for loop - prints in sequence
# l = ['Prachi', 20, 33.8]
# for i in l:
#     print(i)

# x = 'PRACHI'
# for i in x:
#     print(i) # prints all characters one by one 

# for i in [2, 5.5, 'Hello']:
#     print(i)

# for i in range(10):
#     print(i) # prints 0 to 9

# for i in range(1, 10): # range(start_number, end_number (exclusive))
#     print(i) # prints 1 to 9

# for i in range(1, 10, 2): # range(start_number, end_number (exclusive), iteration)
#     print(i) # prints 1 to 9 with increment of 2

# # to go reverse iteration is mandatory
# for i in range(20, 0, -3): # range(start_number, end_number (exclusive), iteration)
#     print(i) # prints 20 to 1 with iteration 2

# # Nested for loop

# # conditional statements can be used inside while loops or for loops

# # break, continue, pass
# # break - jump out of the loop - entire loop breaks - used in loops only
# i = 1
# while i <= 10:
#     if i > 7:
#         break
#     print(i)
#     i += 1
# print("Outside Loop")

# # continue - skip only specific and continue with next iteration - used in loops only
# for i in range(1, 21):
#     if i % 3 == 0 or i % 5 == 0: # skip multiples of 3 or 5
#         continue
#     print(i)

# # pass - nothing (null operation) - used anywhere (loops, functions and classes)
# for i in range(1, 21):
#     if i % 2 != 0: # pass the odd values
#         pass
#     else:
#         print(i)

# for else
nums = [12, 15, 18, 20, 26]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("not found")

nums = [12, 14, 18, 21, 26]
for num in nums:
    if num % 5 == 0:
        print(num)
        break # for else to work
else:
    print("not found")