from concrete_workflows import ConcreteWorkFlow_A, ConcreteWorkFlow_B, ConcreteWorkFlow_C
from context import Context

def create_context(args):
    if args == "A":
        return Context(ConcreteWorkFlow_A())
    elif args == "B":
        return Context(ConcreteWorkFlow_B())
    elif args == "C":
        return Context(ConcreteWorkFlow_C())
    else:
        return Exception("Invalid args")

vals = ["abc","a","def","b","d","e","xy","lki","poq","ghfu"]
context = create_context("A")
context.run_algorithm(vals)
context = create_context("C")
context.run_algorithm(vals)
context = create_context("B")
context.run_algorithm(vals)