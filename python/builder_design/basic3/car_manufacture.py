import json
from abc import ABC, abstractmethod
"""
    A company ABC manufactures CAR they create Luxury and Sports Cars
    In Luxury they create corolla
        engine : 1800 cc 139 hp

    In Sport they create supra
        engine : 2000 cc 200 hp
    
    The cars are build step by step and it can vary in future. The number of car types can increase in future
    Design a software for the same.
"""
class Car:
    car_name : str
    car_type : str 
    engine   : str 
    tier     : str

    def set_car_name(self, car_name):
        self.car_name = car_name
    
    def set_car_type(self, car_type):
        self.car_type = car_type
    
    def set_car_engine(self, engine):
        self.engine = engine
    
    def set_tier(self, tier):
        self.tier = tier

    def get_car_info(self):
        car_info = {"name":self.car_name, "type":self.car_type, "engine":self.engine, "tier":self.tier}
        return car_info

    def show_details(self):
        car_info = self.get_car_info()
        print(json.dumps(car_info, indent = 4))


class CarBuilder(ABC):
    car : Car
    def instantiate_process(self):
        self.car = Car()
        # pass

    @abstractmethod
    def build_car_name(self):
        pass

    @abstractmethod
    def build_car_type(self):
        pass

    @abstractmethod
    def build_car_engine(self):
        pass

    @abstractmethod
    def build_car_tier(self):
        pass

    def get_car(self):
        return self.car

class LuxuryCarBuilder(CarBuilder):
    def build_car_name(self):
        self.car.set_car_name("Corrola")

    def build_car_type(self):
        self.car.set_car_type("Luxury")

    def build_car_engine(self):
        self.car.set_car_engine("v6 1800 cc 139 hp")

    def build_car_tier(self):
        self.car.set_tier("Luxury 18inch")

class SportsCarBuilder(CarBuilder):
    def build_car_name(self):
        self.car.set_car_name("Supra")

    def build_car_type(self):
        self.car.set_car_type("Sports")

    def build_car_engine(self):
        self.car.set_car_engine("v12 2000 cc 200 hp")

    def build_car_tier(self):
        self.car.set_tier("Sports 18inch Solid Plain.")

class Director:
    builder : CarBuilder
    def manufacture_car(self, builder: CarBuilder):
        builder.instantiate_process()
        builder.build_car_name()
        builder.build_car_type()
        builder.build_car_engine()
        builder.build_car_tier()
        return builder.get_car()

def main():
    director            = Director()
    luxury_car_builder  = LuxuryCarBuilder()
    sports_car_builder  = SportsCarBuilder()
    car1 : Car = director.manufacture_car(luxury_car_builder)
    print(car1)
    car1.show_details()
    car2 : Car = director.manufacture_car(sports_car_builder)
    print(car2)
    car2.show_details()


    



main()

