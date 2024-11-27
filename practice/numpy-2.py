import numpy as np

npa = np.arange(16)
npa1 = npa.reshape(4, 4)
print("npa=", npa, sep='\n')
print("npa reshaped=", npa1, sep='\n')
print("npa reshaped=", npa.reshape(8, 2), sep='\n')
# print("npa reshaped=",npa.reshape(5,3), sep='\n') # ValueError: cannot reshape array of size 16 into shape (5,3)
print("npa reshaped=", npa.reshape(4, -1), sep='\n')
print("npa reshaped=", npa.reshape(-1, 2), sep='\n')
print()
print(npa, "size", npa.size, len(npa), npa.ndim, npa.shape, sep='\n', end='\n')
print()
print(npa.reshape(2, -1), "size", npa.reshape(2, -1).size, len(npa.reshape(2, -1)), npa.reshape(2, -1).ndim,
      npa.reshape(2, -1).shape, sep='\n', end='\n')
print()
print(npa.reshape(8, -1), "size", npa.reshape(8, -1).size, len(npa.reshape(8, -1)), npa.reshape(8, -1).ndim,
      npa.reshape(8, -1).shape, sep='\n', end='\n')
print()
print(npa.reshape(2, 4, -1), "size", npa.reshape(2, 4, -1).size, "len", len(npa.reshape(2, 4, -1)), "ndim",
      npa.reshape(2, 4, -1).ndim, "shape",
      npa.reshape(2, 4, -1).shape, sep='\n', end='\n')
print()
print(np.arange(15).reshape(-1, 5))
print("npa.T --> .T shows Transpose\n", np.arange(15).reshape(-1, 5).T)
print(np.arange(15).reshape(-1, 5)[2][3])
print("is same as")
print(np.arange(15).reshape(-1, 5)[2, 3])
print()
print("npa[[0, 0, 1, 2], [0, 2, 2, 4]] = npa[[x series],[y series]]= "
      "gives array series [[x1,y1], [x2, y2], [x3, y3]..] =",
      np.arange(15).reshape(-1, 5)[[0, 0, 1, 2], [0, 2, 2, 4]])
print()
print("npa:", npa1, sep='\n')
print("\n Slicing (by default works on first dimension-rows here): npa1[1:3]:", npa1[1:3], sep='\n')
print("Slicing on second dim:\n", npa1[:, 2:])
print("Slicing on second dim:\nOriginal:\n", npa1, "\nSlicing npa1[2:, 2:]:\n", npa1[2:, 2:])
print()
print("reverse:\n", npa1[::-1])
print()
print(npa1[::-1, ::-1])
print("Transpose:\n", npa1[::-1, ::-1].T)
print("\n", npa1[::-1, ::-2])
print()
print(f"M A S K I N G in multi-dimensional array (gives all elements -not arranged in terms of dimensions)"
      f"\n npa1:\n{npa1} \nnpa1 < 6:\n{npa1 < 6} \n\nnpa1[npa1<6]:\n{npa1[npa1 < 6]}")

print("Aggregate Functions")
print("min, max, average, etc", npa.min(), npa1.max(), npa1.mean(), npa1.sum())
print()
a = np.arange(12).reshape(3, 4)
print(a)
print("a.sum(), a.sum(0) -row wise sum?, a.sum(1) -column wise sum:", a.sum(), a.sum(0), a.sum(1))
print("a.sum(),  np.sum(a, axis=0) -row wise sum?, np.sum(a, axis=1) -column wise sum:", a.sum(), np.sum(a, axis=0),
      np.sum(a, axis=1))
print()
print("np.all() --works like AND. \nnp.any() --works like OR")
prices = np.array([50, 45, 25, 20, 35])
budget = 35
can_afford = np.any(prices <= budget)
print("can_afford:", can_afford)
chores = np.array([1, 1, 1, 1, 0])
print("All chores done:", np.all(chores == 1))
print("Can I afford and all chores done? ", np.any(prices <= budget) and np.all(chores == 1))
print("Can I afford or all chores done? ", np.any(prices <= budget) or np.all(chores == 1))

a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])

print("a < b:", a < b)
print("a < b:", np.all(a < b), (a < b).all())
print("a < b:", np.any(a < b), (a < b).any())

x = np.array([49, 0, 50, 48, 55, 67, 100, 0, 23])
y = np.where(x <= 50, x, x * 0.9)
print(x, y)
print("This is giving indexes of non-zero numbers:", np.where(x))

print("Numpy-2 lencture time: 2:10 -Google link to download "
      "data: https://drive.google.com/uc?id=1vk1Pu0djiYcrdc85yUXZ_Rqq2oZNcohd")



