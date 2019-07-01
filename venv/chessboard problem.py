#creation of chessboard

import numpy as np

ch = np.zeros((8,8))

for i in range(8):
    for j in range(8):
       ch[i,j] = (i+j)%2
print(ch)


#add four queens from the user

for q in range(0,4):
    queenPosition =input("where to place the queen:")
    i = int(queenPosition[0])
    j = int(queenPosition[2])
    

    print(ch)
