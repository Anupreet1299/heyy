#import request
#import requests as rq

#rq.post()

#import re  #regular expression

import numpy as np
"""
#list creation

numbers = [10, 20, 30 ,40, 50]
print(type(numbers))
print()
#pass list/ tuple/set/dictionary/string
#newNumbers = {"a": 10, "b":20}
array = np.array([10,20,30,40,50])
print(array, type(array))

#check size

print(len(array))
print()

#update data in array

array[2] = 50
print(array)

array2 = np.append(array , [60, 70, 70])
print(array2)
print()
#iterate in array
for e in array2:
    print(e)

a1 = np.zeros(8)
print(a1)
print(a1.shape)

a2 = a1.reshape(2,2, 2)
print(a1)
print(a2)

a3 = a2.ravel()
print(a3)
"""


#create a chessboard

a1=np.zeros(8)
print(a1)
print(a1.shape)

ch=np.zeros((8,8),dtype=int)
#print(ch)

ch[1::2,::2]=1
ch[::2,1::2]=1
print(ch)

indexes = []

for q in range(0,4):
    queenPosition = input("where to place first queen :")
    i = int(queenPosition[0])
    j = int(queenPosition[2])

    ch[i][j] = 9
    print(ch)















