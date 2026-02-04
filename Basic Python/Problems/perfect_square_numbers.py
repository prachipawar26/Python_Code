# Perfect squrare numbers ---> is square root of a number is integer
from math import sqrt

for i in range(1, 501):
    if(sqrt(i).is_integer()):
        print(i)