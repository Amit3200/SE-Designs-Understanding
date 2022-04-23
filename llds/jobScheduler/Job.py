from datetime import datetime
from Task import Task
from typing import List
class Job:
    user_id : int
    job_id : int
    job_name : str
    tasks : List[Task]
    schedule_time : int

    def __init__(self, user_id, job_id, job_name, tasks, schedule_time):
        self.user_id = user_id
        self.job_id = job_id
        self.job_name = job_name
        self.tasks = tasks
        self.schedule_time = schedule_time

    def run(self):
        print("Starting Job : {jname}".format(jname = self.job_name))
        for task in self.tasks:
            task.work()
        print("===================================================================")

    def __lt__(self, other):
        return self.schedule_time < other.schedule_time
    
    def __repr__(self):
        return """job_id:{job_id},job_name:{job_name},schedule_time:{stime}""".format(job_id = self.job_id, job_name = self.job_name, stime = self.schedule_time)