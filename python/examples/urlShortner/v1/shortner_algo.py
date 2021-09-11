import random
from collections import defaultdict, deque
from typing import OrderedDict
from string import ascii_letters
from abc import ABC, abstractmethod, abstractproperty

class Shortner_Algo(ABC):
    short_url_storage : deque = deque([])
    def __init__(self):
        pass 

    @abstractmethod
    def generate_short_url(self,capacity):
        return

    @abstractmethod
    def filter_url(self):
        pass

class BaseX_Algo(Shortner_Algo):
    def to_baseX(self, encoding_number):
        character_set = "0123456789{letters}".format(letters = ascii_letters)
        hash_str = ""
        while encoding_number > 0:
            hash_str = character_set[encoding_number%62] + hash_str
            encoding_number = encoding_number // 62
        hash_str = hash_str[::-1]
        return hash_str
    
    def generate_short_url(self,capacity):
        start_value = 519520
        shuffled_encoding_list = list(range(start_value,start_value+capacity))
        random.shuffle(shuffled_encoding_list)
        for encoding_number in shuffled_encoding_list:
            short_url = self.to_baseX(encoding_number)
            self.short_url_storage.append({'url':short_url, 'encoding_number':encoding_number})
        return self.short_url_storage

    def filter_url(self):
        pass

