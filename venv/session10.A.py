class parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print(">> parent constructor executed")

    def showDetails(self):
        print(">>hello, ",self.fname, self.lname)


class child(parent):
    def __init__(self, vehicle, salary):
        self.vehicles = vehicles
        self.salary = salary
        print(">>Child constructor executed")

print("parent class dictionary:" ,parent.__dict__)
print("child class dictionary:", child.__dict__)

ch = child("john", "watson")
print(ch.__dict__)
ch.showDetails()


