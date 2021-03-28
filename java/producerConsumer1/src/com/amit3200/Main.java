package com.amit3200;
/*
author  : amit3200
subject : understanding basics of the threading in the java. Implementation of simple producer consumer problem.
*/
public class Main {
    static int terminatorValue=0;             // used to terminate program [increases on producer and consumer invoke]
    final static int TerminateProcess=7;      // max value till the program should run
    public static void main(String[] args) throws InterruptedException{
        final ProducerConsumer producerConsumerObject = new ProducerConsumer(); // creating one producerConsumerObject
        Thread t1=new Thread(new Runnable() {                                   // thread 1 to run the producer
            @Override
            public void run() {
                try{
                    producerConsumerObject.produce();                           // calling producer
                }
                catch (InterruptedException e){
                    e.printStackTrace();
                }
            }
        });
        Thread t2=new Thread(new Runnable() {                                  // thread 2 to run consumer
            @Override
            public void run() {
                try{
                    producerConsumerObject.consume();                          // calling consumer
                }
                catch (InterruptedException e){
                    e.printStackTrace();
                }
            }
        });
        t1.start();                                                            // start thread 1
        t2.start();                                                            // start thread 2
        t1.join();
        t2.join();
        if(producerConsumerObject.brokerList.size()!=0){                       //  display unconsumed items
            System.out.println("\nSome Items are not yet consumed! Showing them below.");
            for(DataNode ele: producerConsumerObject.brokerList){
                String msg=ele.getNodeVal("Not Yet Consumed!");
                System.out.println(msg);
            }
        }
        else{
            System.out.println("Consumed Everything the brokerList is empty.");
        }
    }
}
