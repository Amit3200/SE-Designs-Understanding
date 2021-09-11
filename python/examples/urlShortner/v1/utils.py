# author : Amit Singh Sansoya [@amit3200]
import json
from collections import defaultdict
from datetime import datetime, timedelta
class FakeDb():
    db : dict = {}
    big_url_lookup : dict = {}

    def __init__(self):
        pass 

    def create_entry(self,token:dict):
        self.db.update({token.get('short_url'):token})
        self.big_url_lookup[token.get('big_url')] = token.get('short_url')
    
    def is_already_short(self,big_url):
        if big_url in self.big_url_lookup:
            return True 
        return False


    def fetch_entry(self,key:str):
        return self.db.get(key,None)

    def show_db(self):
        for records in self.db:
            print(self.db[records])

fakedb = FakeDb()

class Utils:
    def __init__(self):
        pass

    def get_db_token(self,user,big_url,short_url_detail):
        short_url = short_url_detail.get('url')
        user_id = user.get_user_id()
        big_url = big_url
        creation_time = datetime.now()
        validity = creation_time + timedelta(minutes = 1)
        db_token = {
            "user_id":user_id,
            "big_url":big_url,
            "short_url":short_url,
            "creation_time":creation_time,
            "validity_time":validity
        }
        return db_token