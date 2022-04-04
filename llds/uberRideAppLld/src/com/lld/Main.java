package com.lld;

import com.lld.controllers.CabsController;
import com.lld.controllers.RidersController;
import com.lld.managers.CabsManager;
import com.lld.managers.RidersManager;
import com.lld.managers.TripsManager;
import com.lld.models.Cab.Cab;
import com.lld.models.Trip;
import com.lld.strategies.CabMatchingStrategy;
import com.lld.strategies.DefaultCabMatchingStrategy;
import com.lld.strategies.DefaultPricingStrategy;
import com.lld.strategies.PricingStrategy;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception{
        System.out.println("Hello");
        CabsManager cm = new CabsManager();
        RidersManager rm = new RidersManager();
        CabMatchingStrategy dcms = new DefaultCabMatchingStrategy();
        PricingStrategy pcs = new DefaultPricingStrategy();
        TripsManager tm = new TripsManager(cm, rm, dcms, pcs);
        CabsController cc = new CabsController(cm, tm);
        RidersController rc = new RidersController(rm, tm);

        cc.registerCab(1, "archer","suv");
        cc.updateCabLocation(1,1.0,1.1);

        rc.registerRider(1,"takumi");
        rc.bookRide(1,0.0,0.0,5.2,5.3);
        List<Trip> t = rc.fetchHistory(1);
        for(int i = 0; i < t.size(); i++){
            System.out.println(t.get(i));
        }

    }
}
