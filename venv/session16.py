print(">> App started")

numbers = [10, 20, 30, 40, 50]
a=10 ; b=3; c=0
c=a//b

print(numbers[3])
print("c is:", c)

print(">>App finished")


#more built in modules

import json    #javascript object notation

employee = {"eid":101, "name":"john", "salary": 30000}

print(employee)
print(type(employee))

#convert dictionary into json

jsonData = json.dumps(employee)
print(jsonData)
print(type(jsonData))


#get the json data ie string format of dictionary
#and convert it into dictionary

dictData = json.loads(jsonData)
print(dictData)
print(type(dictData))