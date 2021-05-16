# author : amit3200 [Amit Singh Sansoya]
from plan import PLAN 

class COMMERCIAL_PLAN(PLAN):
    domestic_rate = 7.5
    def get_rate(self):
        self.rate = self.domestic_rate
        
