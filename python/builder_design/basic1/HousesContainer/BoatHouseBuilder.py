from HouseBuilder import HouseBuilder
from House import House

class BoatHouseBuilder(HouseBuilder):
    __house = None

    def __init__(self):
        print("BoatHouse Builder")
        self.__house = House()
    
    def build_basement(self):
        self.__house.set_basement("Boat_Wood")
    
    def build_interior(self):
        self.__house.set_interior("Boat_Shelves")
    
    def build_roof(self):
        self.__house.set_roof("Boat_Wood_Roof")
    
    def build_structure(self):
        self.__house.set_structure("Boat")
    
    def get_house(self):
        return self.__house