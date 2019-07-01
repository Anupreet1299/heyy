"""
student
    name


no standardization
solution:constructor

"""

class student:
#self is reference variable which will hold hashcode of current object
#__init__ is know as constructor
#constructor is property of class
    def __init__(self, name, phone, email, password, isCollegeTraining, collegeName, rollNum):
        print(">> self is:", self)
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.isCollegeTraining = isCollegeTraining
        self.collegeName = collegeName
        self.rollNum = rollNum

s1 = student("John", "+91 98878 34322", "john@example.com", "pass123", "true", "ABC ", "    " )

