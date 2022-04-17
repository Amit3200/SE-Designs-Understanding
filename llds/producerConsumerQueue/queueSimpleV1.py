import os
import time
import random
from multiprocessing import Process, Queue, Lock

def producer(queue, lock, names):
    with lock:
        print("Starting producer => {}".format(os.getpid()))
    
    for name in names:
        time.sleep(random.randint(0,10))
        print("{} put {}".format(os.getpid(),name))
        queue.put(name)
    
    with lock:
        print("Producer {} exiting.".format(os.getpid()))

def consumer(queue,lock):
    with lock:
        print("Starting consumer => {}".format(os.getpid()))
    
    while True:
        time.sleep(random.randint(0,10))
        name = queue.get()
        with lock:
            print("{} got {}".format(os.getpid(),name))

if __name__ == '__main__':
    names = [['Master Shake', 'Meatwad', 'Frylock', 'Carl'],
                ['Early', 'Rusty', 'Sheriff', 'Granny', 'Lil'],
                ['Rick', 'Morty', 'Jerry', 'Summer', 'Beth']]

    queue = Queue()
    lock = Lock()
    producers = []
    consumers = []

    for n in names:
        producers.append(Process(target=producer,args=(queue,lock,n)))

    for i in range(len(names) * 2):
        p = Process(target = consumer, args = (queue, lock))
        p.daemon = True
        consumers.append(p)

    for p in producers:
        p.start()

    for c in consumers:
        c.start()

    for p in producers:
        p.join()
