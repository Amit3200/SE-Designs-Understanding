from model.VehicleSize import VehicleSize
class Car:
    registration_number : str 
    car_name            : str 
    size                : VehicleSize
    car_color           : str 

    def __init__(self, registration_name, car_name, vehicle_size, car_color = None):
        self.registration_number = registration_name
        self.car_name            = car_name
        self.size                = vehicle_size
        self.car_color           = car_color
    
    def __repr__(self):
        return self.registration_number+"_"+self.car_name+"_"+str(self.size)+"_"+self.car_color