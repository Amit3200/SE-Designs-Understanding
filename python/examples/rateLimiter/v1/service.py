# author : Amit Singh Sansoya [@amit3200]
from dataclasses import dataclass

@dataclass
class Service:
    service_key_token : str 
    service_name : str 
    service_id : int 
    service_code : int

    def get_servie_token(self):
        return self.service_key_token




class ServiceProvider:
    __instance = None
    service_1 = Service("xaf14gioptyew123oiwe#=", "xaf14", 10231032, 1055)
    def __init__(self):
        if ServiceProvider.__instance != None:
            raise Exception("This is supposed to be a singleton class.")
        else:
            ServiceProvider.__instance = self
    
    @staticmethod
    def get_service():
        if ServiceProvider.__instance == None:
            ServiceProvider()
        return ServiceProvider.__instance
    
    @staticmethod
    def get_token():
        return ServiceProvider.service_1.get_servie_token()


