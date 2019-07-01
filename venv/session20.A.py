import pandas as pd

num1 = [10,20,30,40,50]
num2 = [11,22,33,44,55]

emp1 = {"eid":101, "name":"John", "age": 20}
emp2 = {"eid":201, "name":"Fionaa", "age": 22}
emp3 = {"eid":301, "name":"Kia", "age": 24}


df1 = pd.DataFrame([num1,num2])
df2 = pd.DataFrame([emp1,emp2,emp3])

print(df1)
print()
print(df2)


print(df1[0])
print()
print(df2["eid"])  #we will get columns



print(df2["eid"][])