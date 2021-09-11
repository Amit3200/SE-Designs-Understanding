# author : Amit Singh Sansoya [@amit3200]
import json
from datetime import datetime
from typing import OrderedDict
from user import User
from collections import defaultdict, deque
from utils import fakedb, Utils
from shortner_algo import Shortner_Algo,BaseX_Algo


class Shortner_Service:
    VALID_DATA_STORE : deque = deque([])
    USED_DATA_STORE : defaultdict = defaultdict(OrderedDict)
    SUPPORTED_URL_CAPACITY = None

    def __init__(self, capacity : int, service : Shortner_Algo):
        self.SUPPORTED_URL_CAPACITY = capacity
        self.VALID_DATA_STORE = service.generate_short_url(self.SUPPORTED_URL_CAPACITY)
    

    #after .com part only
    def assign(self,user : User,big_url : str):
        if len(self.VALID_DATA_STORE) == 0:
            print("[Exhausted] Assign Requested but Service Failed! All Short Urls Exhausted.")
        
        elif fakedb.is_already_short(big_url) == False:
            short_url_detail = self.VALID_DATA_STORE.popleft()
            token = Utils().get_db_token(user,big_url,short_url_detail)
            fakedb.create_entry(token)
            self.USED_DATA_STORE[token.get('short_url')] = {'url':token.get('short_url'),'validity_time':token.get('validity_time'), 'encoding_number' : short_url_detail.get('encoding_number')}
            #   just to understand
            print("[Assigned] {user_id} assgined : {big_url} to {short_url}".format(**token))
            return token.get('short_url')
        
        else:
            print("[Already Assigned] {big_url} to {short_url}".format(big_url = big_url,short_url = fakedb.big_url_lookup.get(big_url)))

    
    def fetch(self,user: User,short_url:str):
        token = fakedb.fetch_entry(short_url)
        if token != None:
            if token.get('validity_time') > datetime.now():
                print("[Fetched] {user} fetched {short_url} redirecting to {big_url}".format(user = user.get_user_id(),  short_url = short_url, big_url = token.get('big_url')))
                return token.get('big_url')
            else:
                expired = self.USED_DATA_STORE.pop(short_url)
                valid_token = expired.copy()
                del valid_token['validity_time']
                self.VALID_DATA_STORE.append(valid_token)
                del fakedb.big_url_lookup[fakedb.db.get(short_url).get('big_url')]
                print("[Expired] Short Url {short_url} expired.".format(short_url = short_url))
        else:
            print("[Not in Existence] The url doesnt exisits.")
        return False
    
    def show_created_url(self):
        print(json.dumps({"valid_data_store":list(self.VALID_DATA_STORE)},indent = 4))
        print(json.dumps({"used_data_store":list(self.USED_DATA_STORE)},indent = 4))


class Generate_Service_Factory():
    algo_type = None
    service_type = None
    def __init__(self,algo_type):
        self.algo_type = algo_type
        
    
    def get_service(self):
        if self.algo_type.lower() == "basex":
            self.service_type = BaseX_Algo()
        return self.service_type



