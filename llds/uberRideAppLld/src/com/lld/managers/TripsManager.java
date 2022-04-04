package com.lld.managers;

import com.lld.models.Cab.Cab;
import com.lld.models.Location;
import com.lld.models.Rider;
import com.lld.models.Trip;
import com.lld.strategies.CabMatchingStrategy;
import com.lld.strategies.PricingStrategy;

import java.util.*;
import java.util.stream.Collectors;

public class TripsManager {
    public static final Double MAX_ALLOWED_TRIP_MATCHING_DISTANCE = 10.0;
    private Map<Integer, List<Trip>> trips = new HashMap<>();

    private CabsManager cabsManager;
    private RidersManager ridersManager;
    private CabMatchingStrategy cabMatchingStrategy;
    private PricingStrategy pricingStrategy;

    public TripsManager(CabsManager cabsManager, RidersManager riderManager, CabMatchingStrategy cabMatchingStrategy, PricingStrategy pricingStrategy){
        this.cabsManager = cabsManager;
        this.ridersManager = riderManager;
        this.cabMatchingStrategy = cabMatchingStrategy;
        this.pricingStrategy = pricingStrategy;
    }

    public void createTrip(final Rider rider, final Location fromPoint, final Location toPoint) throws Exception {
        final List<Cab> closeByCabs = cabsManager.getCabs(fromPoint,MAX_ALLOWED_TRIP_MATCHING_DISTANCE);
        final List<Cab> closeByAvailable = closeByCabs.stream().filter(cab -> cab.getCurrentTrip() == null).collect(Collectors.toList());
        final Cab selectedCab = cabMatchingStrategy.matchCabToRider(rider,closeByAvailable,fromPoint,toPoint);
        if(selectedCab == null){
            throw new Exception("No cabs available.");
        }
        final Double Price = pricingStrategy.findPrice(fromPoint, toPoint);
        final Trip newTrip = new Trip(rider,selectedCab,Price,fromPoint,toPoint);
        if(!trips.containsKey(rider.getId())){
            trips.put(rider.getId(),new ArrayList<>());
        }
        trips.get(rider.getId()).add(newTrip);
        selectedCab.setCurrentTrip(newTrip);
    }

    public List<Trip> tripHistory(final Rider rider){
        return trips.get(rider.getId());
    }

    public void endTrip(final Cab cab) throws Exception {
        if(cab.getCurrentTrip() == null){
            throw new Exception("Not Trip Found.");
        }
        cab.getCurrentTrip().endTrip();
        cab.setCurrentTrip(null);
    }
}
