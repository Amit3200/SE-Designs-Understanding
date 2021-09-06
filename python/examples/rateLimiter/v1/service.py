# author : Amit Singh Sansoya [@amit3200]

"""
Service class the service user wants to access and we want to restrict by applying rate limiter.
"""
from dataclasses import dataclass
import rateLimiterDs

rq = rateLimiterDs.rq
@dataclass
class Service:
    service_key_token : str 
    service_name : str 
    service_id : int 
    service_code : int

    def get_servie_token(self):
        return self.service_key_token



"""
Service Provider creates the services and returns as per the user request. as of now only 1.
"""
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
    
    def access_service(self,user):
        response = rq.process(user.get_helper_user_id())
        if response[0]:
            user.window["Allowed"].append(response[1])
            return self.get_token()
        else:
            user.window["Failed"].append(response[1])
            return "Request Throttled. Try again later."

sp = ServiceProvider()

