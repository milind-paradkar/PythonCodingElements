import MyMathModule as my


class Parent:
    parentProp = 'Parent Property'
    __privateParentProp = 'Private Parent Property'


class MyClass(Parent):
    pubMember = ''
    __privateMember = ''

    def __init__(self, m):
        self.member = m
        self.__privateMember = '__privateMember'
        self.__privateParentProp = '__privateParentProp changed'
        print("In init dunder:", self.parentProp, self.__privateParentProp, self.member, self.__privateMember, sep=', ')

    def __str__(self):
        return f"This is My class with __privateMember:{self.__privateMember} and more.."

    # __add__ works as operator overloading in C++ for add ( obj1 + obj2)
    def __add__(self, other):
        return self.parentProp + other.parentProp


m = MyClass('Milind')
m.member = 'Shruti'
m.pubMember = 'Athawale'
m.parentProp = 'HHHHHHHHH'
m.__privateParentProp = 'private member'  # How's this possible to change value of private member outside class
print(m.parentProp, m.member, m.pubMember,
      sep='\n')  # AttributeError: 'MyClass' object has no attribute '__privateMember' and AttributeError: 'MyClass' object has no attribute '__privateMember'
print("In init dunder:", m.parentProp, m.member,
      sep=', ')  # Unresolved attribute reference '_Parent__privateParentProp' for class 'MyClass' and Unresolved attribute reference '_MyClas__privateMember' for class 'MyClass'
my.my_add()

print(my)
print(m)
print("m + m:" + (m + m))

print("TODO: Implement +,-,*,/,<,>,<=,>= for class")
'''
#Implement +,-,*,/,<,>,<=,>= dunders for class
print(obj1 + obj2)
print(obj1 - obj2)
print(obj1 * obj2)
print(obj1 < obj2)

#How to add obj + value
print(obj1 + 4)
print(4 + obj2)
'''


# Python supports multiple inheritance
class A:
    a = 'a'


class B(A):
    b = 'b'


class C(A):
    c = 'c'


class D(B, C):
    d = 'd'


dObj = D()
print("Obj properties:", dObj.a, dObj.b, dObj.c, dObj.d)


class SchoolMember:
    def __init__(self, name):
        self.name = name


class Student(SchoolMember):  # Student is inherited from SchoolMember
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Staff(SchoolMember):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Teacher(Staff):

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department


t = Teacher("Teacher name", 20000, "Maths")
