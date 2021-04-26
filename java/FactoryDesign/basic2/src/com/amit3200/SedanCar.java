package com.amit3200;

public class SedanCar extends Car{
    SedanCar(String vehicleNumber,Location location){
        super(vehicleNumber,CarType.SEDAN,location);
        construct();
    }

    @Override
    void construct(){
        System.out.println("[SEDAN DEBUG]: Connecting to sedan.");
    }
}
