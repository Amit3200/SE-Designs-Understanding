package com.lld.managers;

import com.lld.models.Cab.Cab;
import com.lld.models.Location;

import java.util.*;

public class CabsManager {
    Map<Integer, Cab> cabsMapper = new HashMap<>();

    public void createCab(final Cab newCab) throws Exception {
        if(cabsMapper.containsKey(newCab.getId())){
            throw new Exception("Cab Already Exists");
        }
        cabsMapper.put(newCab.getId(), newCab);
    }

    public Cab getCab(Integer cabId) throws Exception {
        if(!cabsMapper.containsKey(cabId)){
            throw new Exception("Cab Not Found");
        }
        return cabsMapper.get(cabId);
    }

    public void updateCabLocation(final Integer cabId, final Location newLocation) throws Exception {
        if(!cabsMapper.containsKey(cabId)){
            throw new Exception("Cab Not Found");
        }
        cabsMapper.get(cabId).setLocation(newLocation);
    }

    public void updateCabAvailability(final Integer cabId,final Boolean newAvailability) throws Exception {
        if(!cabsMapper.containsKey(cabId)){
            throw new Exception("Cab Not Found");
        }
        cabsMapper.get(cabId).setAvailability(newAvailability);
    }

    public List<Cab> getCabs(final Location fromPoint, final Double distance){
        List<Cab> result = new ArrayList<>();
        for(Cab cab : cabsMapper.values()){
            if(cab.getAvailability() && cab.getLocation().getDistance(fromPoint) <= distance){
                result.add(cab);
            }
        }
        return result;
    }

}
