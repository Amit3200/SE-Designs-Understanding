# author : amit3200 [Amit Singh Sansoya]
from abc import ABC, abstractmethod
class PLAN(ABC):
    rate: float
    block_date: float
    
    def __init__(self):
        pass

    @abstractmethod
    def get_rate(self):
        pass

    def calculate_bill(self,msg,units):
        msg = "{msg} [ Bill ] : {amount}".format(msg = msg,amount = units * self.rate)
        print(msg)
    

