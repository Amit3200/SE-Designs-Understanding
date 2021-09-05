# author : Amit Singh Sansoya [@amit3200]
from TrieNode import TrieNode
import json
"""
Contains the trie functions so this was required to be generic. We need to pass the required trie node from the 
shard mapper and then we can perform insert,search and show.
"""
BLOCK_INDICATIOR = "="*50

class Trie:
    def __init__(self):
        pass

    @classmethod
    def bfs_trie(cls,root):
        curr = root
        queue = [curr]
        trie_structure = []
        while queue:
            size = len(queue)
            level_nodes = ""
            for idx in range(size):
                ele = queue.pop(0)
                level_nodes += str(ele.letter)
                if idx!= size-1:
                    level_nodes += " - "
                for node in ele.childs:
                    queue.append(ele.childs.get(node))
            trie_structure.append(level_nodes)
        return trie_structure


    @classmethod
    def bfs_prefix_trie(cls,root,word):
        curr = root
        trie_structure = []
        
        for char in word:
            if curr.childs.get(char) != None:
                trie_structure.append(char)
                curr = curr.childs.get(char)
            else:
                print("NO WORD, SKIPPED")
                return []

        more_structure = Trie.bfs_trie(curr)
        if more_structure != []:
            more_structure.pop(0)
        trie_structure.extend(more_structure)
        
        return trie_structure


    def insert(self,root,word,shard_info):
        print(BLOCK_INDICATIOR)
        print("RUNNING : INSERT")
        curr = root 
        for char in word:
            if curr.childs.get(char) == None:
                curr.childs[char] = TrieNode(char = char,shard_info = shard_info)
            curr = curr.childs.get(char)
        curr.set_is_end()
        curr.set_full_word(word)
        print("{word} : INSERT SUCCESSFULL".format(word = word))
        response = {'status':'SUCCESS','query_action':'insert','word':word}
        print("RESPONSE GENERATED, RQ: {rq}".format(rq = json.dumps(response)))
        print(BLOCK_INDICATIOR)
        return response


    def search(self,root,word):
        print(BLOCK_INDICATIOR)
        print("RUNNING : SEARCH")
        curr = root 
        response = {'status':'NOT FOUND','query_action':'search','word':word}
        for char in word:
            if curr.childs.get(char) == None:
                break
            curr = curr.childs.get(char)
        if curr.get_is_end():
            response['status'] = 'FOUND'
        print("ENDING : SEARCH")
        print("RESPONSE GENERATED, RQ: {rq}".format(rq = json.dumps(response)))
        print(BLOCK_INDICATIOR)
        return response
                
    

    def show(self,root):
        print(BLOCK_INDICATIOR)
        print("RUNNING : SHOW")
        trie_structure = Trie.bfs_trie(root)
        for lvl in trie_structure:
            print(lvl)
        print("ENDING : SHOW")
        print(BLOCK_INDICATIOR)


    def prefix_show(self,root,word):
        print(BLOCK_INDICATIOR)
        print("RUNNING : PREFIX_SHOW")
        trie_structure = Trie.bfs_prefix_trie(root,word)
        for lvl in trie_structure:
            print(lvl)
        print("ENDING : PREFIX_SEARCH")
        print(BLOCK_INDICATIOR)
    
