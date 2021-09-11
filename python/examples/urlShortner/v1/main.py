# author : Amit Singh Sansoya [@amit3200]
import pdb
import random
from user import User
from utils import fakedb
from url_shortner import Shortner_Service, Generate_Service_Factory

"""
URL SHORTNER
------------

MAIN THING -> given a big url by the user generate a smaller string url.(<7 character assuming)
The short url should be able to redirect to main website.
The short url expires after certain time.
The system should be highly available and then the url should not be predictable.

Solution
--------
There are multiple ways to solve this u might have gone through it. But if not please go through because here
we will look into only one of the implementation which may not be correct. This is just to get an idea how things work.


Discussing few solutions
Approach 1.
    HLD 1.
        User ---> load balancer --> URL SHORTNER SERVICE (GET/POST) --> LOAD BALANCER -->   CACHE/DATABASE  
                                            ===                                                    |
                                            ===                                                    |
                                             |                                                     |
                                    URL SHORTNER GENERATOR  - - - - - - - - - - - - - - - - - - - -|    [check not exits]
        
        This LLD 1.
        -> The check that big url is  already shortened or not will always be there as same url should point to same shortened urls.
            URL SHORTNER GENERATOR
                -> Generates real time : as request comes
                -> use md5/base62 encodings : will require db check if short url exits or not either for url or for random number.
                Checking if short url exits or not can be eliminated in second approach refer below.

            
            As per this design as it looks the user requests the service decides if it is get or put. If we need to shorten the url it will go to the generator and then will update the db accordingly.
            Otherwise return from the cache/DB.
            Now it really depends how the shorten service is written. Here we are focusing on that it is a generator. It means we will generate the url and put it in db in real time.
            i>  If we use md5 we need to take first 7 characters and then take the first 7 characters and check if they are unique.
            ii> If we use someother encoding which generates string on the basis of random number. We will check if random number exists or not.


        -- IMPLEMENTING THIS ONE --
        Suggested LLD 2.
            URL SHORTNER GENERATOR --> URL KEY ASSIGNER.
                -> Will only do assigning on real time.
                -> the keys are already generated : hence look up requests on db are reducing.

            Hmm looks cool though there might be some issues but lets try to code as i said this is just to see how things work. 

Current Code Specs
Main.py -> replicate the situation of requests incoming.
User.py -> creates an user object immutable in nature. [not perfectly u know python limitations!]
Utils.py -> acts as an dummy database.
Url Shortner.py -> basically Service Provider the place where which algorithm will be used for encoding and the place where pre processing of all the shortenining url takes place. Contains the logic of assigning and fetching of urls.
shortner_algo.py -> Contains the main logic of generation or shortening i.e. base62 enconding.

        Queue 1 q1 -> Generated Store of all shuffled short urls = [s5,s1,s2,s6,s3,s9,.....]
        Queue 2 q2 -> Used urls = []
        Request r1 -> assign -> s5 
                                    -   q1 = [s1,s2,s6...]
                                    -   q2 = [s5]
        Request r2 -> assign -> s1
                                    -  q1 = [s2,s6,..]
                                    -  q2 = [s5,s1]
        Request r3 -> fetch -> s5      returns result
        
        timestamp expires s5 expires - q1 = [s1,s2,s6, ...,s5]
        Carry on

    Also in smaller range u might see a pattern in generation i.e because the value is shuffled across the squencetial list. To avoid this use larger list and then cap the capacity. edit in shortner_algo.py accordingly.
    Also the current expiration takes place when fetch is called. In real life an different service will keep on checking if the links are expiring.
    Also the links expire in 1 minute for observing purpose. U can change it in utils.py for more.
"""
def scenario1(URLSS:Shortner_Service):
    p1 = User("amit3200")
    p2 = User("archer1232")
    p3 = User("fujiwara3122")
    p4 = User("kirito2316")
    randomfactor = range(4,10)
    randlist =  [p1,p2,p3,p4]
    random.shuffle(randlist)
    big_url_tc = ['odWvqygfAXX9oOD', 'BiR4rpNYORo9HDa', 'vPobBStuyEkf0cX', '8HR8b0wNQosJvcM', '6wAHj2QAkOlgIDf', 'J45UoMEuSzOMajX', 'p8Ku5JtKoqPzhXo', 'pqLc2s7H6BtlrzI', '3k9mEFOn7eT3zjc', 'f4AUFuxz2AwMqyW', 'tuDLFvAvvqyeopt', 'MznEFNRepLlHZnA', 'lgCISSn8QwSr3U4', 'wgLyQUQ04A3uo0a', '96QqiJN60UctGk5', 'taiHZ0DBogzhtpj', '1hWCTLxP66TJRD3', 'p1W1gvFBRtRdqwv', 'C3rCnSIGicOfyIK', 'xpReoYNEVsCLtaa', 'qQ48ATadIwMX1Rv', 'lUuMzi9ks9xakjQ', 'vRSZVpbhaG89iLl', 'wNm2jHddLAxK5pL', 'usijyNOQbOZevrY', 'U0T2k1JDnfLEuXS', 'jXyCKSYKdYgXhoQ', 'yP8n6vTra26ZBNQ', 'lzbMtaCQacOtbQ0', 'E08LvZ6XBOYoO7P', '8U6mwZ6g4AHXoqh', 'hus0HJnLbLiMj1K', '6H77RLwOOGchQHc', 'S6Edgule9320Pdi', 'EQF8FZKtcdYyMHO', 'jAzRNkyv2hqvgNu', 'QasYQjEuzFLJiWE', 'kxI0sVmJfoMiwKP', 'qawdXj4OKbnGQpr', 'UTjHB28KEa3R0xu', 'vywIEL3VOLGqbL4', 'JuI7XqId72tqn5E', 'dyAx4OZBSQr2yC7', 'dbi6sVj1V8unXNn', 'FamYJdxb6OwuHQp', 'MmfWJgsWldveY6m', '038YqAaFG13nsiS', 'HVc0H6AAXn0rdMm', 'femrBBO8qvwr44A', 'cxq1EVZ0KrC5OHQ']
    short_url_tc = []
    visited = []
    for tc in range(10):
        if random.randint(1,10) in randomfactor:
            curr_url = random.choice(big_url_tc)
            if curr_url not in visited:
                user = random.choice(randlist)
                short_url = URLSS.assign(user, curr_url)
                short_url_tc.append(short_url)
                visited.append(curr_url)
        elif len(short_url_tc) > 0:
            curr_url = random.choice(short_url_tc)
            user = random.choice(randlist)
            URLSS.fetch(user, curr_url)

def scenario2(URLSS:Shortner_Service):
    p1 = User("amit3200")
    p2 = User("archer1232")
    p3 = User("fujiwara3122")
    p4 = User("kirito2316")
    userList =  [p1,p2,p3,p4]
    avail = {'cz9C8cKYj8gzhxD': 1, 'Qp3N2yHSHFmVoXD': 1, 'ORldWmF0uyCMGc8': 1, 'aeaZFP50a5QxYds': 1, 'HJQrWK1nNVLgcCE': 1, 'Z7fCnokgiRijLFo': 1, 'YAdEJrOjkwKf4w8': 1, 'nn9FE8Z9FfT9UvT': 1, '9xYcEZUSEWIJpOg': 1, '2f0pLZJfdzT5ZQ8': 1, '7s3frv3whCkrt8E': 1, 'DNJfbKfwbwatnRs': 1, '8uyZMZMG1VizCYO': 1, 'R8WyjZ1UQzWI3TT': 1, 'MlU3lh7gKeft6I3': 1, 'nLkJhoiRpa4lIMI': 1, 'UANCKUcbcoPbvKd': 1, '0wg2Q2DjYjnhz28': 1, 'mnoKw3ke9rdjCgP': 1, 'Empv7xhkU9DonRi': 1, '3WsWaqtDyhv6Ave': 1, 'AdRHP4N16Z8NoXZ': 1, 'bZgSRGxtEiHdZS5': 1, '6jAnGwGiNTnokJq': 1, '7O9keKiQLEQqtiy': 1, 'tNGF32gopuKBUkn': 1, 'aCI5ZjsbO6bOfkt': 1, 'WsUfm4gvRxjtbC3': 1, '8ov8eIMpW8NV6CV': 1, 'eu3WERwNIzul8DR': 1, 'YD2XFaPNw9vRwWU': 1, 'DWxFVOhEmlerO2P': 1, 'iQxDimU3w4Fabh2': 1, 'kU6f8IipfY05Xh7': 1, 'l5maXRUAFF3wRqN': 1, 'f56qO5mLdOxuSKi': 1, 'SKKbvIqflsWwwSQ': 1, 'h0NC5FX7cd0nQgS': 1, 'LjiDYkfG5wsOBPK': 1, 'UmtkMoN1fpR52JE': 1, 'ajPCbyLEFDXIowb': 1, '2ofcw47HELM6RGH': 1, 'BsmmLCpftmlHphp': 1, 'dwTMrqzY8Iu1PuF': 1, '96ISW5rxJOLB7Sr': 1, 'Hs5xmtoUnrktJDd': 1, 'pbhNZkkaSQRcctk': 1, 'nJFyk76QLiO9b64': 1, 'vohicVdN7oNldxg': 1, 'cMYqS3J3kzdFd0r': 1}
    tc = None
    while tc != 'q':
        tc = input()
        if tc == '1':
            if avail:
                big_url = random.choice(list(avail.keys()))
                avail.pop(big_url)
                user = random.choice(userList)
                short_url = URLSS.assign(user,big_url)
        elif tc == '2':
            short_url = input()
            user = random.choice(userList)
            URLSS.fetch(user, short_url)
        elif tc == '3':
            fakedb.show_db()
        elif tc == '4':
            URLSS.show_created_url()



            

            


def main():
    gsv1 = Generate_Service_Factory(algo_type = "baseX").get_service()
    URLSS = Shortner_Service(capacity = 50, service = gsv1)
    # scenario1(URLSS)
    scenario2(URLSS)
    # URLSS.show_created_url()
if __name__ == "__main__":
    main()