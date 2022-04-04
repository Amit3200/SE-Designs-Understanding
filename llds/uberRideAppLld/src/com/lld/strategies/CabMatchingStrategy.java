package com.lld.strategies;

import com.lld.models.Cab.Cab;
import com.lld.models.Location;
import com.lld.models.Rider;

import java.util.*;

public interface CabMatchingStrategy {
    Cab matchCabToRider(Rider rider, List<Cab> candidateCabs, Location fromPoint, Location toPoint);
}
