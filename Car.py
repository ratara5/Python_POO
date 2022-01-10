class Car():
    
    #initial status or factory or default or constructor
    def __init__(self,color): #other programming languages creates constructor method with the same class name
        self.__lenght=250
        self.__width=120
        self.__wheels=4 #encapsulation prevents change in attribute values out of class. I've change its name into class...
        self.__running=False #programmer want this variable only change from into class*...
        self.color=color

    def inform_status(self): #other programming languages don't use 'self', use it implicit
        print('The car have {} wheels, a width of {}, a lenght of {} and its color is {}'.format(self.__wheels,self.__lenght,self.__width,self.color))#...

    def start(self,starts):
        self.__running=starts#*...
        if(self.__running):
            ch=self.__check()
        if(self.__running and ch==True):
            return 'The car is running'
        elif(self.__running and ch==False):
            return 'Some bad in check. The car cannot start'
        else:
            return 'The car is stopped'
    
    def __check(self): #It's not logic this method initialize its anytime and anywhere. Only it execute when def start(). Because method is encapsulated.
        print('Check in progress')
        self.gasoil='ok'
        self.oil='ok'
        self.doors='closed'

        if(self.gasoil=='ok' and self.oil=='ok' and self.doors=='closed'):
            return True
        else:
            return False



my_car=Car('red')

s1=my_car.start(True)
print(s1)

my_car.inform_status()

##################################################33
print('\n--------------Now, we create a second object----------------')

my_car2=Car('blue')

s2=my_car.start(False)
print(s2)

my_car.wheels=2 #it's not possible, attribute wheels is encapsulated
my_car.__wheels=2 #it's not possible, attribute wheels is encapsulated

my_car2.inform_status()

#print(my_car2.__check()) #it's not possible, method check() is encapsulated