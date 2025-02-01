from collections import defaultdict
from copy import deepcopy

class ParkingLot:
    def __init__(self):
        self.parking_lot = defaultdict(list)
        self.parked_vehicles = defaultdict(int)
        self.vehicle_park_size = {
            'MotorCycle': 1,
            'Car': 2,
        }

    # parking_map should be a dict <string, <int, int>>
    # key refers to vehicle type
    # 0 : int refers to the capacity type
    # 1 : consider it as size may be
    def create_parking_lot(self, floors, parking_map):
        floor_layout = []
        for vehicle_type, capacity in parking_map.items():
            for x in range(capacity):
                floor_layout.append([False, vehicle_type])
        
        for floor in range(floors):
            self.parking_lot[floor] = deepcopy(floor_layout)
  
    def park(self, vehicle_type, vehicle_number, force_park = False, level = 0):
        parking_status = False
        for floor in self.parking_lot:
            for idx, slot in enumerate(self.parking_lot[floor]):
                if (slot[0] == False and slot[1] == vehicle_type) or (slot[0] == False and self.vehicle_park_size[vehicle_type] < self.vehicle_park_size[slot[1]] and force_park):
                    self.parking_lot[floor][idx][0] = vehicle_number
                    self.parked_vehicles[vehicle_number] = (floor, idx)
                    parking_status = True
                    break
            if parking_status:
                break
        if parking_status == False:
            if level < len(self.vehicle_park_size.keys()):
                self.park(vehicle_type, vehicle_number, True, level + 1)
            else:
                return f"Can't Park Vehicle {vehicle_number}"
        return f"Vehicle : {vehicle_number}, Parked at ({floor},{slot})"
    
    def unpark(self, vehicle_number):
        if vehicle_number not in self.parked_vehicles:
            return f"Can't find vehicle with {vehicle_number}"

        parked_coordinates = self.parked_vehicles.get(vehicle_number)
        self.parking_lot[parked_coordinates[0]][parked_coordinates[1]][0] = False
        del self.parked_vehicles[vehicle_number]
        return f"Un Parked {vehicle_number}"
    
    def spot(self, floor, slot):
        if floor < 0 or floor >= len(self.parking_lot.keys()) or slot < 0 or slot >= len(self.parking_lot.get(floor)):
            return f"Incorrect Position for parking lot"
        if self.parking_lot[floor][slot][0] == False:
            return f"No Vehicle parked at ({floor}, {slot})"

        return self.parking_lot[floor][slot][0]

    def debug(self):
        print("=" * 50)
        for floor in self.parking_lot:
            print(floor, " : ", self.parking_lot[floor])
        print("\n")
