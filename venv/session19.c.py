import numpy as np

arr = np.loadtxt("data.txt")
print(arr)



print("------------")

arr1 = np.arange(10,100,10)
print(arr1)

np.savetxt("arraydata.txt", arr1, fmt="%02d")

print("data written")
