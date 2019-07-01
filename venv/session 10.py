#inheritance  Is-a relationship

#amazon e-commerce example
#shoe, mobile etc

class shoe:
    def __init__(self, pid, name, price, brand, color, size ):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color
        self.size = size

    def updateMobileDetails(self, pid, name, price, brand, color, size ):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color
        self.size = size

    def showShoeDetails(self ):

        

