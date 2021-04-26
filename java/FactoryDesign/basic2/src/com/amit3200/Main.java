package com.amit3200;

enum CarType{HATCHBACK, SEDAN, SUV}
enum Location {USA, INDIA}
public class Main {

    public static void main(String[] args) {
        System.out.println(CarFactory.buildCar("UIO-K2W1",CarType.SUV));
        System.out.println(CarFactory.buildCar("I12-1JL",CarType.HATCHBACK));
        System.out.println(CarFactory.buildCar("KOP-LW1",CarType.HATCHBACK));
        System.out.println(CarFactory.buildCar("YUI-21K",CarType.SEDAN));
    }
}
