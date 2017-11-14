class Product(object):
    def __init__(self, price, itemName, weight, brand, cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'For Sale'
    def displayInfo(self):
        print "Price: ${}, Name: {}, Weight: {}lbs, Brand: {}, Cost: ${}, Status: {}".format(self.price, self.itemName, self.weight, self.brand, self.cost, self.status)
        return self
    def sell(self):
        print "It's gone forever now."
        self.status = "sold"
        return self
    def add_tax(self):
        tax = self.price * .1
        print "Tax has been Added. The new total is ${}".format(self.price+tax)
        return self
    def ret(self, reason):
        if(reason == "defective"):
            self.price = 0
            self.status = "defective"
        elif(reason == "in box"):
            self.status = "for sale"
        elif(reason == "open box"):
            self.status = "used"
            self.price = (self.price *.8)
        else:
            print "this is new"
        return self

p1 = Product(200, 'Bike', 25, 'ToyBrandz', 50)

p1.displayInfo().add_tax()