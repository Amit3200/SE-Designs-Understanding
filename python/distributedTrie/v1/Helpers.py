# author : Amit Singh Sansoya [@amit3200]
from TrieNode import TrieNode
from collections import defaultdict
"""
This is just a helper program which initializes the trie node and shards as per the location.
Here we maintain the hashmap for the node as per shard so that the request when comes can be directed to the shard.
"""
tr1c1 = None
tr1c2 = None
tr1mc = None
tr2c1 = None
tr2c2 = None
tr3c1 = None
tr3c2 = None
tr4c1 = None
tr4mc = None
#shard information
shard_info_tr1c1={'location':'region-1','partition':'r1-catcher-1'}
shard_info_tr1c2={'location':'region-1','partition':'r1-catcher-2'}
shard_info_tr1mc={'location':'region-1','partition':'r1-misc-catcher'}
shard_info_tr2c1={'location':'region-2','partition':'r2-catcher-1'}
shard_info_tr2c2={'location':'region-2','partition':'r2-catcher-2'}
shard_info_tr3c1={'location':'region-3','partition':'r3-catcher-1'}
shard_info_tr3c2={'location':'region-3','partition':'r3-catcher-2'}
shard_info_tr4c1={'location':'region-4','partition':'r4-catcher-1'}
shard_info_tr4mc={'location':'region-4','partition':'r4-misc-catcher'}

trie_dictionary = [['amit',shard_info_tr1mc],['work',shard_info_tr1c2],['beat',shard_info_tr2c1],['alpha-human',shard_info_tr2c1],['beta-testing',shard_info_tr4mc],['floating',shard_info_tr4c1],['crossing',shard_info_tr3c2],['exclusive',shard_info_tr3c1],['allotropic',shard_info_tr2c2],['allocation',shard_info_tr2c2],['allogeneic',shard_info_tr2c2],['allosteric',shard_info_tr2c2],['allopatric',shard_info_tr2c2],['allocution',shard_info_tr2c2],['allocators',shard_info_tr2c2],['allocating',shard_info_tr2c2],['allocation',shard_info_tr2c2],['allogamies',shard_info_tr2c2],['allogamous',shard_info_tr2c2],['allometric',shard_info_tr2c2],['allografts',shard_info_tr2c2]]

show_requests = [{
        'action':'show',
        'location':shard_info_tr1c2.get('location'),
        'partition':shard_info_tr1c2.get('partition')
        },
        {
        'action':'show',
        'location':shard_info_tr1c1.get('location'),
        'partition':shard_info_tr1c1.get('partition')
        },
        {
        'action':'search',
        'query_key':'beta-testing',
        'location':shard_info_tr1c1.get('location'),
        'partition':shard_info_tr1c1.get('partition')
        },
        {
        'action':'search',
        'query_key':'beta-testing',
        'location':shard_info_tr4mc.get('location'),
        'partition':shard_info_tr4mc.get('partition')
        },
        {
        'action':'prefix_show',
        'query_key':'allo',
        'location':shard_info_tr1c2.get('location'),
        'partition':shard_info_tr1c2.get('partition')
        },
        {
        'action':'prefix_show',
        'query_key':'allo',
        'location':shard_info_tr2c2.get('location'),
        'partition':shard_info_tr2c2.get('partition')
        }
    ]


def create_trie_nodes():
    global tr1c1,tr1c2,tr1mc,tr2c1,tr2c2,tr3c1,tr3c2,tr4c1,tr4mc
    tr1c1 = TrieNode(shard_info = shard_info_tr1c1)
    tr1c2 = TrieNode(shard_info = shard_info_tr1c2)
    tr1mc = TrieNode(shard_info = shard_info_tr1mc)
    tr2c1 = TrieNode(shard_info = shard_info_tr2c1)
    tr2c2 = TrieNode(shard_info = shard_info_tr2c2)
    tr3c1 = TrieNode(shard_info = shard_info_tr3c1)
    tr3c2 = TrieNode(shard_info = shard_info_tr3c2)
    tr4c1 = TrieNode(shard_info = shard_info_tr4c1)
    tr4mc = TrieNode(shard_info = shard_info_tr4mc)

def get_trie_mapper_for_shard_classifier():
    global tr1c1,tr1c2,tr1mc,tr2c1,tr2c2,tr3c1,tr3c2,tr4c1,tr4mc
    trie_mapper = defaultdict(None)
    trie_mapper['r1c1'] = tr1c1
    trie_mapper['r1c2'] = tr1c2
    trie_mapper['r1mc'] = tr1mc
    trie_mapper['r2c1'] = tr2c1
    trie_mapper['r2c2'] = tr2c2
    trie_mapper['r3c1'] = tr3c1
    trie_mapper['r3c2'] = tr3c2
    trie_mapper['r4c1'] = tr4c1
    trie_mapper['r4mc'] = tr4mc
    return trie_mapper
