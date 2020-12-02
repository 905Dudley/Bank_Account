# A Sample class with init method
class Person:

    #init method or constructor
    def __init__(self, firstname):
        self.name = firstname


    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p1 = Person('Matthew')
p1.say_hi()

p2 = Person('Richard')
p2.say_hi()
