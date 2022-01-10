class Car():
    def to_move(self):
        print('I move myself using 4 wheels')

class Motorcycle():
    def to_move(self):
        print('I move myself using 2 wheels')

class Truck():
    def to_move(self):
        print('I move myself using 12 wheels')

def movement(object): #Doesn´t require indicate object type. Python is weakly-typed language
    object.to_move() #Go to class respective and applies the method respective

t1=Truck()
movement(t1)

m1=Motorcycle()
movement(m1)