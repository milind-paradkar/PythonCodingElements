import numpy as np

a = [1,2,3,4,5,6]
npA = np.array(a)
print(npA)
print("A list can have heterogeneous datatypes. Numpy array is homogeneous data only (only one datatype). Continuous "
      "data storage in memory.")
print("All properties/functions available in list can be used in np array.\n")
print(npA[1:4])
print("Most operations are allowed to executed on np array itself and results in performing on each element:\n", npA ** 2, sep='')
print(npA ** 3)
print(npA + 3)
print(npA < 3)
print(type(npA), "numpy n dimension array")

print(np.array(['1','2','366']))
'''
t = ()
print(type(t))
l = []
for i in range(1,1000,2):
    l.append(i)

t = tuple(l)
'''
nmt = np.array(range(1,1000,2))
print(nmt)
nparr = np.arange(10,90,10)
print(np.arange(1,10,2))
print("Using np.arange() gives np array instead of range() which gives simple list (not numpy array):", nparr)
print(nparr.astype(float))
print(nparr.astype('float'))
print(nparr.astype('str'))

g = nparr[3]
j = nparr[[0,1,3,7]]  #  creating np array out of random indexes. This is not possible with simple list []
print("g:",g, "creating np array out of multiple indexes. This is not possible with simple list [] - j:", j)

exit(0)
d1 = nm.array([3,7,3,6,2,56,325,3])
d2 = nm.array([[3,7,3,7],[8,6,5,4]])
# d3 = nm.array([[3,9],[7,4]],[[4,9],[9,6]])

print(f"d1: dimension:{d1.ndim}, shape:{d1.shape}")
print(f"d2: dimension:{d2.ndim}, shape:{d2.shape}")
# print(f"d3: dimension:{d3.ndim}, shape:{d3.shape}")


l = [1,2,3,4,0,8,-8, "a", 'b', '0', '1', '-1']
lnp = np.array(l, dtype=bool)
print(lnp)

