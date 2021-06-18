# author : Amit Singh Sansoya [@amit3200]
"""
ShardClassifier is nothing but a singleton class which behaves as service and has responsibility of returning the 
trie node when asked if the request has following region and partition.
"""
class ShardClassifier:
    __instance = None
    __shard_mapper = None
    @staticmethod
    def get_instance():
        if ShardClassifier.__instance == None:
            ShardClassifier()
        return ShardClassifier.__instance
    
    def __init__(self,trie_root_mapper):
        if ShardClassifier.__instance != None:
            raise Exception("ShardClassifier is a Singleton Class.")
        else:
            ShardClassifier.__instance = self 
            self.__shard_mapper = {
                'region-1':{
                    'r1-catcher-1':trie_root_mapper.get('r1c1'),
                    'r1-catcher-2':trie_root_mapper.get('r1c2'),
                    'r1-misc-catcher':trie_root_mapper.get('r1mc')
                },
                'region-2':{
                    'r2-catcher-1':trie_root_mapper.get('r2c1'),
                    'r2-catcher-2':trie_root_mapper.get('r2c2'),
                    'r2-misc-catcher':trie_root_mapper.get('r2mc')
                },
                'region-3':{
                    'r3-catcher-1':trie_root_mapper.get('r3c1'),
                    'r3-catcher-2':trie_root_mapper.get('r3c2'),
                    'r3-misc-catcher':trie_root_mapper.get('r3mc')
                },
                'region-4':{
                    'r4-catcher-1':trie_root_mapper.get('r4c1'),
                    'r4-catcher-2':trie_root_mapper.get('r4c2'),
                    'r4-misc-catcher':trie_root_mapper.get('r4mc')
                }
            }
    
    def get_trie_root_by_shard_id(self,location,partition):
        trie_root = self.__shard_mapper.get(location,None).get(partition,None)
        if trie_root != None:
            return trie_root


