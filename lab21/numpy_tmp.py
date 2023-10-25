import numpy as np


arr1d = np.arange(1,11)
print(arr1d)
# arr2d = arr1d.reshape(3,4)


# TODO:DONE (https://numpy.org/doc/stable/reference/generated/numpy.ndarray.resize.html)
# arr2d = arr1d.resize((3,4))
arr2d = np.resize(arr1d, (3,4))
print(arr2d)