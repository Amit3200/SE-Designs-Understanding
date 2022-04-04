package com.lld.controllers;

import com.lld.managers.CabsManager;
import com.lld.managers.TripsManager;
import com.lld.models.Cab.CabFactory;
import com.lld.models.Location;

public class CabsController {
    private CabsManager cabsManager;
    private TripsManager tripsManager;

    public CabsController(CabsManager cabsManager, TripsManager tripsManager){
        this.cabsManager = cabsManager;
        this.tripsManager = tripsManager;
    }

    public void registerCab(final Integer cabId, final String driverName, final String carType) throws Exception {
        CabFactory cf = new CabFactory();
        cabsManager.createCab(cf.getCab(cabId,driverName,carType));
    }

    public void updateCabLocation(final Integer cabId, final Double newX, final Double newY) throws Exception{
        cabsManager.updateCabLocation(cabId,new Location(newX,newY));
    }

    public void updateCabAvailability(final Integer cabId, final Boolean newAvailability) throws Exception{
        cabsManager.updateCabAvailability(cabId,newAvailability);
    }

    public void endTrip(final Integer cabId) throws Exception{
        tripsManager.endTrip(cabsManager.getCab(cabId));
    }

}
