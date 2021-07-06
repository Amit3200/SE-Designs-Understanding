# This is just a program to understand builder pattern in python.

# HousePlan - Abstract Class which has basic methods which will be there for all the types of houses but the properties might vary
from abc import ABC, abstractmethod 

class HousePlan(ABC):

    @abstractmethod
    def set_basement(self,basement):
        pass

    @abstractmethod
    def set_structure(self,structure):
        pass 

    @abstractmethod
    def set_roof(self,roof):
        pass 

    @abstractmethod
    def set_interior(self,interior):
        pass 

