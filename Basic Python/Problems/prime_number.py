# Method 1
num = int(input("Enter the number: "))

for i in range(2, num):
    if num % i == 0:
        print("Not a prime number")
        break
else:
    print("A prime number")

# Method 2 - efficient way to find prime number