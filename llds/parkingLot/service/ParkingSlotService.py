from strategy.ParkingStrategy import ParkingStrategy
from model.ParkingLot import ParkingLot
from strategy import *

class ParkingSlotService:
    parkingLot = None
    parkingStrategy : ParkingStrategy= None
    def __init__(self, floor, size, strategy):
        self.parkingLot = ParkingLot(floor, size, strategy.ticket_slot_map)
        self.parkingStrategy = strategy
    
    def park(self,car) -> int:
        ticket = next(self.parkingStrategy.getNextSlot())
        if ticket != None:
            self.parkingLot.park(car,ticket)
        return ticket
    
    def makeSlotFree(self,ticket_no):
        self.parkingLot.markSlotFree(ticket_no)
    


