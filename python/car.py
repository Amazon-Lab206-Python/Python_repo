class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def displayInfo(self):
        print "Price: $"+ str(self.price)
        print 'Speed: '+str(self.speed)+'mph'
        # print fuel status
        print 'Fuel:'+ self.fuel 
        #print mileage
        print 'Mileage:'+str(self.mileage)+'mpg'
        #print Tax rate
        print 'Tax:',
        if self.price > 10000:
            print '0.15'
        else:
            print '0.12'

c1 = Car(10000, 105, 'Kind of Full' , 15)
c2 = Car(100, 15, 'Empty' , 9)
c3 = Car(50000, 1005, '1' , 105)
c4 = Car(5000, 95, 'Kind of Full' , 25)
c5 = Car(1000, 45, 'Kind of Full' , 25)
c6 = Car(6000, 85, 'Half Full' , 22)
c7 = Car(15000, 100, 'Not Full' , 35)

c1.displayInfo();
c2.displayInfo();
c3.displayInfo();
c4.displayInfo();
c5.displayInfo();
c6.displayInfo();
c7.displayInfo();
        