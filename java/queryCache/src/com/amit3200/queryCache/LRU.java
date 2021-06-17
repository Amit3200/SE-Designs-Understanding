package com.amit3200.queryCache;

import java.util.HashMap;

public class LRU {
    Integer size = 0,capacity = 0;
    public HashMap<String,Node> cache = new HashMap<>();
    Node head = null, tail = null;

    public LRU(){
        this.capacity = 5;
        this.size = 0;
        this.head = null;
        this.tail = null;
    }

    public LRU(Integer capacity){
        this.capacity = capacity;
        this.size = 0;
        this.head = null;
        this.tail = null;
    }

    void removeNode(Node node){
        if(this.size == 1)
            this.head = this.tail = null;
        else{
            Node prev = node.prev;
            Node next = node.next;
            if(prev == null){
                this.head = next;
                head.prev = null;
            }
            else if(next == null){
                this.tail = prev;
                prev.next = null;
            }
            else{
                next.prev = prev;
                prev.next = next;
            }
            node.next = node.prev = null;
        }
        this.size -= 1;
    }

    void addLatest(Node node){
        if(this.size == 0)
            this.head = this.tail = node;
        else{
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
        }
        this.size += 1;
    }



    void updateCache(Node node){
        if(this.tail == node)
            return;
        removeNode(node);
        addLatest(node);
    }

    public Node get(String query){
        if(!cache.containsKey(query))
            return null;
        Node node = cache.get(query);
        updateCache(node);
        return node;
    }

    public void put(String query, String title, String value){
        if(cache.containsKey(query)){
            Node node = cache.get(query);
            node.value = value;
            node.title = title;
            updateCache(node);
        }
        else{
            if(this.size == this.capacity){
                System.out.println("[DEBUG] : Overflow Detected.");
                String invalidCacheKey = this.head.query;
                removeNode(this.head);
                cache.remove(invalidCacheKey);
            }
            Node node = new Node(query,title,value);
            addLatest(node);
            cache.put(query,node);
        }
    }
}
