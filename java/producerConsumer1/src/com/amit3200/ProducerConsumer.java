package com.amit3200;

import java.util.LinkedList;
import static com.amit3200.Main.*;

public class ProducerConsumer {
    LinkedList<DataNode> brokerList=new LinkedList<DataNode>(); // broker queue
    int maxBufferCapacity=5;        // broker queue size

    public void produce() throws InterruptedException{          // producer cooking data
        int currentCookingItem=0;
        while(terminatorValue<=TerminateProcess){
            synchronized (this){
                while(brokerList.size()==maxBufferCapacity){
                    wait();
                }
                DataNode ele=new DataNode(currentCookingItem);
                System.out.println("Producer Currently Cooking - "+ele.getNodeVal("Producer"));
                currentCookingItem++;
                terminatorValue+=1;
                brokerList.add(ele);
                notify();
                Thread.sleep(1000);
            }
        }
    }

    public void consume() throws InterruptedException{      // consumer eating data
        while (terminatorValue<=TerminateProcess){
            synchronized (this){
                while(brokerList.size()==0){
                    wait();
                }
                DataNode ele=brokerList.removeFirst();
                System.out.println("Consumer Consuming - Node Date:"+ele.getNodeVal("Consumer"));
                terminatorValue+=1;
                notify();
                Thread.sleep(1000);
            }
        }
    }
}
