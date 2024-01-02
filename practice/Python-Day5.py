# Function def   Beginner:Function-1
def myfunction():
    print("statement1 printed")


myfunction()


def greet(name):
    print("Hello,", name)


greet("Milind")
greet(2)


def print_car_details(brand, color, price):
    print("Car with brand:", brand, "Color:", color, 'and price:', price)


print_car_details("Mercedes", "red", 2310000)
print_car_details(price=230000, brand="Volvo", color='red')


def multiply(a, b):
    '''
    When you type three quotes below def, some auto suggestion comes. You can use this when used with help(func_name)
    :param a:
    :param b:
    :return:
    '''
    print(a * b)


multiply(5, 7)
multiply("Milind", 5)  # this will also work. See output. it is string repeated n times
multiply(5, 'Milind')

# name = input("Please enter your name:")  # May include spaces.. everything is by default considered as String
name = 'ABC'
multiply(name, 8)


# Function def   Beginner:Function-2    4th Aug 2023
def simpleFunc(a, b):
    """
    This is docstring
    :param a: str or int
    :param b: str or int , see the effect of simpleFunc(1, "mmm")
    :return:
    """
    print("Addition is:", a, b)
    print("Addition is", a + b)


simpleFunc(1, 2)
# simpleFunc(122, "mmm")
# simpleFunc(b='hhh', 7) position based arg is not supported after keyword based arg

simpleFunc(4, b=77)


def funcWithDefaultArg(a, b, c=8):
    print(a, b, c)


funcWithDefaultArg(2, 4)
funcWithDefaultArg(1, 2, 3)

'''
def funcWithDefaultArgFirst(a, b, c=8, d): SyntaxError: non-default argument follows default argument   --same as Java
    print(a,b,c)
'''

age = 12


def showMyLocalAge():
    age = 20  # defining local variable, it overrides global variable and creates new variable with local scope
    print("age:", age)


showMyLocalAge()
print("age:", age)


def useGlobalAge():
    global age  # we are saying that please use global age variable. Do not create new variable.
    age = 20
    print("age:", age)


useGlobalAge()
print("age:", age)

# Lambda function
cube_n = lambda n: n ** 3  # no need to write 'def', no need to write 'return' as well

print('cube of n:', cube_n(5))

power_n = lambda a,b: a**b

print("Power:", power_n(2, 3))

# map - execute single function on multiple items
# Syntax: map(function_to_perform, iterables)
num_list = [1, 2, 3, 4, 5]
cubes = map(cube_n, num_list)
print('cubes:', cubes, list(cubes))

doubles = list(map(lambda a: a*2, num_list))
print('doubles:', doubles)

# Search for 'pass' keyword
