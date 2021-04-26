package com.amit3200;

public class CarFactory {
    private CarFactory(){

    }
    public static Car buildCar(String vehicleNumber,CarType model){
        Car carObject = null;
        Location location = Location.INDIA; // use something to detect on runtime.
        switch (location){
            case USA:
                carObject = UsaCars.buildCar(vehicleNumber,model);
                break;

            case INDIA:
                carObject = IndianCars.buildCar(vehicleNumber,model);
                break;

            default:
                break;
        }
        return carObject;
    }
}
