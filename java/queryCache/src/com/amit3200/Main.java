package com.amit3200;

import com.amit3200.queryCache.LRU;
import com.amit3200.queryCache.queryAPI;
import org.json.JSONObject;
import java.util.ArrayList;
import java.util.Arrays;


public class Main {

    public static void main(String[] args){
        LRU lru = new LRU(5);
        lru.put("work","LRU1","code");
        lru.put("cross","LRU1","walk");
        lru.put("name","LRU1","amit3200");
        lru.put("profession","LRU1","software engineer");
        lru.put("hobby","LRU1","procastinating");
        lru.put("nature","LRU1","anti social");
        lru.put("status","LRU1","complex disorder");

        queryAPI cacheObj = new queryAPI(lru);
        ArrayList<String> queries = new ArrayList<>(Arrays.asList("WORK","IDX","OrtHodox","NamE","hoBby","sTatus","name","work","cross","hobby","status","statUs","NAture","Status","Hobby","profession"));
        for(String q : queries){
            JSONObject resp = cacheObj.processQuery(q);
            System.out.println("[PROD] : KEY - "+q+" :response -> "+resp.toString());
        }
    }

}
