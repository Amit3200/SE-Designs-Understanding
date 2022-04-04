package com.lld.models.Cab;

public class CabFactory{
    public Cab getCab(int id, String driverName, String CabType){
        if(CabType.toLowerCase() == "hatchback"){
            Cab obj = new HatchbackCab(id, driverName);
            return obj;
        }
        if(CabType.toLowerCase() == "suv"){
            Cab obj = new SUV(id, driverName);
            return obj;
        }
        return new HatchbackCab(id,driverName);
    }
}