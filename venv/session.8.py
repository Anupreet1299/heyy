class product:

    restaurantName ="ABC"


    #constructor: when object is created in memory
    def __init__(self):
        self.name = "Dal makhani"
        self.price = 200

    #function

    def showProduct(self):
        print(self.name, self.price, product.restaurantName)


    #destructor:
    def __del__(self):
        print("product deleted", self)

p1 = product
p2 = product

#print( __dict__)
#print( __dict__)
# showProduct()
p2.showFunction()

print(id(p1))
print(id(p2))

print("thank you")