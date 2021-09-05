# author : Amit Singh Sansoya [@amit3200]
# lets create a scenario
# rate limiter was supposed to handle 5 requests per user in min
from user import User
import random, time
from rateLimiterDs import RequestProcessor
import json

rq = RequestProcessor()
archer = User(name = "Archer")
time.sleep(random.randint(1,2))
gilgamesh = User(name = "Gilgamesh")
time.sleep(random.randint(1,2))
fujiwara = User(name = "Fujiwara")

idx = 0
for i in range(15000):
    factor = random.randrange(1,5)
    time.sleep(random.uniform(0.00001,0.0000009))
    archer.get_service_access(rq)
    time.sleep(random.uniform(0.00001,0.0000009))
    gilgamesh.get_service_access(rq)
    # print(json.dumps(rq.rlds,indent=4))
    time.sleep(random.uniform(0.00001,0.0000009))
    if (idx >= (200*factor) and idx<= (400 *factor)):
        w = random.randint(1,120)
        time.sleep(w)
        idx += w
    idx += 1
    

def write(name,obj):
    with open("E://"+name+".json","w+") as fd:
        fd.write(json.dumps(obj.window))

write("archer1",archer)
write("gilgamesh1",gilgamesh)
write("fujiwara1",fujiwara)


