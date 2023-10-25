import numpy as np

# ------------------------------ Create NDArray ------------------------------ #
# l = [
# 	[1,2,3],
# 	[4,5,6],
# 	[7,8,9]
# ]

# ndarr = np.array(l)

# print(l)
# print(ndarr)

# ----------------------------------- Types ---------------------------------- #

# arr1 = np.arange(1,11, dtype=np.float32)
# print(arr1.dtype)
# print(arr1)

# -------------------------------- Array Shape ------------------------------- #
# l = [
# 		[1,2,3],
# 		[4,5,6],
# 		[7,8,9]
# ]



# arr2d = np.array(l, dtype=np.byte)
# print(arr2d)
# print(arr2d.shape)
# print(len(arr2d.shape))


# arr1d = np.arange(1,9)
# print(arr1d)
# print(arr1d.shape)
# print(arr1d.ndim)

# arr2d = arr1d.reshape(3,3)
# print(arr2d)
# print(arr2d.shape)
# print(arr2d.ndim)


# arr3d = np.arange(1,13).reshape(2,3,2)
# print(arr3d)


# ---------------------------------- Resize ---------------------------------- #

# arr1d = np.arange(1,10)
# # print(arr1d.shape)
# # arr2d = np.resize(arr1d, (12,))

# # TODO: DONE (https://numpy.org/doc/stable/reference/generated/numpy.ndarray.resize.html)
# arr2d = arr1d.resize(12)
# print(arr2d)

# --------------------------------- Linspase --------------------------------- #
# arr = np.linspace(1,100,num=10)
# print(arr)

# ----------------------------------- Full ----------------------------------- #
# matrix = np.full((3,3),9)
# print(matrix)

# --------------------------------- Indexing --------------------------------- #
# l = [
# 	[1,2,3],
# 	[4,5,6],
# 	[7,8,9]
# ]

# arr2d = np.arange(1,10).reshape(3,3)

# print(arr2d)

# print( l[1][2] )

# print(arr2d[1][2]) # NEVER DO THAT
# print(arr2d[1,2]) # DO THIS

# ---------------------------------- Slicing --------------------------------- #
# arr2d = np.arange(1,10).reshape(3,3)
# print(arr2d)
# print( arr2d[0, 0:-1])
# print( arr2d[:,0])
# print( arr2d[:,0:2])

# --------------------------- Arithmetic Operations -------------------------- #
# All Operations in numpy arrays are POINT-TO-POINT (ELEMENT WISE):
# l1 = [1,2,3]
# l2 = [4,5,6]

# print(l1+l2)

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# print(arr1+arr2)
# print(arr1**arr2)

# arr1 = np.array([1,2,3])
# print( arr1 + 10)

# ---------------------------- Statistic Functions --------------------------- #
# arr1 = np.array([1,2,3])
# print( arr1.mean()) #2

# ---------------------------- Boolean Operations ---------------------------- #
# arr1 = np.arange(1,7).reshape(2,3)
# # [[1 2 3]
# #  [4 5 6]]

# print(arr1<3)

# [[T T F]
#  [F F F]]

# ---------------------------- Logical Operations ---------------------------- #
### where

# arr1 = np.arange(1,7).reshape(2,3)
# print(arr1)

# arr2 = np.where(arr1<3, arr1**2, arr1**3)
# print(arr2)


# arr1 = np.array([True,True,False])
# arr2 = np.array([False,False,False])

# # print(arr1 or arr2)
# print(np.logical_or(arr1,arr2))










