package com.amit3200;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

// DataNode is the food cooked.

public class DataNode {
    private String dateProduced;
    private int dataValue;
    DataNode(int data){
        LocalDateTime now=LocalDateTime.now();
        DateTimeFormatter dt=DateTimeFormatter.ofPattern("yyyy-MM-dd hh:mm:ss");
        this.dateProduced=dt.format(now);
        this.dataValue=data;
    }
    public String getNodeVal(String msg){
        return "Node Date:"+this.dateProduced+" Node Data:"+this.dataValue+" - - - > "+msg.toUpperCase();
    }
}
