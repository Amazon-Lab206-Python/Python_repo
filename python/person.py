class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def talk(self):
        print "my name is: {}".format(self.name)
        

p1 = Person(25, 'Noah')
p2 = Person(25, 'Todd')
p3 = Person(10,"Dennis The Menace")

p1.talk()
p2.talk()
p3.talk()
