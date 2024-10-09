import MyMathModule as my


class Parent:
    parentProp = 'Parent Property'
    __privateParentProp = 'Private Parent Property'

    def showPrivateParentProp(self):
        return self.__privateParentProp
class MyClass(Parent):
    pubMember = ''
    __privateMember = ''

    def __init__(self, m):
        self.member = m
        self.__privateMember = '__privateMember'
        self.__privateParentProp = '__privateParentProp changed'
        print("EDITED:In init dunder:", self.parentProp, self.__privateParentProp, self.member, self.__privateMember, sep=', ')

    def __str__(self):
        return f"This is My class with __privateMember:{self.__privateMember} and more.."

    # __add__ works as operator overloading in C++ for add ( obj1 + obj2)
    def __add__(self, other):
        return self.parentProp + other.parentProp


m = MyClass('Milind')
m.member = 'Shruti'
m.pubMember = 'Athawale'
m.parentProp = 'HHHHHHHHH'
print("TODO: What is happening here ?")
m.__privateParentProp = 'private member changed'  # How's this possible to change value of private member outside class
m.parentProp = 'parent property changed'
print(m.showPrivateParentProp(), m.parentProp, m._MyClass__privateMember, m._Parent__privateParentProp, sep=",")  #here it has no effect of above statement but no error on above statement.
m._Parent__privateParentProp =' Private property changed outside also using obj._ClassName__privateProp way'
#print(m.__privateMember, m.__privateParentProp) #This gives error
print(f"Still this works: (Py way of accessing private members): {m._MyClass__privateMember},\nand\n{m._Parent__privateParentProp}, <- I thought this would be same, but, see the difference ->  {m._MyClass__privateParentProp}")
print(m.parentProp, m.member, m.pubMember,
      sep='\n')
print("Hi .. 9999 :", m.parentProp, m.member,
      sep=', ')
my.my_add()
print(my)
print(m)
dir(m)
print("dir(m):", dir(m))
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



class SchoolMember:
    def __init__(self, name):
        self.name = name


print("\nIf we define any function using def in normal scenario, all params are explicit. Like param1, param2.")
print("But when function is defined in class, it expects at least one param. First param for any function is object of own class.")
print("Or even for function def myfunc(a, b, c), a is self object and you have to call only myObj.myfunc(b, c). Here myObj is passed as param 'a' automatically.\n")
class Student(SchoolMember):  # Student is inherited from SchoolMember
    def __init__(self, name, grade):
        self.grade = grade
        #self.name = name   #No need to call this explicitely

        #No need to call super() as first statement in __init__() like in Java
        #self is sent automatically
        super().__init__(name)

class Staff(SchoolMember):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


class Teacher(Staff):

    def __init__(self, name, salary, department):
        self.department = department
        super().__init__(name, salary)
        if super() is not None:
            pass

    def myFunc(obj, g,j):
        print(g)

t = Teacher("Teacher name", 20000, "Maths")
print(t.name, t.salary, t.department)
t.myFunc(3,4)

