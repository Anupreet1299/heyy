"""
relationship mapping
HAS-A mapping
teacher
    name
    phone
    email

subject
 name
:::::::::::

customer
     name
     phone
     email

address
    adrsline
    city
    state


"""


class Customer:
    #constructor for standardisation
     def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone

     #function:update operation

    def updateCustomerDetails(self):
        self.name = name
        self.email = email
        self.phone = phone
    #function :read operation

    def showCustomerDetails(self):
        print("name:", self.name)
        print("email:", self.email)
        print("phone:", self.phone)




