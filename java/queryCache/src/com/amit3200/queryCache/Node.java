package com.amit3200.queryCache;

public class Node {
    String query;
    String title;
    String value;
    Node prev, next;

    Node(String query, String value){
        this.query = query;
        this.value = value;
        this.prev  = null;
        this.next  = null;
    }

    Node(String query, String title,String value){
        this.query = query;
        this.title = title;
        this.value = value;
        this.prev  = null;
        this.next  = null;
    }
}
