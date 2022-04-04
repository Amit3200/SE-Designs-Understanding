package com.lld.models;

import static java.lang.Math.*;

public class Location {
    private Double x, y;

    public Location(Double x, Double y){
        this.x = x;
        this.y = y;
    }

    public Double getX(){
        return x;
    }

    public Double getY(){
        return y;
    }

    public void setX(Double x){
        this.x = x;
    }

    public void setY(Double y){
        this.y = y;
    }

    public Double getDistance(Location location2){
        return sqrt(pow(this.x - location2.getX(),2) + pow(this.y - location2.getY(),2));
    }

    @Override
    public String toString(){
        return "Location{" + "\n" +
                "x = " + getX() + "\n" +
                "y = " + getY() + "\n" +
                "}";
    }
}
