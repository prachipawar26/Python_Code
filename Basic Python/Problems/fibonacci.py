# Fibonacci Series
def fib(n):
    a = 0
    b = 1

    if n <= 0:
        print("Does not exist")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
    
    for i in range(2, n):
        temp = a + b
        a = b
        b = temp
        # if temp < 100: for series number less than 100
        print(temp)

fib(10)

# Fibonacci using generator
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

f = fibonacci(30)
for i in f:
    print(i)