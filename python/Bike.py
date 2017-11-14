class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "My price is {}, my max speed is {} and, my total miles is {}".format(self.price,self.max_speed,self.miles)
    def ride(self):
        self.miles = self.miles + 10
        return self
    def reverse(self):
        self.miles  = self.miles - 5
        return self

b1 = Bike(199.99, 35, 0)
b2 = Bike(299.99, 45, 0)
b3 = Bike(399.99, 55, 0)

b1.ride().ride().ride().reverse().displayInfo()
b2.ride().ride().reverse().reverse().displayInfo()
b3.reverse().reverse().reverse().displayInfo()