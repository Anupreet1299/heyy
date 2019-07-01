import pandas as pd

numbers = [10,20,30,40,50]
s1 = pd.Series(numbers)

print(s1)

print()


ages = {"john":20, "jennie": 30, "jim":40, "jack":50, "joe":60}
s2 = pd.Series(ages)
print(s2)

print()

#access elements

print(s1[0])

print(s2["jennie"])
print("==============")
#slice elements
print(s1[1:])
print()
print(s1[:3])

print()
print(s1[2:5])

print()
print(s2["jim":])
print(s2["jim":"joe"])  #joe will be inclusive