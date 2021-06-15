package com.amit3200.queryCache;

import org.json.JSONObject;

public class queryAPI {

    LRU memory_cache = null;
    public queryAPI(LRU cache){
        this.memory_cache = cache;
    }

    public String queryPraser(String query){
        String queryStr = query.toLowerCase();
        return queryStr;
    }

    public JSONObject createCacheResponse(String query,Node result){
        String value = null,title = null;
        boolean presentInCache = true;
        if(result == null){
            value = "INVALID! NOT PRESENT IN CACHE.";
            title = "INVALID! NOT PRESENT IN CACHE.";
            presentInCache = false;
        }
        else{
            value = result.value;
            title = result.title;
        }
        JSONObject json = new JSONObject();
        json.put("query",query);
        json.put("title",title);
        json.put("value",value);
        json.put("presentInCache",presentInCache);
//        System.out.println("[DEBUG] : "+json.toString());
        return json;

    }

    public JSONObject processQuery(String query){
        String processableQuery = this.queryPraser(query);
        Node result = this.memory_cache.get(processableQuery);
        return this.createCacheResponse(processableQuery,result);
    }
}
