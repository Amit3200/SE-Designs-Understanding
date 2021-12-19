# SE-Designs-Understanding
#### ```maintained by [amit3200](https://github.com/Amit3200)```
Contains various design strategies with the implementation of them on a small level with an example. This repo helps us to understand how and why one should implement various designs while creating applications.

## Projects
 #### *[urlShortner](https://github.com/Amit3200/SE-Designs-Understanding/tree/master/python/examples/urlShortner/v1)
 #### *[rateLimiter](https://github.com/Amit3200/SE-Designs-Understanding/tree/master/python/examples/rateLimiter/v1)
 #### *[logger](https://github.com/Amit3200/SE-Designs-Understanding/tree/master/python/examples/logger/v1)
 #### *[case_study](https://github.com/Amit3200/SE-Designs-Understanding/tree/master/python/examples/case_study/study1)
 #### *[distributedTrie](https://github.com/Amit3200/SE-Designs-Understanding/tree/master/python/examples/distributedTrie/v1)


# urlShortner
 * Mimics the case of an url shortner. Uses 2 queues where the shortened url are generated and kept as some request comes it is consumed and is allocated  to the allocated queue which says that shortened url is used.

# rateLimiter
 * This allows to rate limit a particular api request.

# logger
 * Logger is used to log the application uses the sequencing accordingly. Uses heap to map the requests.

# case_study
 * rabbit_mq application upload asynchronously and notify user about upload using rabbit mq

# Distributed Trie v1 (Shard by Region)
 * This was just a try and mimic program for the simulation in run time memory.
 * How the things work. What are the assumptions?
 * So we aim to build the trie which is distributed. Now the distribution can be done on the basis of multiple things.For the ease of things we willl keep it simple and will distribute the trie as per the region. So this means every region will have different trie node. The data between them are mutually exclusive to each other.
 * Code for `Distributed Trie v1` at [Link to Distributed Trie v1](https://github.com/Amit3200/SE-Designs-Understanding/blob/master/python/examples/distributedTrie/v1/distributedTrieV1.png)
 * Refer to diagram below
![Alt text](python/examples/distributedTrie/v1/distributedTrieV1.png?raw=true "Distributed Trie v1")


> Feel free to reach me out and give suggestions on the same.


Connect at [`amit3200`](https://github.com/Amit3200)
