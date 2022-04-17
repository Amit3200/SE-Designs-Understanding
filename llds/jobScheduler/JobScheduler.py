import os
import heapq
from Task import Task
from Job import Job
from multiprocessing import Process

class JobScheduler:
    jobs :heapq = []
    job_tracker = {}
    def add(self, job: Job):
        if job not in self.job_tracker:
            print(self.jobs)
            heapq.heappush(self.jobs,job)
            self.job_tracker[job] = 1
    
    def remove(self, job: Job):
        if job in self.job_tracker:
            jobs = list(self.jobs)
            x = jobs.index(job)
            del jobs[x]
            del self.job_tracker[self.jobs]
            self.jobs = heapq.heapify(jobs)
    






def executeFromQueue(js,start,ps):
    print("Executing")
    if js.jobs != [] and start%js.jobs[0].schedule_time == 0:
        print("Running process {p} and parent is {ps}".format(p = os.getpid(), ps = ps))
        job = heapq.heappop(js.jobs)
        job.run()
        heapq.heappush(js.jobs,job)
    else:
        print("Waiting")