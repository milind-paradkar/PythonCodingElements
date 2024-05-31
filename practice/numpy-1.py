import numpy as nm
import numpy as np


def function_1():
    print("third")
    function_2()


def function_2():
    print("second")
    function_3()


def function_3():
    print("first")


function_1()
a = [1,2,3,4,5,6]

print(nm.array(a))
print(nm.array(a) ** 2)
print(nm.array(a) ** 3)
print(type(nm.array(1)), "numpy n dimension array")

'''
t = ()
print(type(t))
l = []
for i in range(1,1000,2):
    l.append(i)

t = tuple(l)
'''
t = tuple(range(1,1000,2))
nmt = nm.array(t)
print(nmt)

b = [(1,2,3,4,5,9), (7,8,9)]
print(b[0][-1]) # To find element 9

nparr = np.arange(10,90,10)
print(nparr)
print(nparr.astype('float'))
print(nparr.astype('str'))

g = nparr[3]
j = nparr[[3,7]]  #  creating np array out of random indexes. This is not possible with simple list []
print("g:",g, "j", j)

d1 = nm.array([3,7,3,6,2,56,325,3])
d2 = nm.array([[3,7,3,7],[8,6,5,4]])
d3 = nm.array([[3,9],[7,4]],[[4,9],[9,6]])

print(f"d1: dimension:{d1.ndim}, shape:{d1.shape}")
print(f"d2: dimension:{d2.ndim}, shape:{d2.shape}")
print(f"d3: dimension:{d3.ndim}, shape:{d3.shape}")





