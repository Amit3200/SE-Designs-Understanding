// @amit3200 [Amit Singh Sansoya]
// It was all meant to happen as I was all talk.
/*
    Time Taken to code : 1hour 50 mins
    Design a url shortner service (base 62 simple hashing) however the following things should be satisfied
    -> user should generate short url                                        :  get_short_url("www.xyz.com/example") -> abcde;
    -> other user should generate be able to access long url using short_url :  get_long_url("abcde") -> www.xyz.com/example;
    -> user should be able to history of generated and so far mapped urls

    Issues not handled while coding:
        Doenst handle duplicates as of now
    
    SOLID ? [Tried]

    CLASS USER          -> USER CLASS (user name, user id) GET()
    CLASS URL_NODE      -> URL NODE (url related info created, expiry, urlid)
    CLASS URL_SERVICE   -> generate(), get(), maps()    [algo() hidden as private]

*/
#include<bits/stdc++.h>
using namespace std;
#define lld long long int
lld run_user_id = 100;
lld run_url_id = 5000;

lld get_run_user_id(){
    run_user_id += 1;
    return run_user_id;
}

lld get_run_url_id(){
    run_url_id += 1;
    return run_url_id;
}

class URL_NODE{
    public:
    lld url_id;
    string long_url;
    string short_url;
    lld creation_timestamp;
    lld validity_timestamp;
    URL_NODE(string &long_url){
        this->url_id        = get_run_url_id();
        this->long_url      = long_url;
        this->creation_timestamp = 11;
        this->validity_timestamp = -1; 
    }
};

class URL_SERVICE{
    private:
    map<lld,URL_NODE*> url_id_to_url_node_mapper;       // url_id to Node mapper;
    map<string,lld> short_url_to_url_id_mapper;         // short url to url_id mapper;
    map<lld,vector<lld>> user_id_to_url_id_mapper;      // user_id to url_id mapper;

    
    lld generate_url_id(string long_url){
        URL_NODE* url_node = new URL_NODE(long_url);
        url_id_to_url_node_mapper[url_node->url_id] = url_node;
        return url_node->url_id;
    }

    string generate_short_url(lld url_id){
        string short_url = "";
        char character_set[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        lld parsing_url_id = url_id;
        while(parsing_url_id){
            short_url.push_back(character_set[parsing_url_id%62]);
            parsing_url_id = parsing_url_id/62;
        }
        reverse(short_url.begin(),short_url.end());
        url_id_to_url_node_mapper[url_id]->short_url = short_url;
        return short_url;
    }   

    public:
    string generate_url(string &long_url,lld user_id){
        lld url_id = generate_url_id(long_url);
        string short_url = generate_short_url(url_id);
        short_url_to_url_id_mapper[short_url] = url_id;
        user_id_to_url_id_mapper[user_id].push_back(url_id);
        return short_url;
    }

    void show_urls(lld user_id){
        if(user_id_to_url_id_mapper.find(user_id) == user_id_to_url_id_mapper.end()){
            cout<<"No url in system for user "<<user_id<<"\n"; 
            return;
        }
        cout<<"SHOW URL START\n";
        cout<<"INFO\n";
        cout<<"===============================\n";
        cout<<"User : "<<user_id<<"\n";
        for(auto url_ids : user_id_to_url_id_mapper[user_id]){
            cout<<url_id_to_url_node_mapper[url_ids]->long_url<<"                                       :  "<<url_id_to_url_node_mapper[url_ids]->short_url<<"\n";
        }
        cout<<"SHOW URL END\n\n\n";
    }

    string get_url(string &short_url){
        if(short_url_to_url_id_mapper.find(short_url) == short_url_to_url_id_mapper.end()){
            cout<<"Short url has no mapping in system\n";
            return "invalid";
        }
        return url_id_to_url_node_mapper[short_url_to_url_id_mapper[short_url]]->long_url;
    }
}*url_service;

class USER{
    private:
    lld uid;
    string name;

    public:
    USER(string name){
        this->name = name;
        this->uid  = get_run_user_id();
    }

    string get_short_url(string &long_url){
        string short_url = url_service->generate_url(long_url,uid);
        return short_url;
    }

    string get_long_url(string &short_url){
        string long_url = url_service->get_url(short_url);
        return long_url;
    }

    void show_url_history(){
        url_service->show_urls(uid);
    }
};

int main(){
    url_service = new URL_SERVICE();
    USER* archer = new USER("Archer");
    USER* takumi = new USER("takumi");
    USER* kira   = new USER("kira");
    string url1 = "www.google.com/abcdefghij";
    string url2 = "www.workcode.com/wiok1lse";
    string url3 = "opq1adcxc";
    string url4 = "www.wwe123xcode.com/wiok1lse";
    string s1 = archer->get_short_url(url1);
    cout<<"Archer generated : "<<s1<<"\n";
    cout<<"Takumi hit "<<s1<<" and got : "<<takumi->get_long_url(s1)<<"\n";
    string s2 = takumi->get_short_url(url2);
    cout<<"Takumi generated : "<<s2<<"\n";
    cout<<"Archer hit "<<s2<<" and got : "<<archer->get_long_url(s2)<<"\n";
    string s3 = archer->get_short_url(url4);
    cout<<"Archer generated : "<<s3<<"\n";
    cout<<"Kira hit "<<s2<<" and got : "<<kira->get_long_url(s2)<<"\n";
    cout<<"Kira hit "<<s1<<" and got : "<<kira->get_long_url(s1)<<"\n";
    cout<<"Kira hit "<<url3<<" and got : "<<kira->get_long_url(url3)<<"\n";
    cout<<"\n\n";
    archer->show_url_history();
    takumi->show_url_history();
    kira->show_url_history();
}

