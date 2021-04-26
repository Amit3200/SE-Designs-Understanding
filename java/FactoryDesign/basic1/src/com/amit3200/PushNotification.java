package com.amit3200;

public class PushNotification implements Notification {
    @Override
    public void notifyUser() {
        System.out.println("[Notification Type] : PUSH");
    }
}
