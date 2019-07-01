#automatic = main thread || execution context

#variable arguments
"""
def addNumbers(*args):
    print(args)
    print(type(args))

addNumbers(10,20)
"""

#passing value

num = 10
def show():
    num = 11
    print(">>1. num ")

"""
object oriented programming structure
>object
>class
1. encapsulation
2. abstraction
3. inheritance
4. polymorphism


"""

class User:
    pass
class Driver:
    pass

data = []
print(type(data))

#object construction statement
u = User()
d = Driver()

print(type(u))
print(type(d))

print(u)
print(d)

# write data in object
u.name = "john"
u.phone = "748493"
u.email = "john@example.com"
u.address = "rewood shore"

d.name = "george"
d.phone = "234487"
d.experience ="3 years"
d.license = "wy443"


