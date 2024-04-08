import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)
print(type(arr))
#checking numpy version
print(np.__version__)
arrs = np.array(42)
print(arrs)
c =np.array([1,2,3,4,5])

#create a 2d array containing two arrays with the values 1,2,3 and 4,5,6
b = np.array([[1,2,3],[4,5,6]])

#create a 3d array with two 2d arrys
a=np.array([[[1,2,3],[4,5,6]],[[1,4,9],[16,25,36]]])
print(c.ndim)
print(b.ndim)
print(a.ndim)

#Array Indexing of 1-D arrays
arr1 = np.array([1,2,3,4,5])
print(arr1[3])
print(arr1[2]+arr1[4])
#Accessing 2-D arrays
#think of 2D array like a table with rows and columns, where the 
#dimension represents the row and the index represents the column
arr = np.array([[1,2,3,4,5],[4,5,6,7,8]])
print('2nd element of 1st row',arr[0,1])
print('5th element of 2nd row',arr[1,4])
#Accessing 3D arrays
 
#slicing
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
#So, if you visualize the array [1, 2, 3, 4, 5, 6, 7], counting from the end, -1 refers to 7,
#-2 refers to 6, -3 refers to 5, and so on.
#Therefore, -3:-1 extracts elements 5 and 6.
print(arr[-3:-1])
#step value to determine the step of the slicing
print(arr[1::2])
#slicing 2-D arrays
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])
#From both elements, slice index 1 to index 4 (not included),
# this will return a 2-D array:
print(arr[0:2,1:4])