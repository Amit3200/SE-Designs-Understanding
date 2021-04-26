package com.amit3200;

public class SuvCar extends Car{
    SuvCar(String vehicleNumber, Location location){
        super(vehicleNumber,CarType.SUV,location);
        construct();
    }

    @Override
    void construct(){
        System.out.println("[SUV DEBUG]: Connecting to suv.");
    }
}
