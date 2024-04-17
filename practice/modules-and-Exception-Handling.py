"""
    .py file
        module
            package/library
"""
# Method 1
import math  # Import all functions of module, called by math.XXX as math.pow(2,3)
math.pow(4,5)
# Method 2

from math import *  # everything can be called without math. such as pow(2,3), overwritten code in case of collision.

# Method 3
from math import floor, ceil, pow

# Method 4
import MyMathModule as mm

mm.my_add()
floor(4.6)

# Method 5
from math import factorial as fc, gamma as g

r = math
print(isinstance(math, object))
print(math.pow(2, 3))
print(r.pow(2, 3))

help(math.pow)

import random

r = random.randint(0, 10)
print("Random number:", r)
random.seed(100)  # setting Seed value

#  -- Exception Handling

try:
    print(3/0)
except:
    print("Error occurred. Generic. not any specific. No idea what this is, but it is taken care of for now.")

try:
    print(3 / 2)
except ZeroDivisionError:
    print("Caught Divide by zero error")
finally:
    print("This will get executed all the time. (with/without error)")

try:
    print(3 / 0)
except ZeroDivisionError as z:
    print("Caught Divide by zero error:", z)
finally:
    print("This will get executed all the time. (with/without error)\n\n")

l = [2, 0, "Hello", None, True]

for e in l:
    try:
        print(f'Current Element- {e}')
        result = 5 / int(e)
        print("Result- ", result)
    except Exception as ex:
        print(f'SOS - {ex}')
        # raise Exception('THIS PASSWORD IS INCORRECT')
    print("-" * 15)


class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


# raise MyCustomException("This is My own exception")


class SalaryNotInRangeError(Exception):
    def __init__(self, message):
        super().__init__(message)


def check_salary(salary):
    try:
        if salary not in range(10001, 100000):
            raise SalaryNotInRangeError("Salary is not in range")
        else:
            print("Congratulations!!")

    except SalaryNotInRangeError as e:
        print(e)

check_salary(10001)
check_salary(101)