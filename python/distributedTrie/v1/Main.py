# author : Amit Singh Sansoya [@amit3200]

    
from ShardClassifier import ShardClassifier
from QueryAPI import QueryAPI
import Helpers as hlp


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