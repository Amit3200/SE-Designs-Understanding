package com.amit3200;


public abstract class Car {
    String vehicleNumber=null;
    CarType model = null;
    Location location = null;

    Car(String vehicleNumber,CarType model,Location location){
        this.vehicleNumber = vehicleNumber;
        this.model = model;
        this.location = location;
    }

    abstract void construct();

    String getVehicleNumber(){
        return vehicleNumber;
    }

    void setVehicleNumber(String vehicleNumber){
        this.vehicleNumber = vehicleNumber;
    }

    CarType getModel(){
        return model;
    }

    void setModel(CarType model){
        this.model=model;
    }

    Location getLocation(){
        return location;
    }

    void setLocation(Location location){
        this.location = location;
    }

    @Override
    public String toString(){
        return "[STATEMENT]: Car No:"+vehicleNumber+" Model "+model+" at Location "+location+".";
    }

}
