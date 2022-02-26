// @amit3200 [Amit Singh Sansoya]
// It was all meant to happen as I was all talk.
#include<bits/stdc++.h>
using namespace std;

/*
Design a linkedlist in a way that every first element has pointer to down 
and every level has not more then 4 elements.
Desigin efficient insert(), delete()

Consider
1. Distinct elements
*/
class Node{
    public:
    int data;
    Node *next, *down;
    bool is_first = false;
    Node(int val, bool is_first = false){
        data = val;
        next = nullptr;
        down = nullptr;
        this->is_first = is_first;
    }
}*root;


void build_ll_1(){
    root = new Node(2, true);
    Node *ele = root;
    ele->next = new Node(7);
    ele->next->next = new Node(8);
    ele->next->next->next = new Node(11);
    if(ele->is_first){
        ele->down = new Node(13,true);
        ele->down->next = new Node(16);
        ele->down->next->next = new Node(17);
        ele->down->next->next->next = new Node(21);
    }
    if(ele->down->is_first){
        ele->down->down = new Node(30,true);
        ele->down->down->next = new Node(32,true);
    }
}

void print_ll_v1(Node *root){
    cout<<"==========================================\n";
    int lvl = 0;
    Node *ptr = root;
    queue<Node*> q;
    q.push(root);
    while(!q.empty()){
        auto ele = q.front();
        q.pop();
        if(ele->down){
            q.push(ele->down);
        }
        while(ele){
            cout<<ele->data<<" ";
            ele = ele->next;
        }
        cout<<"\n";
    }
}

// not efficient (ne)
Node *ne_adjust(Node *parent){
    Node *ptr = parent;
    queue<Node*> q;
    q.push(parent);
    vector<Node*> res;
    while(!q.empty()){
        auto ele = q.front();
        q.pop();
        if(ele->down){
            q.push(ele->down);
        }
        while(ele){
            res.push_back(ele);
            ele = ele->next;
        }
    }
    for(int i = 0 ; i < res.size(); i += 4){
        auto ele = res[i];
        int idx = 0;
        while(idx < 4 && i+idx < res.size()){
            res[i+idx]->next = res[i+idx+1];
            res[i+idx]->down = nullptr;
            res[i+idx]->is_first = false;
            idx += 1;
        }
        res[i+idx-1]->next = nullptr;
        ele->is_first = true;
        if(i+4 < res.size()){
            ele->down = res[i+4];
        }
        else{
            ele->down = nullptr;
        }
    }
    return parent;
}

// not efficient (ne)
Node* ne_insert(Node *parent,int val){
    Node *ptr = parent;
    bool inserted = false;
    queue<Node*> q;
    q.push(parent);
    int level = 0;
    while(!q.empty()){
        auto ele = q.front();
        q.pop();
        if(ele->down){
            q.push(ele->down);
            level += 1;
        }
        if((ele->down && ele->down->data > val) || (q.size() == 0 && !ele->down)){
            while(ele){
                // handle at start add
                if(ele->data > val){
                    Node *node = new Node(val,true);
                    ele->is_first = false;
                    node->next = ele;
                    node->down = ele->down;
                    ele->down = nullptr;
                    inserted = true;
                    if(level == 1){
                        parent = node;
                    }
                    break;
                }

                if(ele->data < val && (ele->next && ele->next->data > val)){
                    Node *node = new Node(val);
                    node->next = ele->next;
                    ele->next = node;
                    inserted = true;
                    break;
                }

                // handle at end add
                if(ele->data < val && !ele->next){
                    Node *node = new Node(val);
                    ele->next = node;
                    inserted = true;
                    break;
                }
                ele = ele->next;
            }
        }
        if(inserted)
            break;
    }
    parent = ne_adjust(parent);
    return parent;
}


// not efficient (ne)
Node* ne_delete(Node *parent,int val){
    // need to implement
    queue<Node*> q;
    q.push(parent);
    int level = 0;
    bool deleted = false;
    while(!q.empty()){
        auto ele = q.front();
        q.pop();
        if(ele->down){
            q.push(ele->down);
            level += 1;
        }
        if((ele->down && ele->down->data > val) || (q.size() == 0 && !ele->down)){
            int idx = 0;
            while(ele){
                // head delete;
                if(ele->data == val && idx == 0){
                    ele->next->down = ele->down;
                    if(level == 1){
                        parent = ele->next;
                    }
                    deleted = true;
                    break;
                }
                else{
                    if(ele->next->data == val){
                        if(ele->next->next){
                            ele->next = ele->next->next;
                        }
                        else{
                            ele->next = nullptr;
                        }
                        deleted = true;
                        break;
                    }
                }
                idx += 1;
                if(deleted)
                    break;
                ele = ele->next;
            }
        }
        if(deleted)
            break;
    }
    parent = ne_adjust(parent);
    return parent;
}

int main(){
    build_ll_1();
    print_ll_v1(root);
    root = ne_insert(root,6);
    root = ne_insert(root,1);
    root = ne_insert(root,27);
    root = ne_insert(root,45);
    root = ne_insert(root,12);
    root = ne_insert(root,31);
    root = ne_insert(root,25);
    root = ne_insert(root,38);
    root = ne_insert(root,53);
    root = ne_insert(root,10);
    print_ll_v1(root);
    root = ne_delete(root,31);
    print_ll_v1(root);
    root = ne_delete(root,2);
    print_ll_v1(root);
    root = ne_delete(root,10);
    print_ll_v1(root);
    root = ne_delete(root,32);
    print_ll_v1(root);
    root = ne_delete(root,1);
    print_ll_v1(root);
    cout<<"End\n";
}

// Outputs
// ==========================================
// 2 7 8 11 
// 13 16 17 21 
// 30 32 
// ==========================================
// 1 2 6 7 
// 8 10 11 12 
// 13 16 17 21 
// 25 27 30 31 
// 32 38 45 53 
// ==========================================
// 1 2 6 7 
// 8 10 11 12 
// 13 16 17 21 
// 25 27 30 32 
// 38 45 53 
// ==========================================
// 1 6 7 8 
// 10 11 12 13 
// 16 17 21 25 
// 27 30 32 38 
// 45 53 
// ==========================================
// 1 6 7 8 
// 10 11 12 13 
// 16 17 21 25 
// 27 30 32 38 
// 45 53 
// ==========================================
// 1 6 7 8 
// 10 11 12 13 
// 16 17 21 25 
// 27 30 38 45 
// 53 
// ==========================================
// 6 7 8 10 
// 11 12 13 16 
// 17 21 25 27 
// 30 38 45 53 