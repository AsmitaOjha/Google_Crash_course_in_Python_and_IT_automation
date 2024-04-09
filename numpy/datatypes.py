#changing data type from float to integer by using 'i' as parameter value:
import numpy as np
arr = np.array([1.1,2.1,3.1])
print(arr.dtype)
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

#change data type from float to integer by using int as parameter value:
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

#change data type from integer to boolean:
import numpy as np
arr = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

