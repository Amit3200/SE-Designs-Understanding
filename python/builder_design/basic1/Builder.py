from HousesContainer import IglooBuilder, BoatHouseBuilder
from Engineer import Engineer

class Builder:

    def __init__(self):
        iglooBuilder = IglooBuilder.IglooBuilder()
        boatHouseBuilder = BoatHouseBuilder.BoatHouseBuilder()

        engineer_builder = Engineer(iglooBuilder)
        engineer_builder.construct_house()
        house = engineer_builder.get_house()
        self.print_msg(house)

        #over write
        engineer_builder = Engineer(boatHouseBuilder)
        engineer_builder.construct_house()
        house = engineer_builder.get_house()
        self.print_msg(house)        

    def print_msg(self,house):
        print("DETAILS OF HOUSE")
        print("Object : ",house)
        print(house.show_house())