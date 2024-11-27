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
m1 = np.array([ [[34, 20, 39], [101, 22, 23], [27, 55, 79]], [[4, 10, 19], [1, 12, 3], [7, 5, 9]] ])
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





print("\n---Whole execution completed in %s seconds ---" % (time.time() - start_time))
