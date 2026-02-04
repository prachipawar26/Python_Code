def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

result = fact(5)
print(result)

# Recursive factorial

def r_fact(n):
    if n == 0:
        return 1
    else:
        return  n * r_fact(n - 1)
    
res = r_fact(5)
print(res)