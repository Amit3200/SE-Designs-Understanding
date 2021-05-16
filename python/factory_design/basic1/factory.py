# author : amit3200 [Amit Singh Sansoya]
from commercial_plan import COMMERCIAL_PLAN
from domestic_plan import DOMESTIC_PLAN
import json

class FACTORY_CONTROL:
    current_plan = None 
    purchase_unit = None
    domestic_abbr = ['DOM','DOMESTIC']
    commercial_abbr = ['COMR','COMMERCIAL']
    
    def __init__(self,current_plan,purchase_unit):
        self.current_plan = current_plan
        self.purchase_unit = purchase_unit
        factory_instance = self.controller()
        factory_instance.get_rate()
        msg = 'FOR PLAN {plan} and UNITS {units}'.format(plan = self.current_plan,units = self.purchase_unit)
        factory_instance.calculate_bill(msg,self.purchase_unit)
    
    def controller(self):
        plan_instance = None 
        if self.current_plan.upper() in self.domestic_abbr:
            plan_instance = DOMESTIC_PLAN()
        elif self.current_plan.upper() in self.commercial_abbr:
            plan_instance = COMMERCIAL_PLAN()
        else:
            pass 
        return plan_instance



obj1 = FACTORY_CONTROL("DOM",5)
obj2 = FACTORY_CONTROL("dom",8)
obj3 = FACTORY_CONTROL("COMR",9)
obj4 = FACTORY_CONTROL("commercial",5)
obj5 = FACTORY_CONTROL("comr",3)