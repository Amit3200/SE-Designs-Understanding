package com.lld.models;

public class Rider {
    int id;
    String name;
    public Rider(int id, String name){
        this.id = id;
        this.name = name;
    }

    public int getId(){
        return this.id;
    }

    public String getName(){
        return this.name;
    }

    @Override
    public String toString(){
        return "Rider{" + "\n" +
                "id : " + id + "\n" +
                "name : " + name + "\n" +
                "};";
    }
}
