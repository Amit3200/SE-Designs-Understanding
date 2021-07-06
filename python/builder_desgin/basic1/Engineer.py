from HouseBuilder import HouseBuilder
class Engineer:
    __house_builder = None
    def __init__(self,house_builder):
        self.__house_builder = house_builder
    
    def get_house(self):
        return self.__house_builder.get_house()

    def construct_house(self):
        self.__house_builder.build_basement()
        self.__house_builder.build_interior()
        self.__house_builder.build_roof()
        self.__house_builder.build_structure()
    
