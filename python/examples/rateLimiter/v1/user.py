# author : Amit Singh Sansoya [@amit3200]
"""
User is nothing but a user class
Generates user_id
Contains the window object which holds the logs of the user.
"""
import time
from collections import defaultdict
from service import sp



class User:
    name : str 
    creation_id : str 
    user_id : str 
    window : defaultdict(list)
    service_provider = sp

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
    
    def get_service_access(self):
        return self.service_provider.access_service(self)



    
