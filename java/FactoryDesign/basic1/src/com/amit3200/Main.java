package com.amit3200;
/*
author : amit3200
purpose : understanding the Factory Design Pattern
 */
public class Main {
    public static void main(String[] args){
        NotificationFactory notificationFactory =  new NotificationFactory();
        Notification notification = notificationFactory.createNotification("PUSH");
        notification.notifyUser();
    }
}
