# author : Amit Singh Sansoya [@amit3200]
"""
User.py
Creating user with the minimum requirements.
Immutable Object just for fun so that if we return user object somewhere we are not changing value using that object value.
"""

from datetime import datetime
from dataclasses import dataclass, field

@dataclass(frozen = True)
class User:
    
    user_name : str 
    user_id : str = field(init = False)
    creation_time : str = field(init = False)

    def create_user_id(self,user_name) -> str:
        return "@{user_name}#{arbitary}".format(user_name = user_name.lower(), arbitary = int(datetime.timestamp(datetime.now())))
    
    def create_creation_time(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __post_init__(self):
        object.__setattr__(self,'user_id',self.create_user_id(self.user_name))
        object.__setattr__(self,'creation_time',self.create_creation_time())
    
    def get_user_id(self):
        return self.user_id

    def display(self):
        print(self)

