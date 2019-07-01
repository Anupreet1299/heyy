import numpy as nm

arr1 = nm.array([10, 20, 30, 40, 50])
arr2 =nm.array([[10,20,30],[40,50,60],[70,80,90]])

print(arr1, type(arr1))
print(arr2, type(arr2))


print(len(arr1))
print(len(arr2))

print(arr1[1])
print(arr2[1][2])


print("arr1 shape is :", arr1.shape)
print("arr2 shape is :", arr2.shape)

#if arr2 is irregular array like
arr2 =nm.array([[10,20],[40,50,60, 79],[70,80,90,78, 43]])
#then the shape will be
print("arr2 shape is :", arr2.shape)


print()


a1 =nm.ones(8)
print(a1)

a2 =nm.zeros(9)
print(a2)

print(a1.shape)

print(a1.reshape(2,2,2))

print(a1.ravel())