from abc import ABC, abstractmethod
class ParkingStrategy(ABC):
    def __init__(self,floor,size):
        pass
    @abstractmethod
    def addSlot(self):
        pass

    @abstractmethod
    def removeSlot(self,ticketNo):
        pass 

    @abstractmethod
    def getNextSlot(self):
        pass
    