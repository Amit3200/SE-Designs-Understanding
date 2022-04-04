package com.lld.models.Cab;

import com.lld.models.Location;
import com.lld.models.Trip;

public interface Cab {
    public int getId();
    public String getDriverName();
    public String getVehicle();

    public Location getLocation();
    public void setLocation(Location location);

    public boolean getAvailability();
    public void setAvailability(Boolean isAvailable);

    public Trip getCurrentTrip();
    public void setCurrentTrip(Trip trip);
}






