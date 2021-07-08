from HouseBuilder import HouseBuilder
from House import House

class IglooBuilder(HouseBuilder):
    __house = None

    def __init__(self):
        print("Igloo Builder")
        self.__house = House()
    
    def build_basement(self):
        self.__house.set_basement("Ice_Bars")
    
    def build_interior(self):
        self.__house.set_interior("Ice_Carvings")
    
    def build_roof(self):
        self.__house.set_roof("Ice_Dome")
    
    def build_structure(self):
        self.__house.set_structure("Ice_Blocks")
    
    def get_house(self):
        return self.__house