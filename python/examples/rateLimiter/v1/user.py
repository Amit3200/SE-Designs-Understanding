# author : Amit Singh Sansoya [@amit3200]
import time
from collections import defaultdict

class User:
    name : str 
    creation_id : str 
    user_id : str 
    window : defaultdict(list)

    @staticmethod
    def get_creation_id() -> str:
        return "T#21#{curr_time}".format(curr_time = int(time.time()))
    
    def get_user_id(self) -> str:
        id_name = "{name}_U#{creation_id}".format(name = self.name.lower(),creation_id = self.creation_id)
        return id_name

    def __init__(self, name):
        self.name :str = name
        self.creation_id :str = self.get_creation_id()
        self.user_id :str = self.get_user_id()
        self.window = defaultdict(list)
    

    def get_helper_user_id(self):
        return self.user_id
    
    def get_service_access(self,rq):
        response = rq.process(self.get_helper_user_id())
        if response[0]:
            self.window["Allowed"].append(response[1])
        else:
            self.window["Failed"].append(response[1])


    
