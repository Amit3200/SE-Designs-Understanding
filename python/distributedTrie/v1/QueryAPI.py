# author : Amit Singh Sansoya [@amit3200]

import json
import string
import threading
from Trie import Trie

class QueryAPI:

    def __init__(self,request, shard_instance):
        self.request = request
        self.shard_instance = shard_instance
        self.allowed_actions = ['search','show','insert','prefix_show']
        self.process_controller()
    
    def clean_key(self,word):
        new_key = ""
        if word:
            for wchar in word.lower():
                if wchar in string.ascii_lowercase:
                    new_key +=  wchar
        return new_key
    
    def process_controller(self):
        key = self.clean_key(self.request.get('query_key',None))
        action_key = self.request.get('action',None)
        if action_key in self.allowed_actions:
            shard_info = {'location':self.request.get('location',None),'partition':self.request.get('partition',None)}
            trie_driver = Trie()
            root = self.shard_instance.get_trie_root_by_shard_id(shard_info.get('location'),shard_info.get('partition'))
            if trie_driver != None and root != None:
                print("RUNNING REQUEST, RQ {rq}".format(rq = json.dumps(self.request)))
                if action_key == 'search':
                    search_task = threading.Thread(target = trie_driver.search, args=(root,key,))
                    print(search_task)
                    search_task.start()
                    search_task.join()
                elif action_key == 'insert':
                    insert_task = threading.Thread(target = trie_driver.insert, args=(root,key,shard_info))
                    insert_task.start()
                    insert_task.join()
                elif action_key == 'show':
                    show_task = threading.Thread(target = trie_driver.show, args = (root,))
                    show_task.start()
                    show_task.join()
                elif action_key == 'prefix_show':
                    prefix_show_task = threading.Thread(target = trie_driver.prefix_show, args=(root,key,))
                    prefix_show_task.start()
                    prefix_show_task.join()
            else:
                print("REQUEST CANNOT BE SERVED. SHARD OR PARTITION DOESN'T EXIST. RQ : {rq}".format(rq = json.dumps(self.request)))







