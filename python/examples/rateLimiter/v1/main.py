# author : Amit Singh Sansoya [@amit3200]
# lets create a scenario
# rate limiter was supposed to handle 5 requests per user in min
"""
Rate limiter limits an api from being used with in a time span. Like a certain api might have access for a user to use only 5 reqeusts in a minute.
If more then 5 requests are made in minute others should be invalidated.

This uses the sliding window logic.
Pros
-> Handles the boundary conditions.
-> Better then other approaches.

Cons
-> Memory used here is more as all the timestamps of those windows are being maintained.

Consider 3 requests allowed in a minute and we get every second one requests
-> ts = 1 -> rq = 1 [allowed]
-> ts = 2 -> rq = 2 [allowed]
-> ts = 3 -> rq = 3 [allowed]
-> ts = 4 -> rq = 4 [not allowed] [3 requests in 60 sec]
.....................................................................................
-> ts = 60 -> rq = 60 [not allowed]
-> ts = 61 -> rq = 61 [allowed] [rq 1 expires and we had 1 capacity left so allowed]
-> ts = 62 -> no request        [rq 2 and rq 3 expired]
-> ts = 63 -> rq = 62 [allowed] [we had 2 capacity left]
-> ts = 64 -> rq = 63 [allowed] [we had 1 capacity left]
-> ts = 65 -> rq = 64 [not allowed] [3 requests in 1 min consumed]
.....................................................................................
"""

"""
Main.py -> Scenario Creator - The way api's are called.
User.py -> Holds only user creation and service asker. Means a function by which user object can ask for the service. So User has access to Service Provider class [Singleton has reponsibility to return service]
Service.py -> Creates the Service and Necessary functions for the service provider. Before returning the token this has access to RateLimiterDs Object. And hence it runs the validation before the actual api call.
rateLimiterDs.py -> Actual Rate Limiter logic.

This is main program where u can simulate how the requests should be made. How the pattern of requests should look like.
Create user and request processor object and pass it to the get service access function.
lastly dumping some logs

Customize the request calling pattern and use the logs to plot the metric to see how it works.
"""
from user import User
import random, time
import json



archer = User(name = "Archer")
time.sleep(random.randint(1,2))
gilgamesh = User(name = "Gilgamesh")
time.sleep(random.randint(1,2))
fujiwara = User(name = "Fujiwara")
def write(name,obj):
    with open("E://"+name+".json","w+") as fd:
        fd.write(json.dumps(obj.window))

def scenario1():
    for i in range(30):
        if i%2 == 0:
            for j in range(3):
                archer.get_service_access()
                time.sleep(random.uniform(0.01,1))
        elif i%3 == 0:
            for j in range(3):
                archer.get_service_access()
                time.sleep(random.uniform(1.5,2.5))
        elif i%5 == 0:
            for j in range(3):
                archer.get_service_access()
                time.sleep(random.uniform(0.01,5))
    
    write("archer3",archer)



def scenario2():
    idx = 0
    for i in range(1500):
        factor = random.randrange(1,10)
        time.sleep(random.uniform(0.00001,0.0000009))
        archer.get_service_access()
        time.sleep(random.uniform(0.00001,0.0000009))
        gilgamesh.get_service_access()
        time.sleep(random.uniform(0.00001,0.0000009))
        fujiwara.get_service_access()
        time.sleep(random.uniform(0.00001,0.0000009))
        if (idx >= (100*factor) and idx<= (200 *factor)):
            w = random.randint(1,120)
            time.sleep(w)
            idx += w
        idx += 1
        



    # write("archer2",archer)
    # write("gilgamesh2",gilgamesh)
    # write("fujiwara2",fujiwara)


scenario1()