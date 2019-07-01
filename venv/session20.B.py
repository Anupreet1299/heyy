import pandas as pd

table = pd.read_csv("temperature.csv")
print(table)

print("===============================")

print(table["Year"])

print("===============================")


print(table.iloc[3])
print("===============================")

print(table.iloc[1:5])

print("=============HEAD==================")

print(table.head(5))

print("=============TAIL==================")

print(table.tail(3))