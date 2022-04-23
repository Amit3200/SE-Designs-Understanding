from types  import FunctionType
class Task:
    task_id : int
    task_name : str
    task_info : str 
    func : FunctionType 

    def __init__(self, task_id, task_name, func, task_info = None):
        self.task_id = task_id
        self.task_info = task_name
        self.func = func
        self.task_name = task_info

    def work(self, params = None):
        print("Executing task : {task_name}".format(task_name = self.task_name))
        self.func(params)