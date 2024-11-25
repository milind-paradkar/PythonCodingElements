import numpy as np

a = [1, 2, 3, 4, 5, 6]
npA = np.array(a)
print(npA)
print("A list can have heterogeneous datatypes. Numpy array is homogeneous data only (only one datatype). Continuous "
      "data storage in memory.")
print("All properties/functions available in list can be used in np array.\n")
print(npA[1:4])
print("Most operations are allowed to executed on np array itself and results in performing on each element:\n",
      npA ** 2, sep='')
print(npA ** 3)
print(npA + 3)
print(npA < 3)
print(type(npA), "numpy n dimension array")

print(np.array(['1', '2', '366']))

nmt = np.array(range(1, 1000, 2))
print(nmt, "\ntype nmt:", type(nmt))

nparr = np.arange(10, 90, 10)
print("Using np.arange() gives np array instead of range() which gives simple list (not numpy array):", nparr)
print("\nnp.arange(1,10,2): ", np.arange(1, 10, 2))
print("np.arange(1,10,0.2) (also accepts floating point step):", np.arange(1, 10, 0.2))
print()

print("np array is HOMOGENIOUS type array:")
print(np.array([1, 2, 3, 4, 5, 6, 7]))
print(np.array([1, 2, 3, 4.2, 5, 6, 7]))
print(np.array([1, 2, 3, 4, 5, '6', 7]))
print(np.array([1, 2, 3, 4, 5, '6', 7, False, True]))
print(np.array([1, 2, 3, 4, 5, 6, 7, False, True, True, False]))
print(np.array([-2, 0, 1, 2, 3, 4, 5, 6, 7, False, True, True, False], dtype=bool))
print("\nFor:", "['0','-1', '1', 'Amit','', '\n', '\t']", "converted to bool:",
      np.array(['0', '-1', '1', 'Amit', '', '\n', '\t'], dtype=bool),
      "Only empty string is converted to False. Everything else is True",
      sep='\n')

print(nparr.astype(float))
print(nparr.astype('float'))
print(nparr.astype('str'))
print()
g = nparr[3]
j = nparr[[0, 1, 3, 7]]  #  creating np array out of random indexes. This is not possible with simple list []
print(f"indexing  np array out of multiple indexes. This is not possible with simple list [] -g:{g}  np array- j:{j}\n")

print("numpy also supports element replacement using slicing:")
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
nl2 = np.array(l2)
print("nl2:", nl2)
# l2[3:] = 0  # Does not work. TypeError: can only assign an iterable
nl2[3:] = 0
print("nl2:", nl2)
nl2[::3] = 77
print("nl2:", nl2)
nl2[[1, 3, 9]] = 88  # selected elements replacement with 88
print("nl2:", nl2)

npa10 = np.array([1,2,3,4,5,6,7,8,9,10])
lstBoolean = [True, False, True, True, True,False,False, True, True,False]
print("*IMP*Fancy indexing/Masking \nThis concept is used in Pandas\nPassing lst of booleans as a index outputs in "
      "showing element only at True. \nnpa10[lstBoolean]:", npa10[lstBoolean]) # IndexError: boolean index did not match
# indexed array  along axis 0; size of axis is 10 but size of corresponding boolean axis is 2
print("npa10[npa10%2 == 0]:", npa10[npa10 % 2 == 0])
print()
print("NPS (Net Promotor Score) = % promotors - % Detractor")
print("If all people are promotors (rated 9-10), we get 100 NPS ")
print("Conversely, If all people are detractors (rated 0-6), we get -100 NPS.")
print("Also, if all are neutral (rated 7-8), we get a 0 NPS")
print("Therefore, the range of NPS lies between [-100,100]")
print("")
print("NPS data link: https://drive.google.com/file/d/1c0ClC8SrPwJq5rrkyMKyPn80nyHcFikK/view?usp=sharing")
print("score = np.loadtxt('survey.txt', dtype ='int')")
print("Lecture Numpy-1, time: 2:15")

print("\nM U L T I   D I M E N S I O N    N P    A R R A Y\n")
d1 = np.array([3, 7, 3, 6, 2, 56, 325, 3])
d2 = np.array([[3, 7, 3, 7], [8, 6, 5, 4]])
l1 = [[3, 9, 8], [7, 4, 3]], [[4, 9, 3], [9, 6, 65]]
d3 = np.array(l1)

print(f"d1:\n{d1} \ndimension .ndim:{d1.ndim} and  .shape:{d1.shape}")
print(f"d2:\n{d2} \ndimension .ndim:{d2.ndim} and  .shape:{d2.shape}\n")
print(f"d3:\n{d3} \ndimension .ndim:{d3.ndim} and  .shape:{d3.shape}\n")
print("Please note, while creating multi dimensional array in np, you cannot use variable lengths within array as this:"
      " [[1,2], [1,2,3]]\n")

l = [1, 2, 3, 4, 0, 8, -8, "a", 'b', '0', '1', '-1']
lnp = np.array(l, dtype=bool)
print(l, lnp, sep='\n')
print(
    f"\nnp array can be accessed by negative indexes also same as pythong lists. Examples:\nd1[-1]:{d1[-1]} \nd2[-1]:{d2[-1]}, \nd3[-1]:{d3[-1]} \n\n")


