package com.lld.strategies;

import com.lld.models.Location;

public interface PricingStrategy {
    Double findPrice(Location fromPoint, Location toPoint);
}
