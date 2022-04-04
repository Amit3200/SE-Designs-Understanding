package com.lld.strategies;

import com.lld.models.Cab.Cab;
import com.lld.models.Location;
import com.lld.models.Rider;
import java.util.*;

public class DefaultCabMatchingStrategy implements CabMatchingStrategy {
    @Override
    public Cab matchCabToRider(final Rider rider, final List<Cab> candidateCabs, Location fromPoint, Location toPoint){
        if(candidateCabs.isEmpty()){
            return null;
        }
        return candidateCabs.get(0);
    }
}
