from model.Car import Car
class Slot:
    slot        : int
    floor       : int
    car         : Car   = None

    def __init__(self, slot, floor):
        self.slot = slot
        self.floor = floor
    
    def isSlotFree(self):
        return self.car == None 
    
    def assignCar(self, car : Car):
        self.car = car 
    
    def unassignCar(self):
        self.car = None
    
    def getParkedCar(self):
        return self.car
    
    def __repr__(self):
        return str(self.floor)+"_" + str(self.slot) + "_" + str(self.car)