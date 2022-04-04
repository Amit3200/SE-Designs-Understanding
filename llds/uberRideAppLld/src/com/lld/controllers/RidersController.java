package com.lld.controllers;

import com.lld.managers.RidersManager;
import com.lld.managers.TripsManager;
import com.lld.models.Location;
import com.lld.models.Rider;
import com.lld.models.Trip;
import java.util.*;

public class RidersController {
    private RidersManager ridersManager;
    private TripsManager tripsManager;
    public RidersController(RidersManager rm, TripsManager tm){
        ridersManager = rm;
        tripsManager = tm;
    }
    public void registerRider(final Integer riderId, final String riderName) throws Exception{
        ridersManager.createRider(new Rider(riderId,riderName));
    }

    public void bookRide(final Integer riderId, final Double sx, final Double sy,final Double dx,final Double dy) throws Exception{
        tripsManager.createTrip(ridersManager.getRider(riderId),new Location(sx,sy),new Location(dx,dy));
    }

    public List<Trip> fetchHistory(final Integer riderId) throws Exception{
        List<Trip> trips = tripsManager.tripHistory(ridersManager.getRider(riderId));
        return trips;
    }
}
