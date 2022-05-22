from collections import defaultdict
from model.Slot import Slot
class ParkingLot:
    parking_lot     = defaultdict(list[Slot])
    ticket_slot_map = defaultdict(list[int])
    slot_capacity   = None
    
    def __init__(self,floor, slot_capatcity, ticket_slots):
        self.slot_capacity = slot_capatcity
        for floor_no in range(1,floor + 1):
            for slots in range(slot_capatcity):
                slot_created = Slot(slots,floor_no)
                self.parking_lot[floor_no].append(slot_created)
        self.ticket_slot_map = ticket_slots

    def getSlot(self,ticket_no) -> Slot:
        if self.ticket_slot_map.get(ticket_no,None) == None:
            return None
        return self.parking_lot[self.ticket_slot_map[ticket_no][0]][self.ticket_slot_map[ticket_no][1]]
    
    def park(self,car, ticket_no) -> Slot:
        if self.getSlot(ticket_no) == None:
            print("Invalid Exception")
        elif self.getSlot(ticket_no).isSlotFree():
            self.getSlot(ticket_no).assignCar(car)
            return self.getSlot(ticket_no)
        else:
            print("Already Occupied")
    
    def markSlotFree(self, ticket_no) -> Slot:
        self.getSlot(ticket_no).unassignCar()
        return self.getSlot(ticket_no)
    
    def showParkingLot(self):
        print(self.parking_lot)
        print("="*50)
        print(self.ticket_slot_map)