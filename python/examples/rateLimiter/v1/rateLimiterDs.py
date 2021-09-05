# author : Amit Singh Sansoya [@amit3200]
from datetime import datetime, timedelta
from service import ServiceProvider as serve
from collections import OrderedDict,defaultdict
import copy

class RateLimiterDs:
    RATE_LIMITER_DS = defaultdict(OrderedDict)
    HARD_RATE_LIMIT = 5
    TIME_LIMIT = 60
    __instance = None
    
    @staticmethod
    def getRateLimiter():
        if RateLimiterDs.__instance == None:
            RateLimiterDs()
        return RateLimiterDs.__instance
    
    def __init__(self):
        if RateLimiterDs.__instance != None:
            raise Exception ("RateLimiterDs should be singleton.")
        else:
            RateLimiterDs.__instance = self
    


class RequestProcessor(RateLimiterDs):
    rlds = RateLimiterDs.RATE_LIMITER_DS


    @staticmethod
    def get_current_time_key():
        return int(datetime.timestamp(datetime.now()))

    def show_status(self,msg):
        print(msg)

    def assign_new_bucket(self, user_id):
        ts = self.get_current_time_key()
        user_bucket = OrderedDict({ts:1})
        self.rlds[user_id] = user_bucket
        msg = "[Accepted] {user_id} : request added at ts {ts}, current count : {cs}".format(user_id = user_id, ts = ts, cs = 1)
        self.show_status(msg)
        return ts

    def process(self,user_id):
        ts = None
        served = False
        condition_satisfied = False
        current_entries = self.rlds.get(user_id,None)
        current_entries_copy = copy.deepcopy(current_entries)
        if current_entries == None:
            served = True 
            condition_satisfied = True
            ts = self.assign_new_bucket(user_id)
        else:
            ts = self.get_current_time_key()
            for time in current_entries_copy:
                if ts-time <= RateLimiterDs.TIME_LIMIT:
                    if sum(current_entries.values()) + 1 <= RateLimiterDs.HARD_RATE_LIMIT:
                        current_entries[ts] = current_entries.get(ts,0) + 1
                        self.rlds[user_id] = current_entries
                        served = True
                        condition_satisfied = True
                        msg = "[Accepted] {user_id} : request added at ts {ts}, current count : {cs}".format(user_id = user_id, ts = ts, cs = sum(current_entries.values()))
                        self.show_status(msg)
                        break
                    else:
                        msg = "[Rejected] {user_id} : request failed at ts {ts}, current count : {cs}".format(user_id = user_id, ts = ts, cs = sum(current_entries.values()))
                        self.show_status(msg)
                        break
                else:
                    # need to know before deleting
                    msg = "[Deleting] {user_id} : request expired for ts {ts}, current count : {cs}, expired.".format(user_id = user_id, ts = time, cs = sum(current_entries.values()))
                    self.show_status(msg)
                    if time in current_entries:
                        del current_entries[time]
                    condition_satisfied = True
                    self.rlds[user_id] = current_entries
        if served == False and condition_satisfied == True:
            served = True
            ts = self.assign_new_bucket(user_id)                    
        return [served, ts]


                
    
    



    

