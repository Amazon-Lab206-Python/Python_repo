class Animals(object):
    def __init__(self,name):
        self.name = name
        self.health = 100
    def displayInfo(self):
        print 'My name is {}, {}hp'.format(self.name,self.health)
    def walk(self):
        self.health -= 1
        return self;
    def run(self):
        self.health -= 5
        return self;
class Dog(Animals):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self;
class Dragon(Animals):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        print '{} I am a Dragon'.format(self.health)
        return self;
    

a1 = Animals('spot')
d1 = Dog('max')
dr1 = Dragon('Donkey')

a1.walk().walk().walk().run().run().displayInfo();
d1.walk().walk().walk().run().run().pet().displayInfo();
dr1.pet().fly().fly().fly().displayInfo()