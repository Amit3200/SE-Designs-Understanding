package com.amit3200;

public class HatchBackCar extends Car{
    HatchBackCar(String vehicleNumber,Location location){
        super(vehicleNumber,CarType.HATCHBACK,location);
        construct();
    }

    @Override
    void construct(){
        System.out.println("[HATCHBACK DEBUG]: Connecting to hatchback.");
    }
}
