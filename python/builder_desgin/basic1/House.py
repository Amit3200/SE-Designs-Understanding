from HousePlan import HousePlan

class House(HousePlan):
    __basement:str = None
    __structure:str = None
    __roof:str = None
    __interior:str = None

    def set_basement(self,basement):
        self.__basement = basement
    
    def set_interior(self,interior):
        self.__interior = interior
    
    def set_roof(self, roof):
        self.__roof = roof 
    
    def set_structure(self, structure):
        self.__structure = structure
    
    def show_house(self):
        msg = """
        Basement:{basement},
        Structure:{structure},
        Roof:{roof},
        Interior:{interior}
        """.format(basement = self.__basement, structure = self.__structure, roof = self.__roof, interior = self.__interior)
        return msg



