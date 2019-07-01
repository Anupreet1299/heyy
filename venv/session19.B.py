#r programming language
import pandas as pd
import numpy as np
"""
pandas has two datastructures 
1. series : 1D array
2. data frames : 2D array (tables)


"""

#object construction statements
series = pd.Series()
frame = pd.DataFrame()

print(series)
print(frame)


print(type(series))
print(type(frame))


#list

numbers = [10,20,30,40,50]

array = np.array([11,22,33,44,55])

print(numbers)
print(array)


#panda series


hey = pd.Series([10,20,30,40,60])
print(hey)


hey = pd.Series(numbers)
print(hey)