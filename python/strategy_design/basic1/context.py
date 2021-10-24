from strategy import Strategy
class Context:

    def __init__(self, strategy : Strategy) -> None:
        self._strategy = strategy
    
    def get_strategy(self) -> Strategy:
        return self._strategy
    
    def set_strategy(self, strategy : Strategy) -> None:
        self._strategy = strategy
    
    def run_algorithm(self, args) -> None:
        # print("[Before running algorithm] : {args}".format(args = args))
        ex_args = self._strategy.execute(args)
        print("[After running algorithm] : {args}".format(args = ex_args))




