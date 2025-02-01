# 45 minutes
# cases covered
# park, unpark, spot
# force_parking
# basic checks on sizes
# park -> O(N * M), unpark -> O(1), spot -> O(1)
from models.parking_lot import ParkingLot



bike = 'MotorCycle'
car = 'Car'


building_a = ParkingLot()


map_of_building_a = {
    bike : 2,
    car : 3
}

building_a.create_parking_lot(2, map_of_building_a)

building_a.debug()





print(building_a.park(car, '1001'))
building_a.debug()
print(building_a.park(car, '1002'))
print(building_a.park(bike, '101'))
building_a.debug()
print(building_a.park(bike, '102'))
building_a.debug()
print(building_a.park(bike, '103'))
print(building_a.park(car, '1003'))
building_a.debug()
print(building_a.park(bike, '104'))
print(building_a.park(bike, '105'))
building_a.debug()


print(building_a.unpark('105'))
print(building_a.unpark('104'))
building_a.debug()

print(building_a.unpark('1003'))
print(building_a.unpark('1001'))
building_a.debug()


print(building_a.park(car, '1005'))
building_a.debug()


print(building_a.spot(0, 1))
building_a.debug()
