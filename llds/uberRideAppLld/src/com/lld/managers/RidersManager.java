package com.lld.managers;

import com.lld.models.Rider;

import java.util.*;

public class RidersManager {
    Map<Integer, Rider> riderMapper = new HashMap<>();

    public void createRider(final Rider rider) throws Exception {
        if(riderMapper.containsKey(rider.getId())){
            throw new Exception("Rider Id Already Exists.");
        }
        riderMapper.put(rider.getId(),rider);
    }

    public Rider getRider(final Integer riderId) throws Exception {
        if(!riderMapper.containsKey(riderId)){
            throw new Exception("Rider Doesn't Exists.");
        }
        return riderMapper.get(riderId);
    }

}
