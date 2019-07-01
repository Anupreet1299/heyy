import numpy as np

arr1 = np.arange(10,21)
print(arr1)


arr2 = np.arange(10,31, 3)
print(arr2)


arr3= np.ones((3,3,3) , dtype=int)
print(arr3)

arr4 =np.linspace(0,21,4)
print(arr4)

arr = np.arange(10,51,3)
print(arr ,type(arr))
print(arr.shape)
print(arr[1])
print(arr[-1])

#slicing

print(arr[:-3])

slices = slice(1,20,2)
print(slices)
print(arr[slices])


arr2d = np.array([(1,2,3),(3,4,5),(6,7,8)])

print(arr2d[0,1])
print(arr2d[0:2, 0:2])



arr3d = np.array([[(1,2,3),(3,4,5),(6,7,8)]])
print(arr3d)

print(arr3d[0:2, 0:2,0:2])
