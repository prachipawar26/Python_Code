class Calculator:
    def add(self, a, b, c=0): # 'c' is optional
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))    # 15
print(calc.add(5, 10, 2)) # 17