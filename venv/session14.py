import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#model
class customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def showCustomerDetails(self):
        print(">>Name: {} Phone:{} Email={}".format(self.name, self.phone, self.email))


# Use a service account
cred = credentials.Certificate('myprivatekey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

#cRef = customer("Fionna", "+91 99999 88888", "fionna@example.com")
#data = cRef.__dict__

#db.collection("customer").document().set(data)

#print(">> ",cRef.name,"Saved in Firebase")

docs = db.collection("customer").get()

for doc in docs:
    print(doc.id, doc.to_dict())
