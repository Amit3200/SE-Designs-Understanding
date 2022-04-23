
from multiprocessing import Process
from Task import Task
from Job import Job
from JobScheduler import JobScheduler, executeFromQueue
import os
def func1(args = None):
    print("This is func1. Working on stuff")

def func2(args = None):
    print("This is func2. Working on stuff")

def func3(args = None):
    print("This is func3. Working on stuff")

def func4(args = None):
    print("This is func4. Working on stuff")

task1 = Task(task_id=1,task_name="func1",func=func1,task_info="dummyfunc1")
task2 = Task(task_id=2,task_name="func2",func=func2,task_info="dummyfunc2")
task3 = Task(task_id=3,task_name="func3",func=func3,task_info="dummyfunc3")
task4 = Task(task_id=4,task_name="func4",func=func4,task_info="dummyfunc4")

job1 = Job(user_id=1,job_id=1,job_name="job_1",tasks=[task1,task4],schedule_time=2)
job2 = Job(user_id=2,job_id=2,job_name="job_2",tasks=[task2,task3,task4],schedule_time=3)
job3 = Job(user_id=1,job_id=3,job_name="job_3",tasks=[task2,task1,task3,task4],schedule_time=4)
js = JobScheduler()
js.add(job1)
js.add(job2)
js.add(job3)

if __name__ == '__main__':
    start = 1
    print(js.jobs)
    ps = os.getpid()
    print("parent os : {os}".format(os = ps))
    while start < 20:
        # print("Current Ts", start)
        p = Process(target = executeFromQueue,args=(js,start,os.getpid()))
        p.start()
        p.join()
        start += 1