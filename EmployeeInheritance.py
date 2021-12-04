class Person(object):
    
    def __init__(self,name,age) :
        self.name=name
        self.age=age

    def printData(self) :
        print(self.name,self.age)

class Employee(Person):

    def __init__(self,name,age,profession) :
        Person.__init__(self,name,age)
        self.profession=profession



p1=Employee("rohit naikade",22,"Worker")

p1.printData()
# p1.printData()

