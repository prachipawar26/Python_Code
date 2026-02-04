# try and except - used for handling errors without breaking the rest of code
# e.g.: using when only integer input is accepted and rest must be handled
# Types of errors - Compile time (syntactical), logical, run time 

try:
    value = 10/0
    num = int(input("Enter the number: "))
    print(num)
# except: # error handled for all exceptions
#     print("Invalid input")
except ZeroDivisionError: # specific error handler
    print("Divide by zero error")
# or 
# except ZeroDivisionError as err:
#     print(err)
except ValueError:
    print("Invalid input")
    
finally: # execute no matter if error or exception occurred or not
    print("End")

# sequence of error handling matters


# x = -5
x = 5
if x < 0:
    raise Exception('a should be positive')

# y = -10
y = 10
assert(y >= 0), 'y is not positive'

class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, msg, val):
        self.msg = msg
        self.val = val

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is to high')
    if x < 5:
        raise ValueTooLowError('Value is to low')
    
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e)