# author : Amit Singh Sansoya [@amit3200]
from typing import DefaultDict
from logger import Logger
import heapq
from collections import defaultdict
from ProcessNode import ProcessNodeBuilder

    


class MyLogger(Logger):
    def __init__(self):
        self.queue = []
        self.process_mapper = defaultdict(ProcessNodeBuilder)

    def warn_message(self, status, process_id, ts):
        if status == "kill":
            return '[ Warn ] :      {p_id} which is unknown pid, was attempted to be killed at {en_ts}.'.format(p_id = process_id, en_ts = ts)
        if status == "running":
            return '[ Warn ] :      {p_id} which is already running, was tried to be start again at {st_ts}'.format(p_id = process_id, st_ts = ts)

    def logger_message(self,node):
        return '[ Logger ] :    {p_id} started at {st_ts} and ended at {en_ts}'.format(p_id = node.get_process_id(), st_ts = node.get_start_time(), en_ts = node.get_end_time())

    def start(self, process_id, start_time, end_time = None, info = None, mode = None):
        node = ProcessNodeBuilder(process_id = process_id, start_time = start_time).build()
        if process_id not in self.process_mapper:
            self.process_mapper[process_id] = node
        else:
            print(self.warn_message(status = "running", process_id = process_id, ts = start_time))

    def finish(self, process_id, end_time):
        if process_id in self.process_mapper:
            updated_node = self.process_mapper.get(process_id).end_time(end_time).build()
            heapq.heappush(self.queue,updated_node)
            del self.process_mapper[process_id]
        else:
            print(self.warn_message(status = "kill", process_id = process_id, ts = end_time))


    
    def log(self):
        tmp = self.queue[:]
        while len(tmp) > 0:
            ele = heapq.heappop(tmp)
            # print("="*50)
            print(self.logger_message(ele))
            # print(ele)
            # print("="*50)

