for i in range(6):
    for j in range(6):
        print("#", end="")
    print()

for i in range(6):
    for j in range(i + 1):
        print("#", end="")
    print()

for i in range(6):
    for j in range(6 - i):
        print("#", end="")
    print()

for i in range(1, 5):
    for j in range(i, 5):
        print(j, end="")
    print()

fixed_chars = "PQR"
for i in range(1, 5):
    for j in range(i):
        print(chr(65 + j), end="")
    r_count = 4 - i
    if r_count > 0:
        print(fixed_chars[i-1 : i-1 + r_count], end="")
    print()