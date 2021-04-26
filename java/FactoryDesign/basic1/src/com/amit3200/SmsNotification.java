package com.amit3200;

public class SmsNotification implements Notification{
    @Override
    public void notifyUser() {
        System.out.println("[Notification Type] : SMS");
    }
}
