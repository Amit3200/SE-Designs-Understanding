package com.amit3200;

public class EmailNotification implements Notification{
    @Override
    public void notifyUser() {
        System.out.println("[Notification Type] : EMAIL");
    }
}
