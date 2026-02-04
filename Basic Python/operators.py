# Operators
"""
1. Arithmetic ---> +, -, *, /, //, %, **
2. Assignment ---> =
3. Relational ---> <, >, <=, >=, ==, !=
4. Logical ---> AND, OR, NOT
5. Unary ---> +, -
6. BitWise ---> ~, &, |, ^, <<, >>
"""

# Arithmetic
x = 100
y = 12
print(x + y) # addition
print(x - y) # substraction
print(x * y) # multiplication
print(x / y) # normal division
print(x // y) # integer division
print(x % y) # modulo
print(x ** 2) # exponentiation

#  Assignment
x = x + 2 # way of increment
print(x)
x += 10 # way of increment
print(x)
x *= 3
print(x)

a, b = 10, 15 # multiple variables assigned at once
print(a)
print(b)

# Unary 
n = 7
# negation
print(-n) # return -7
n = -n
print(n) # returns -7

# Relational
print(a < b) # lesser than?
print(a > b) # greater than?
print(a <= b) # lesser than or equal to? 
print(a >= b) # greater than or equal to? 
print(a == b) # equal to?
print(a != b) # not equal to? 

# Logical 
# AND - if both condition true ---> returns true; if any condition false ---> returns false
# OR - if both condition false ---> returns false; if any condition true ---> returns true
# NOT - if true ---> returns false (vice versa)
print(a < 8 & b > 10) # AND
print(a < 8 | b > 10) # OR
print(not(b > 10)) # NOT

# BitWise
print(~12) # complement; returns '-13' as complement of 12 = 2's complement of 13 
print(10 & 15) # bitwise AND (&)
print(25 | 30) # bitwise OR (|)
print(42 ^ 10) # XOR (^) - if both binary numbers 0 or 1 ---> 0; if one 0, other 1 ---> 1
print(10 << 2) # left shift
print(10 >> 2) # right shift