from strategy.ParkingStrategy import ParkingStrategy
from collections import defaultdict

class SimpleStrategy(ParkingStrategy):
    ticket_slot_map = defaultdict(list[int])
    def __init__(self,floor,size):
        for floor_no in range(1,floor+1):
            for slots in range(1,size+1):
                ticket_no = str(floor_no) + "0100" + str(slots)
                self.ticket_slot_map[ticket_no] = [floor_no,slots]

    def getNextSlot(self):
        for ticket in self.ticket_slot_map.keys():
            yield ticket
            
    def addSlot(self):
        pass 

    def removeSlot(self, ticketNo):
        pass