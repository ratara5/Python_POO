class Vehicle():    
    def __init__(self,manufacturer,model):
        self.manufacturer=manufacturer
        self.model=model
        self.running=False #when we build this object, the object is stopped by default
        self.accelerating=False
        self.braking=False
    def start(self):
        self.running=True
    def speed_up(self):
        self.accelerating=True
    def brake(self):
        self.braking=True
    def inform_status(self):
        print('Manufacturer: {}\nModel: {}\nRunning: {}\nAccelerating: {}\nBraking: {}'.format(self.manufacturer,self.model,self.running,self.accelerating,self.braking))

class Truck(Vehicle):
    def to_load(self,load):
        self.load=load
        if(self.load):
            return "The furgon is loaded"
        else:
            return "The truck isn't loaded"

class Motorcycle(Vehicle):    
    maneuvering=''    
    def maneuver(self):
        self.maneuvering='Im doing maneuver'
    def inform_status(self): #Overrides this method for the subclass motorcycle
        print('Manufacturer: {}\nModel: {}\nRunning: {}\nAccelerating: {}\nBraking: {}\nManeuvering: {}'.format(self.manufacturer,self.model,self.running,self.accelerating,self.braking,self.maneuvering))

class Quad(Motorcycle): #Quad motorcycle 4 wheels. Inheret all of class Motorcycle
    pass

class ElecVehicle(Vehicle):
    def __init__(self,elecvehicle_manufacturer,elecvehicle_model):
        super().__init__(elecvehicle_manufacturer,elecvehicle_model)
        self.autonomy=100
        self.charging=False
    def to_charge(self):
        self.charging=True
    def inform_status(self):
        super().inform_status()
        print('Autonomy: {}\nCharging: {}'.format(self.autonomy,self.charging))