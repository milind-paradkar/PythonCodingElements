# functional programming
from builtins import reversed
from functools import reduce
from timeit import timeit

a = 10


def aa():
    # a = 30 This is creating new local variable a which does not overwrite a variable defined outside.
    global a  # Remove this and you will get error for below. Reason is a is not defined inside function.
    # when you say a=30 then you are redefining a. It never overwrites global a and never changes a outside this function.
    a = a + 1


aa()
print(a)

# It keeps data immutable

# lambda functions -- One liner function
# Higher order functions (function either taking function as an argument OR return another function)
# Decorators


nums = [1, 2, 3, 4, 5, 6]

nums.sort(reverse=True)
print(nums)
print(nums.sort(reverse=True))  # lst.sort() sorts the list but does not return anything !
print(sorted(nums, reverse=True))  # sorted() returns sorted list back
print(sorted(nums))  # sorted() returns sorted list back

n_sq = []
# approach 1
for i in nums:
    n_sq.append(i ** 2)
print("for loop Approach1:", n_sq)
# approach2
sqs = [i ** 2 for i in nums]  # using List comprehension
print("List comprehension Approach2:", sqs)

n_sq = map(lambda x: x ** 2, nums)
print("lambda with map function Approach3:", list(n_sq))
# approch 4
sq_lambda = lambda x: x ** 2  # assign a lambda to name and you can call name() as a function
print("Lambda function  Square:", sq_lambda(6))
print("Lambda function Approach4:", list(map(sq_lambda, nums)))

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
digits_t = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
digits_s = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
# print(int(digits)) # TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
print("Converting list of strings into int using map:", map(int, digits), " finally:", digits, " to ",
      list(map(int, digits)))
print("map(int, digits): Works like mapping int(each_item) of iterable digits.")

print("\n map(func, iterable) returns a map object. You can typecast it into list, tuple, etc.")
print(list(map(int, digits)))
print(tuple(map(int, digits_t)))
print(list(map(int, digits_s)))

print("\nPython tertiary condition writing ( ? : ) in Java:")
print('''if condition == true:
    x
else
    y

is written in Python as:
" x if condition else y "
''')

x = 59
y = 10
if x > y:
    print("Greater")
else:
    print("Less")

print("Greater" if x > y else "Less")
comparison = lambda f, s: "Greater" if f > s else "Less"
print(comparison(23, 87))
l1 = [12, 32, 2, 98, 809, 9, 9, 99, 78, 9, 98, 54, 8]
l2 = [43, 2, 67, 87, 6708, 78, 8, 7]
print("map function with more than one arg...")
print(list(map(comparison, l1, l2)))  # map function with more than one arg
print(
    "In case of more than one iterable, mapping function STOPS at min length of all iterables. THERE IS NO ERROR for length mismatch.")


def greater(x, y):
    return x > y


greater_la = lambda x, y: x > y
print(greater_la(3, 2))
print((lambda x, y: x > y)(2, 3))

students = [("Milind", 98, "Maths"), ("Colan", 100, "Algebra"), ("Adam", 78, "History")]  # List of tuples
print(f"\nstudents - a tuple: {students}")
print("Sorted by first element in tuple (by default) : ", sorted(students))
print("Sorted by second element [1] in tuple         : ", sorted(students, key=lambda dt: dt[1]))
print("Sorted by third element [2] in tuple          : ", sorted(students, key=lambda dt: dt[2]))

students = [{"name": "Milind", "marks": 98, "subject": "Maths"}, {"name": "Nolan", "marks": 88, "subject": "Algebra"},
            {"name": "Adam", "marks": 78, "subject": "History"}]  # dictionary
print(f"\nstudents - a dictionary: {students}")
print("Sorted by marks            :", sorted(students, key=lambda data: data['marks']))
print("Sorted by name (reversed)  :", sorted(students, key=lambda data: data['name'], reverse=True))
print("Sorted by subject          :", sorted(students, key=lambda data: data['subject']))


def simpleFunc():
    print("Simple func without any param called.")


def functionCaller(func):
    func()


functionCaller(simpleFunc)


def generateExponential(power):
    def exp(number):
        return number ** power

    return exp


print(
    f"2 ** 4: generated:[{generateExponential(4)}] which is of type [{type(generateExponential(4))}] -> Actual output:{generateExponential(4)(2)} ")
square = generateExponential(2)
cube = generateExponential(3)
print("5 square:", square(5))
print("5 cube:", cube(5))


def pow(n):
    return lambda x: x ** n


pow3 = pow(3)
print("pow3(4):", pow3(4))

print("\nhttps://pythontutor.com/\n")


# Decorators
def pretty(func):
    def myImplementaion():
        print("-" * 50)
        func()
        print("-" * 50)

    return myImplementaion


def awsome(func):
    def myImplementation():
        print("*" * 50)
        func()
        print("*" * 50)

    return myImplementation


def greeter():
    print("Hello, How are you!")


print("\nSimple Greeter")
greeter()
print("\nGreeter called with pretty and new function getting called")
pretty_greeter = pretty(greeter)
pretty_greeter()
print("\nDirect way to call additional functionality")
awsome(greeter)()
print()


# Let's redefine greeter with decorators

@pretty
@awsome
def greeter():
    print("Hello, How are you!")


print("\nRedefined greeter with decoratr. Note: we are calling original function only... Not creating any new function")
greeter()


@awsome
@pretty
def greeter():
    print("Hello, How are you!")


print("\nDecorator sequence matters!")
greeter()

print("\n\nSome use cases of functional programming:\n"
      "     Data should be separated from mutations.\n"
      "     Treat variables and functions as Unchangeable.")

# MAP: map() higher order function
squares = [i ** 2 for i in nums]  # short cut method to create a list
print("\nSquares:", squares)
# Same can be done with map function.
cubes = map(lambda x: x ** 3, nums)  # Theoretically this is faster than above way
print("cubes", cubes, list(cubes))


def checkSize(n):
    if n < 150:
        return 'S'
    elif n < 180:
        return 'M'
    else:
        return 'L'


# Same logic in ternary operator
chkSz = lambda n: 'S' if n < 150 else 'M' if n < 180 else 'L'
l = [120, 155, 200, 177, 67, 700, 160]
print(list(map(checkSize, l)))
# print("same as ?")
print(list(map(chkSz, l)))

# How to use timeit ?
# timeit('[i** 2 for i in range(100)]', number=1000)
l = map(lambda x: x ** 2, range(10))
for i in l:
    print(i)

# Good example to use map()
heights = [124, 136, 178, 200, 320, 200, 150, 156]


def complex_logic(h):
    if h < 151:
        return 'S'
    elif h < 180:
        return 'M'
    elif h < 300:
        return 'L'


'''
n= input() #Input as 1 2 3 4 5
nu = list(map(int, input.split()))
'''
'''
rand_nums = map(int, input()) # Short and smart
print(list(rand_nums))
'''
print("MAP:")
print("Important concept")
a = [1, 2, 3, 4, 5, 6, 7]
b = ('a', 'b', 'c')
c = {'x', 'y', 'z'}
print(
    f" a={a}\n b={b}\n c={c}\nconcatenating three iterables{list(map(lambda x, y, z: str(x) + str(y) + str(z), a, b, c))}\n")
print("# Map loops over more than one variable and loops as long as at least one is exhausted.")
print("# Map stops at end of smallest available iterable")

# Filters
print("\nFILTER:")
a = [i for i in range(1, 31)]
print(f"Main list:{a}, \nFILTER reduces elements based on condition: {list(filter(lambda x: x % 3 == 0, a))} ")

print("\nZIP:")
print("ZIP creates tuples of all iterables (collecting it in list)  :", list(zip(a, b, c)))
print("ZIP creates tuples of all iterables (collecting it in tuple) :", tuple(zip(a, b, c)))
print("ZIP creates tuples of all iterables (collecting it in list)  :", set(zip(a, b, c)))

student_data = [['S ROY', 4.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 5.0], ['G GHOSH', 3.0]]
scores =[4.0, 3.0, 2.0, 5.0]
high = 4
scores = filter(lambda x: x != high, scores)
second_low_score = max(scores)
student_data1 = list(filter(lambda x: x[1] ==second_low_score, student_data))
print(list(filter(lambda x: x[1] == 2.0, student_data)))

column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
           ('Bob', 99000, 'data engineer'),
           ('Frank', 87000, 'data analyst')]

db = [dict(zip(column_names, row)) for row in db_rows]
print(db)

exit()
# Reduce
# from functools import reduce   --need this import
print("\nREDUCE:")
print("REDUCE gives single value based on iterable elements")
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"num:{num}")
print("sum using reduce():", reduce(lambda x, y: x + y, num))
print("avg using reduce():", reduce(lambda x, y: (x + y) / 2, num))
print("min using reduce():", reduce(lambda x, y: x if x < y else y, num))
print("max using reduce():", reduce(lambda x, y: x if x > y else y, num))
print("multiplication using reduce():", reduce(lambda x, y: x * y, num))
print("sum using reduce():", reduce(lambda x, y: x + y, num))
print("sum using reduce() with initial value (100):", reduce(lambda x, y: x + y, num, 100))
print("sum using reduce() with initial value 100 (works as default output, if iterable is empty):",
      reduce(lambda x, y: x + y, [], 100))

print("\n\nARGS and KWARGS (key named args")
print("Put *any_var and that becomes pointer to take any number of arguments (0 or more)")
print(
    "If you have any positional arguments (any arg without *) it has to be first and *args should be the last param\n")
print("PARAM ORDER IS: positional_args, *args and then **named_args (kwargs):")


def custom_sum(a, b, *args):
    print(f'a- {a} b-{b} args-{args}')


# print(custom_sum()) # TypeError: custom_sum() missing 2 required positional arguments: 'a' and 'b'
custom_sum(3, 5)
custom_sum(4, 5, 6, 8, 9, 10)


def my_sum(*anyargs):
    if anyargs:
        return sum(anyargs, 0)


print(my_sum())  # If no return value, print shows 'None'
print(my_sum(5))
print(my_sum(5, 7, 8))

'''
def trythis(*a, b): # Wrong def. positional arg cannot come after *args
    print(f'a={a} b={b}')


print(trythis(1, 2))
print(trythis(1, 2, 3))
'''
print("Usage of *arg in unpacking. Here we can have *param at any position")
x, y = (12, 17)
print(f'x:{x} y:{y}')
# x, y = (1,2,3) # ValueError: too many values to unpack (expected 2)
x, y, *any = (1, 2, 3, 4, 5, 6, 7)
print(f'x:{x} y:{y} any:{any}')
x, y, *any, h = (1, 2, 3, 4, 5, 6, 7)  # *a, b, *c --not allowed. Only one starred expression allowed in assignment
print(f'MAGIC-- x:{x} y:{y} any:{any} h:{h}')

print("\n QWARGS --named arguments (parameters)")


def create_person(name, age, gender, **extra_args):
    Person = {
        "name": name,
        "gender": gender,
        "age": age
    }
    print(f"extra_args= {extra_args} and Person={Person}")


create_person("Milind", "22", "Male")
create_person("Milind", "22", "Male", new_property="property_value", randomName="dsgdhsgdh")
create_person(gender="male", name="Milind", age="67")
create_person(gender="male", name="Milind", age="67", new_property="property_value", randomName="dsgdhsgdh")


def create_person(name, age, gender, **extra_args):
    Person = {
        "name": name,
        "gender": gender,
        "age": age
    }
    if extra_args:
        Person.update(extra_args)
    print(f"extra_args= {extra_args} and Person={Person}")


create_person("Milind", "22", "Male")
create_person("Milind", "22", "Male", new_property="property_value", randomName="dsgdhsgdh")
create_person(gender="male", name="Milind", age="67")
create_person(gender="male", name="Milind", age="67", new_property="property_value", randomName="dsgdhsgdh")


def random_func(x, a=100, *n, **z):
    print(f'x={x}')
    print(f'a={a}')
    print(f'n (args are collected as tuple)={n}')
    print(f'z (qwargs are collected as dictionary {{}})={z}')


print("\nPARAM ORDER IS: positional_args, *args and then **named_args (qwargs): (x, *n, **z)")
print(" *args is collected as tuple (), and **qwargs is colleted as dictionary {} ")
random_func(1, 2, 3, 4, 5, 6, name="Milind", age=89, hobbies="Drawing and Swimming")
# random_func(1, 2, 3, 4, 5, a=6, name="Milind", age=89, hobbies="Drawing and Swimming") # TypeError: random_func() got multiple values for argument 'a'
# random_func(my_prop=12, 1,2,3,4,5,6, name="Milind", age=89, hobbies="Drawing and Swimming") # SyntaxError: positional argument follows keyword argument
# random_func(1, name="Milind",2,3,4,5,6, age=89, hobbies="Drawing and Swimming") # SyntaxError: positional argument follows keyword argument

array = [[1, [[2]], [[[3]]], [[4], 5]]]
result = lambda x: sum(map(result, x), []) if isinstance(x, list) else [x]
print(result(array))
