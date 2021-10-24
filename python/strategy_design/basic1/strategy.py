from abc import ABC, abstractclassmethod, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def execute(args):
        pass