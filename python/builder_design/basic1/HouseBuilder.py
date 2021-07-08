from abc import ABC,abstractmethod

class HouseBuilder(ABC):
    
    @abstractmethod
    def build_basement(self):
        pass 

    @abstractmethod
    def build_interior(self):
        pass 

    @abstractmethod
    def build_roof(self):
        pass 

    @abstractmethod
    def build_structure(self):
        pass

    @abstractmethod
    def get_house(self):
        pass


