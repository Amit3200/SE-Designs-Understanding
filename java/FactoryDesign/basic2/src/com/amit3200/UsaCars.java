package com.amit3200;

public class UsaCars {
    static Car buildCar(String vehicleName,CarType model){
        Car carObject = null;
        switch (model){
            case HATCHBACK:
                carObject = new HatchBackCar(vehicleName,Location.USA);
                break;

            case SEDAN:
                carObject = new SedanCar(vehicleName,Location.USA);
                break;

            case SUV:
                carObject = new SuvCar(vehicleName,Location.USA);
                break;

            default:
                break;
        }
        return carObject;
    }
}
