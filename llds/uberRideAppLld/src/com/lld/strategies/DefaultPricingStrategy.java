package com.lld.strategies;

import com.lld.models.Location;


public class DefaultPricingStrategy implements PricingStrategy{
    public static final Double PER_KM_RATE = 10.0;

    @Override
    public Double findPrice(Location fromPoint, Location toPoint){
        return fromPoint.getDistance(toPoint) * PER_KM_RATE;
    }
}
