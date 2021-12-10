# author : Amit Singh Sansoya [@amit3200]
from abc import ABC, abstractmethod
class Logger(ABC):

    @abstractmethod
    def start(self, process_id, start_time):
        pass

    @abstractmethod
    def finish(self, process_id, end_time):
        pass

    @abstractmethod
    def log(self):
        pass
