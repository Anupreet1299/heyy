"""
database

myphp admin

1. create database
    creation of tables
    tables can be related to each other
2. create tables in database





5.

"""
import mysql.connector


# DAO : Data Access Object
class DBHelper:

    def saveCustomerInDB(self, customer):

        # 1. Create SQL Statement
        sql = "insert into customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)

        # 2. Create Connection with Database
        con = mysql.connector.connect(user="root", password="",host="127.0.0.1", database="training")

        # 3. Obtain Cursor ro execute SQL Statements
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

        print(customer.name," Saved !!")

    def updateCustomerInDB(self, customer):
        # 1. Create SQL Statement
        sql = "update customer set name = '{}', phone = '{}', email = '{}' where cid = {}".format(customer.name,
                                                                                                  customer.phone,
                                                                                                  customer.email,
                                                                                                  customer.cid)
        # 2. Create Connection with Database
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="training")

        # 3. Obtain Cursor ro execute SQL Statements
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

        print(customer.name, " Updated !!")

    def deleteCustomerInDB(self, cid):
        # 1. Create SQL Statement
        sql = "delete from Customer where cid = {}".format(cid)
        # 2. Create Connection with Database
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="training")

        # 3. Obtain Cursor ro execute SQL Statements
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

        print(cid, " Deleted !!")


    def fetchAllCustomer(self):


        #1. create sql query
        sql = "select * customers "

        #2. create connection with the database
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="training")
        #3. obtain cursor and execute SQL statements
        cursor = con.cursor()
        cursor.execute(sql)
        #no need to write con.commit
        rows = cursor.fetchAll()

        for row in rows:
            print(row)

class customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def showCustomerDetails(self):
        print(">>Name: {} Phone:{} Email={}".format(self.name, self.phone, self.email))
"""
print("Options:")
print("1. Create New Customer")
print("2. Update Customer")
print("3. Delete Customer")



choice = int(input("Enter Choice:"))
if choice == 1:
    cRef = customer(None, None, None)
    cRef.name = input("enter Customer Name:")
    cRef.phone = input("enter Customer Phone: ")
    cRef.email = input("enter Customer Email:")


    cRef.showCustomerDetails()
    save = input("Would you like to save Customer(yes/no)")
    if save == "yes":
        db = DBHelper()
        db.saveCustomerInDB(cRef)

elif choice == 2:
    cRef = customer(None, None, None)
    cRef.cid = int(input("Enter Customer ID:"))
    cRef.name = input("Enter Customer Name:")
    cRef.phone = input("Enter Customer Phone:")
    cRef.email = input("Enter Customer Email:")

    cRef.showCustomerDetails()
    update = input("Would you like to Update Customer(yes/no)")
    if update == "yes":
        db = DBHelper()
        db.updateCustomerInDB(cRef)

elif choice == 3:
    cid = int(input("Enter Customer ID:"))
    delete = input("Would you like to Delete Customer(yes/no)")
    if delete == "yes":

        db = DBHelper()
        db.deleteCustomerInDB(cid)

"""





