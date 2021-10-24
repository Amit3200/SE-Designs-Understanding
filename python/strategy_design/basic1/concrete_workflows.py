from strategy import Strategy
import random
class ConcreteWorkFlow_A(Strategy):
    
    def execute(self, args):
        print("[Algorithm] : Sorted")
        return sorted(args, key = lambda x : (len(x),x))

class ConcreteWorkFlow_B(Strategy):
    
    def execute(self, args):
        print("[Algorithm] : Sorted & Reversed")
        return sorted(args, reverse = True, key = lambda x : (len(x),x))

class ConcreteWorkFlow_C(Strategy):
    
    def execute(self, args):
        print("[Algorithm] : Shuffled")
        random.shuffle(args)
        return args


    
        
