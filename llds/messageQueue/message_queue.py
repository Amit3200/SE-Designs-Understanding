from collections import deque, defaultdict
from datetime import datetime, timedelta
import queue
import time
import json

QUEUE_MESSAGE_LIMIT = 50

class Message:
    message         : dict
    message_id      : int
    creation_time   : datetime

    def __init__(self, message:dict):
        self.message_id     = int(time.time())
        self.creation_time  = datetime.now()
        if type(message) == dict:
            self.message = message
        else:
            raise Exception("Message is not in JSON Format.")

    def get_content(self):
        return self.message    

    def get_message(self):
        return self.__repr__()

    def __repr__(self):
        return """
            message_id      : {message_id},
            creation_time   : {creation_time},
            message         : {content},
        """.format(message_id = self.message_id, creation_time = self.creation_time, content = json.dumps(self.message, indent = 4))
        


class Queue:
    #[[1, (m1,m2)] ]
    queue_id: int
    queue   : list[Message]

    def __init__(self, qid):
        self.queue_id = qid
        self.queue = list()
    
    def add_message(self, message: Message):
        if len(self.queue) + 1 <= QUEUE_MESSAGE_LIMIT:
            self.queue.append(message)
        
    def consume_message(self) -> dict:
        if len(self.queue) > 0:
            msg = self.queue.pop(0)
            return msg.get_content()
        return dict({})

    def __repr__(self):
        val_msg     = "\nQueue {qid}".format(qid = self.queue_id)
        content = []
        for val in self.queue:
            content.append(val.get_message())
        msgs = json.dumps({'contents' : content}, indent = 4)
        val_msg += "\n"+msgs
        return val_msg

class QueueManager:
    queueM      : int
    queueName   : str
    queueManager : defaultdict(list[Queue])

    def __init__(self, queueM : int, queueName : str):
        self.queueM = queueM
        self.queueName = queueName
        self.queueManager = defaultdict(list[Queue])

    def add_queue(self, queue_id:int):
        if queue_id not in self.queueManager:
            self.queueManager[queue_id] = Queue(queue_id)
        else:
            raise Exception("Queue with given id already exists.")
    
    def remove_queue(self, queue_id:int):
        if queue_id in self.queueManager:
           del self.queueManager[queue_id]

    def get_queue(self, queue_id: int) -> Queue:
        if queue_id in self.queueManager:
            return self.queueManager[queue_id]
        else:
            raise Exception("Queue with given id doesn't exists.")
    
    def get_all_queue(self) -> list[Queue]:
        return list(self.queueManager.values())
    
    def __repr__(self):
        val_msg = "queueM id : {qmid}\nqueueName : {qName}".format(qmid = self.queueM, qName = self.queueName)
        val = self.queueManager.__repr__()
        return val_msg + "\n" + val


class Publisher:
    orgs : list[QueueManager]

    def __init__(self):
        self.orgs = []

    
    def add_queue_manager(self, queueManager: QueueManager):
        self.orgs.append(queueManager)

    def publish_to_all(self, queueManager: QueueManager, message: Message):
        for queueM in self.orgs:
            if queueM == queueManager:
                queue = queueM.get_all_queue()
                for q in queue:
                    q.add_message(message)
    
    def publish_to_specific(self, queueManager: QueueManager, queue_id : int , message : Message):
        for queueM in self.orgs:
            if queueM == queueManager:
                queue = queueM.get_queue(queue_id)
                queue.add_message(message)
    
    def show_queue(self, queueManager: QueueManager, queue_id: int):
        for queueM in self.orgs:
            if queueM == queueManager:
                print(queueM.get_queue(queue_id)) 

    def show_all_queue(self, queueManager: QueueManager):
        for queueM in self.orgs:
            if queueM == queueManager:
                print(queueM.get_all_queue()) 

        
    
    def __repr__(self):
        val_msg = "Publisher"
        val = ""
        for org in self.orgs:
            val += org.__repr__()
        return val_msg + "\n" + val

# class Subscriber:
class Subscriber:
    subsrciber_id   : int 
    queueManager    : QueueManager
    queue_mapper    : dict[(int,Queue)]


    def __init__(self, sub_id: int, queueM : QueueManager):
        self.subsrciber_id  = sub_id
        self.queueManager   = queueM
        self.queue_mapper   = defaultdict(Queue)
    
    def add_queue_to_consume(self, qid : int):
        queue = self.queueManager.get_queue(qid)
        self.queue_mapper[qid] = queue
    
    def consume(self):
        # while True:
            if len(self.queue_mapper.keys()) > 0:
                for queue in self.queue_mapper.values():
                    if len(queue.queue) > 0:
                        print(" = = " * 50)
                        print("RECEIVED CONTENT")
                        print(queue.consume_message())
                        print("CONSUMED")
                        print(" = = " * 50)
            else:
                raise Exception("Empty Query Mapper")
    
    def detach_queue(self,qid):
        if qid in self.queue_mapper:
            print("Subscriber {sid} has lost access to queue id {qid}".format(sid = self.subsrciber_id, qid = qid))
            del self.queue_mapper[qid]
    
    def __repr__(self):
        val = "Subscriber : {sid}".format(sid = self.subsrciber_id)+"\n"+self.queueManager.__repr__()
        return val



    



pub = Publisher()
qm1 = QueueManager(1, "archer")
qm2 = QueueManager(2, "kai")
pub.add_queue_manager(qm1)
pub.add_queue_manager(qm2)

qm1.add_queue(1)
qm1.add_queue(2)
qm1.add_queue(3)

qm2.add_queue(1)

m1 = Message({'name':'a1','content':'m1'})
m2 = Message({'name':'a1','content':'m2'})
m3 = Message({'name':'a2','content':'m3'})
m4 = Message({'name':'a2','content':'m4'})
m5 = Message({'name':'a3','content':'m5'})

pub.publish_to_all(qm1, m1)
# pub.show_all_queue(qm2)
# print("\n")
print(pub)

pub.publish_to_specific(qm1, 1, m2)
pub.publish_to_specific(qm2, 1, m3)
print(pub)
pub.publish_to_specific(qm2, 1, m3)
# pub.publish_to_specific(qm1, 4, m2)
print(pub)