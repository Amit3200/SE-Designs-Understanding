# author : Amit Singh Sansoya [@amit3200]
# TrieNode : TrieNode Definition
from collections import defaultdict

class TrieNode:
    def __init__(self,shard_info, char = None):
        self.childs             = defaultdict(None)
        self.letter             = char
        self.is_end             = False
        self.full_word          = None
        self.shard_id           = shard_info.get('location',None)
        self.partition_key      = shard_info.get('partition',None)
    

    def set_full_word(self,word):
        self.full_word = word 
    

    def set_is_end(self):
        self.is_end = True
    

    def get_is_end(self):
        return self.is_end