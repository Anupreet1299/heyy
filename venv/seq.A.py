technologies = ["AI","android", "hadoop", "Jee"]
technologies[1]= "mobile apps"

print(technologies)

del technologies[2]

#print(technologies[0:-2])
"""
data = [1, 2, 3, 4, 5, "john", "jim"]
data.pop(3)  #removes on the basis of index
print(data)

data.remove(3) #removes the matching element
print(data)

data.remove("john")
print(data)
"""

#length of data
data = ["java", "c++", "c"]
print(len(data))
print(max(data) )
print(min(data))


#iterate in list
for i in range(len(data)):
    print(data[i])

print()
print()
#enhanced for loop / for each loop

for kuchbhi in data:
    print(kuchbhi)