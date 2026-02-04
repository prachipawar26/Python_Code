# Method 1 - uses extra variable
num1 = 5
num2 = 10

print(f"1. Before swap: a = {num1}, b = {num2}")
temp = num1
num1 = num2
num2 = temp
print(f"1. After swap: a = {num1}, b = {num2}")

# Method 2 - needs extra bit (as int internally converts into binary for calculation)
print(f"2. Before swap: a = {num1}, b = {num2}")
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(f"2. After swap: a = {num1}, b = {num2}")

# Method 3 - most efficient using xor
print(f"3. Before swap: a = {num1}, b = {num2}")
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
print(f"3. After swap: a = {num1}, b = {num2}")

# Method 4 - unique to python (uses concept of 2 rotation with stack)
print(f"4. Before swap: a = {num1}, b = {num2}")
num1, num2 = num2, num1
print(f"4. After swap: a = {num1}, b = {num2}")
