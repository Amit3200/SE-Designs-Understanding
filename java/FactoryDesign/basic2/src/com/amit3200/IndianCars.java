package com.amit3200;

public class IndianCars {
    static Car buildCar(String vehicleName,CarType model){
        Car carObject = null;
        switch (model){
            case HATCHBACK:
                carObject = new HatchBackCar(vehicleName,Location.INDIA);
                break;

            case SEDAN:
                carObject = new SedanCar(vehicleName,Location.INDIA);
                break;

            case SUV:
                carObject = new SuvCar(vehicleName,Location.INDIA);
                break;

            default:
                break;
        }
        return carObject;
    }
}
