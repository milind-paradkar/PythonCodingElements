# Python supports multiple inheritance

class Base:
    def __init__(self, p1):
        self.baseProperty = p1


class Derived(Base):
    def __init__(self, p1, p2, p3):
        super().__init__(p1)  # Without this statement, we will get this error: AttributeError: 'Derived' object has
        # no attribute 'baseProperty' because, super class attributes are not automatically created unless __init__()
        # is called on super()
        self.derivedProperty = p2
        self.__privateProp = p3  # By adding __ to any prop, we are making it private.
        # Unresolved attribute reference '__privateProp' for class 'Derived'


d1 = Derived(6, 7, 10)
d1.derivedProperty = 7889876  # I can change attributes of class even outside of class def. there is no security.
print("d1.derivedProperty:", d1.derivedProperty)
print("d1.baseProperty:", d1.baseProperty)
# print("", d1.__privateProp)



class simple:
    a = 1  # Class level variable
    b = 2
    dList = [5, 6, 7]

    def __init__(self, cParam, eList):
        self.c = cParam  # instance level variable
        self.eList = eList

    def method(self):
        print("Method()")

    def method(self, a):
        print("Method(", a, ")")


s1 = simple(5, [1, 2, 3])
s2 = simple(7, [4, 5, 6])
s1.a = 10
s2.b = 35
s2.dList.append(65)  # class level mutable object changes for all instances
s2.eList.append(38)  # object level mutable object changes only for that instance
s1.c = 76
s1.d = 1777
print(s1.a, s1.b, s1.dList, s1.eList, s2.a, s2.b, s2.dList, s2.eList, s1.c, s2.c, s1.d)


#print("There is NO method overloading in Python?", s1.method(), s1.method(1) )

class A:
    a = 'a'
    print("Random statement called, just for fun! outside of any def")

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        if type(other) == int:
            return self.x + other
        elif type(other) == A:
            return self.x + other.x


print("Type of Class:", type(A), type(A(4)), isinstance(A(2), A))


class MoreDunders:
    def __myOwn__(self):
        print("My own dunder function")


m = MoreDunders()
m.__myOwn__()

a1 = A(2)
a2 = A(3)

print(a1 + 25, a1 + a2, a1 + a2 + 100)
print("I can do a1 + 3, but cannot do 3 + a1. Error we get is TypeError: unsupported operand type(s)"
      " for +: 'int' and 'A'  ")


class B(A):
    b = 'b'
    print("Am I class?")

    def __init__(self, x, y):
        self.y = y
        super().__init__(x)


class C(A):
    c = 'c'

    def __init__(self, x, z):
        self.z = z
        super().__init__(x)


class D(B, C):
    d = 'd'

    def __init__(self, x, y, z):
        super().__init__(x, z)  #Will call first inherited class's init which is in this case, class B, so z will be passed to y in class B. (not to z in class C)
        B.__init__(self, x, y)  #See the difference. super() passes self automatically, but CLASSNAME.__init() requires self to be passed explicitly.
        C.__init__(self, x, z)
        self.z = z


print("Execution starts! Before dObj creation.")
dObj = D(1, 2, 3)
print("Obj properties:", dObj.a, dObj.b, dObj.c, dObj.d, dObj.x, dObj.y, dObj.z)
print(f"MRO:{D.__mro__}\n")


class A:
    x = 10
    print("print statement called.")


class B(A):
    pass


class C(B):
    pass


class D(A):
    x = 5


class E(C, D):
    pass


e = E()
e1 = E()
print("1] E.__mro__:", E.__mro__)
print("x:", e.x)


class A:
    pass


class B(A):
    x = 10


class C(B):
    pass


class D(A):
    x = 5


class E(C, D):
    pass


e = E()
print("2] E.__mro__:", E.__mro__)
print("x:", e.x)


class A:
    pass


class B(A):
    pass


class C(B):
    x = 10


class D(A):
    x = 5


class E(C, D):
    pass


e = E()
print("3] E.__mro__:", E.__mro__)
print("x:", e.x)
print("Conclusion: From __mro__ when we go from L2R, value gets picked (precedence) from the class that comes first. ")

print("\nRule for __mro_")
print("Rule 0] Start with current class.")
print("Rule 1] Left path first, right path later.")
print("Rule 2] All children need to be covered before the parent.")

#Refer diagram Multiple-Inheritance-__mro__-complex-diagram1.PNG
print()
print("Refer diagram Multiple-Inheritance-__mro__-complex-diagram1.PNG")
print("__mro__ : N,L,F,C,E,D,B, M,K,I,J,H,G,A ")

print(f"gives memory location of object by id(): {id(e)} and {id(B)}")


class A:
    x = 1


class B:
    x = 2


class C:
    x = 3


class D(A, B, C):
    pass


d = D()
help(d)
print(D.__mro__)
print(d.x)
