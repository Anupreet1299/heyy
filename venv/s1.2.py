johnsAge = 30
print( johnsAge,   hex(id(johnsAge)))

jennysAge = 30
print( jennysAge, hex(id(jennysAge)))

#copy operation : reference copy
jacksAge = johnsAge

del johnsAge
#print(jennysAge, hex(id(jennysAge)))
#ps: johnsAge and jennysAge are known as reference variables
print(jacksAge, hex(id(johnsAge)))