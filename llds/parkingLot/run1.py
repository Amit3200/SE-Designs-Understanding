from model.VehicleSize import VehicleSize
from model.Car import Car
from strategy.SimpleStrategy import SimpleStrategy
from service.ParkingSlotService import ParkingSlotService

floor = 4
size = 100
strategy_taken = SimpleStrategy(floor,size)
ps = ParkingSlotService(floor,size,strategy_taken)

print(ps.parkingLot.showParkingLot())

c1 = Car("TA21","skoda",VehicleSize.Medium,"black")
print(c1)
o1 = ps.park(c1)
print(o1)
c2 = Car("TA21","suzuki",VehicleSize.Large,"white")
print(c2)
o2 = ps.park(c2)
print(o2)


print(ps.parkingLot.showParkingLot())

gs = ps.makeSlotFree('101001')
print(gs)
print(ps.parkingLot.showParkingLot())