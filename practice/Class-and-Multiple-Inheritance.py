# Python supports multiple inheritance
class A:
    a = 'a'
    print("Random statement called, just for fun! outside of any def")
    def __init__(self, x):
        self.x = x


class B(A):
    b = 'b'
    print("Am I class?")
    def __init__(self, x, y):
        self.y = y
        super().__init__(self,x)

class C(A):
    c = 'c'

    def __init__(self, x, z):
        self.z = z
        super().__init__(x)

class D(B, C):
    d = 'd'

    def __init__(self, x, y, z):
        # super().__init__(x) not sure
        B.__init__(self,x,y)
        C.__init__(self, x,z)
        self.z = z

print("Execution starts! Before dObj creation.")
dObj = D(1, 2, 3)
print("Obj properties:", dObj.a, dObj.b, dObj.c, dObj.d, dObj.x, dObj.y, dObj.z)
print(f"MRO:{D.__mro__}\n")

class A:
    x= 10
    print("print statement called.")

class B(A):
    pass

class C(B):
    pass

class D(A):
    x=5

class E(C,D):
    pass

e = E()
e1 = E()
print("1] E.__mro__:",E.__mro__)
print("x:", e.x)


class A:
    pass

class B(A):
    x=10

class C(B):
    pass

class D(A):
    x=5

class E(C,D):
    pass

e = E()
print("2] E.__mro__:",E.__mro__)
print("x:", e.x)

class A:
    pass

class B(A):
    pass

class C(B):
    x=10

class D(A):
    x=5

class E(C,D):
    pass

e = E()
print("3] E.__mro__:",E.__mro__)
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
    x=1

class B:
    x=2

class C:
    x= 3

class D(A, B, C):
    pass

d = D()
help(d)
print(D.__mro__)
print(d.x)