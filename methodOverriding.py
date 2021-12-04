class Person(object):
    def display(self):
        print("this is Person class")

class Student(Person):
    def display(self):
        print("this is student class")

p1=Student()
p1.display()