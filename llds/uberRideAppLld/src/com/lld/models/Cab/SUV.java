package com.lld.models.Cab;

import com.lld.models.Location;
import com.lld.models.Trip;

public class SUV implements Cab {
    int id = 0;
    String driverName = "";
    String vehicleType = "SUV";
    int capacity = 5;
    Trip currentTrip;
    Location currentLocation;
    Boolean isAvailable;

    public SUV(int id, String driverName){
        this.id = id;
        this.driverName = driverName;
        this.isAvailable = true;
    }

    @Override
    public int getId() {
        return id;
    }

    @Override
    public String getDriverName() {
        return driverName;
    }

    @Override
    public String getVehicle() {
        return this.vehicleType + "_" + this.capacity;
    }

    @Override
    public Location getLocation() {
        return currentLocation;
    }

    @Override
    public void setLocation(Location location) {
        this.currentLocation = location;
    }

    @Override
    public boolean getAvailability() {
        return isAvailable;
    }

    @Override
    public void setAvailability(Boolean isAvailable) {
        this.isAvailable = isAvailable;
    }

    @Override
    public Trip getCurrentTrip() {
        return this.currentTrip;
    }

    @Override
    public void setCurrentTrip(Trip trip) {
        this.currentTrip = trip;
    }

    @Override
    public String toString(){
        return "Cabs{"+
                "id = " + id + "\n" +
                "driverName = " + driverName + "\n" +
                "vehicleType = " + vehicleType + "\n" +
                "currentLocation = " + currentLocation + "\n" +
                "isAvailable = " + isAvailable + "};";
    }
}
