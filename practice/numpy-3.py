import numpy as np
import time

start_time = time.time()
ctr = 1


def prln(*kwargs):
    global ctr
    print(f"[{ctr}]:\n", *kwargs, "\n", sep='')
    ctr = ctr + 1


prln("Numpy-3 ")
a = np.array([10, 13, 15, 5, 2, 5, 3, 9, 8, 3, 5, 6])
b = np.sort(a)
prln("np.sort() need to store new array to see effect", a, b)
a.sort()
prln("a.sort() sorts np array inline:", a, b)

m = np.array([[4, 10, 19], [1, 12, 3], [7, 5, 9]])
prln("m:\n", m)
# m.sort()  # Sorts in-line and gives None back if called in print()
mSorted = np.sort(m)
prln("m.sort():\n", mSorted)
m1 = np.array([[[34, 20, 39], [101, 22, 23], [27, 55, 79]], [[4, 10, 19], [1, 12, 3], [7, 5, 9]]])
prln("m1:\n", m1)
m1Sorted = np.sort(m1)
prln("m1.sort(): Sorted inner most array\n", m1Sorted)

prln("Testing for Axis for sorting:")
prln("m:\n", m)
mSorted = np.sort(m, 0)
prln("m.sort(axis=0): Called as row wise sorting (elements are sorted row wise- "
     "elements in one row are considered for sorting)- item is not moved across column- for 2D array\n", mSorted)

prln("m1:\n", m1)
m1Sorted = np.sort(m1, 0)
prln("m1.sort(axis=0): Sorted outer most array for 3D. "
     "multiple 2D arrays are sorted (shifted) while keeping 2D arrays as it is.\n", m1Sorted)

prln("m:\n", m)
mSorted = np.sort(m, 1)
prln("m.sort(axis=1): Called as column wise sorting (elements are sorted (shifted) column wise- "
     "elements in one column are considered for sorting) -row for item does not interchange for 2D array\n", mSorted)

prln("m1:\n", m1)
m1Sorted = np.sort(m1, 1)
prln("m1.sort(axis=1): For 3D array, outermost array sequence remained same. "
     "2D arrays are sorted (shifted) row wise while keeping columns as it is.\n", m1Sorted)

print("Visual Demo of Matrix Multiplication: https://www.geogebra.org/m/ETHXK756")
print()
a = np.array([2, 4, 5, 6, 7])
prln("a=", a, " a * 5 --multiply all elements by 5 for np array=", a * 5)
b = np.array([2, 3, 4, 5, 2])
prln("b=", b, "a * b --multiply a with b element wise=", a * b)

prln("Mathematical Matrix multiplication:")
print("When matrix multiplication of m X n and n X o is done, output is m X o matrix")
m = np.arange(1, 16).reshape(3, 5)
n = np.arange(1, 16).reshape(5, 3)
prln(f"m=\n{m}\nn=\n{n}\n\n m dot n=\n", m.dot(n))
prln(f"m=\n{m}\nn=\n{n}\n\n m matmul n=\n", np.matmul(m, n))
prln(f"m=\n{m}\nn=\n{n}\n\n m @ n (short cut, internally uses matmul)=\n", m @ n)
prln(f"m.dot(5):\n{m.dot(5)}\n"
     f"m @ 5:          --ValueError: matmul: Input operand 1 does not have enough dimensions (has 0, gufunc core with"
     f" signature (n?,k),(k,m?)->(n?,m?) requires 1) \nnp.matmul(m,5): --ValueError: matmul: Input operand 1 does not "
     f"have enough dimensions (has 0, gufunc core with signature (n?,k),(k,m?)->(n?,m?) requires 1)")

prln("V e c t o ri s a t i o n")


def random_operation(x):
    if x % 2 == 0:  # This is expected as True or False. When np array is passed, it becomes like [true, False, True, False]
        x -= 2
    else:
        x += 2
    return x


print("random_operation:", random_operation(3))
print("random_operation:", random_operation(4))
# print("random_operation:", random_operation([4, 4, 5 ])) # Does not work on simple list
print("This works, so expected that below also works:", np.array([4, 4, 5]) % 2, np.array([4, 4, 5]) % 2 == 0)
print("But random_operation(np.array([4, 4, 5])) gives error when evaluating if condition: --ValueError: The truth"
      " value of an array with more than one element is ambiguous. Use a.any() or a.all()"
      "\nReason: 'if' expected as True or False. When np array is passed, it becomes like [true, False, True, False]")

print("To solve this, use np.vectorize() to make your function READY to accept np array.")
np_random_operation = np.vectorize(random_operation)
prln(np_random_operation(np.array([2, 4, 5, 10])))
prln(np_random_operation(np.array([[2, 4], [5, 10]])))
prln(np_random_operation([2, 4]), "\nType:", type(np_random_operation([2, 4])))
prln(np_random_operation([[2, 4], [4, 7]]), "\nType:", type(np_random_operation([2, 4])),
     " <--BECAUSE, this is vectorized function, normal list is also converted to np array.")
prln("type(random_operation):", type(random_operation), "\ntype(np_random_operation):", type(np_random_operation))

prln("B r o a c a s t i n g")
prln("np.tile. This is used internally for broadcasting..")
a = [1, 2]
prln(a, '\n', np.tile(a, (3, 1)))
prln(a, '\n', np.tile(a, (1, 3)))
prln(a, '\n', np.tile(a, (3, 3)))

a = np.array([1, 2, 3, 4, 5, 6, 7])
b = np.array([[10, 20, 30, 40, 50, 60, 70],
              [100, 200, 300, 400, 500, 600, 700],
              [10, 20, 305, 40, 560, 620, 770],
              [10, 20, 30, 40, 50, 60, 70]])
prln("When using operations on np array such as +, -, ect.. it tiles (replicates)"
     " elements automatically to match bigger element. This is called broadcasting\n", "a:", a, "\nb:\n", b,
     "\na + b:\n", a + b)
x = [1, 2, 3, 4, 5]
y = [[10]]
prln(f"x:{x}\ny:\n{y}\nx + y:\n{x + y}")
y = [[10], [20]]
prln(f"x:{x}\ny:\n{y}\nx + y:\n{x + y}")
y = [[10], [20], [30]]
prln(f"x:{x}\ny:\n{y}\nx + y:\n{x + y}")

x = np.array([1, 2, 3, 4, 5])
y = np.array([[10]])
prln(f"Broadcast:\nx:{x}\ny:\n{y}\nx + y:\n{x + y}")
y = np.array([[10], [20]])
prln(f"Broadcast:\nx:{x}\ny:\n{y}\nx + y:\n{x + y}")
y = np.array([[10], [20], [30]])
prln(f"Broadcast:\nx:{x}\ny:\n{y}\nx + y:\n{x + y}")

prln("So, when nd array of size: (8,1,6,1) is operated with (7,1,5), it broadcasts well because it is treated as ")
print("(8,1,6,1) and")
print("(1,7,1,5)")
print("because any array of size for example 8 is always treated as (1,8) or (1,1,8) or (1,1,1,8) while expanding.")
print()
n = np.arange(15).reshape(15,1)
print(n)
print("What this is doing? -->\n", n[:,None])

print()
print("On DELL: 0.01267695426940918 seconds")
print("On DELL: 0.01288294792175293 seconds")
print("On DELL: 0.014171361923217773 seconds")
print("\n---Whole execution completed in %s seconds ---" % (time.time() - start_time))
