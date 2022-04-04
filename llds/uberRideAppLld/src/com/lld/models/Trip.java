package com.lld.models;

import com.lld.models.Cab.Cab;

enum TripStatus{
    IN_PROGRESS,
    FINISHED
}

public class Trip {
    private Rider rider;
    private Cab cab;
    private TripStatus status;
    private Double price;
    private Location fromLocation;
    private Location toLocation;

    public Trip(Rider rider, Cab cab, Double price, Location fromPoint, Location toPoint){
        this.rider = rider;
        this.cab = cab;
        this.price = price;
        this.fromLocation = fromPoint;
        this.toLocation = toPoint;
        this.status = TripStatus.IN_PROGRESS;
    }

    public void endTrip(){
        this.status = TripStatus.FINISHED;
    }

    @Override
    public String toString(){
        return "Trip{" + "\n" +
                "rider = " + rider + "\n" +
                "price = " + price + "\n" +
                "from = " + fromLocation + "\n" +
                "to = " + toLocation + "\n" +
                "status = " + status + "\n" +
                "};";
    }

}
