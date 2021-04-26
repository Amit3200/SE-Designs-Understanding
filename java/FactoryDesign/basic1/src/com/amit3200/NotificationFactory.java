package com.amit3200;

public class NotificationFactory {
    public Notification createNotification(String channel){
     if(channel==null || channel.isEmpty())
         return null;
     switch (channel){
         case "SMS":
             return new SmsNotification();
         case "PUSH":
             return new PushNotification();
         case "EMAIL":
             return new EmailNotification();
         default:
             return null;
     }
    }
}
