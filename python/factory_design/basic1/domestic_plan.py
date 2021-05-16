# author : amit3200 [Amit Singh Sansoya]
from plan import PLAN 

class DOMESTIC_PLAN(PLAN):
    domestic_rate = 3.5
    def get_rate(self):
        self.rate = self.domestic_rate
        
