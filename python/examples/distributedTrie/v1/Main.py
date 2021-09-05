# author : Amit Singh Sansoya [@amit3200]

    
from ShardClassifier import ShardClassifier
from QueryAPI import QueryAPI
import Helpers as hlp

"""
This is the main program where the distributed trie starts.
How the things work. What are the assumptions?.
So we aim to build the trie which is distributed. Now the distribution can be done on the basis of multiple things.
For the ease of things we willl keep it simple and will distribute the trie as per the region. So this means every
region will have different trie node. The data between them are mutually exclusive to each other.
"""
# allowed_actions = ['search','show','insert','prefix_show']

def main():
    # server side work [as not running on server as of now ;)]
    hlp.create_trie_nodes()
    trie_mapper = hlp.get_trie_mapper_for_shard_classifier()
    sc = ShardClassifier(trie_mapper)

    # insert operations
    for insert_request in hlp.trie_dictionary:
        request = {
        'action':'insert',
        'query_key':insert_request[0],
        'location':insert_request[1].get('location'),
        'partition':insert_request[1].get('partition')}
        qAPI = QueryAPI(request,sc)
        del qAPI
    

    # other operations
    for request in hlp.show_requests:
        qAPI = QueryAPI(request,sc)
        del qAPI

main()