class ProcessNode:
    def __init__(self, builder):
        self.p_process_id = builder.p_process_id
        self.p_start_time = builder.p_start_time
        self.p_end_time = builder.p_end_time
        self.p_info = builder.p_info
        self.p_mode = builder.p_mode
    
    def __lt__(self, nxt):
        return self.p_process_id < nxt.p_process_id

    def get_process_id(self):
        return self.p_process_id

    def get_start_time(self):
        return self.p_start_time
    
    def get_end_time(self):
        return self.p_end_time
    
    def get_info(self):
        return self.p_info
    
    def get_mode(self):
        return self.p_mode

    def end_time(self,end_time):
        self.p_end_time = end_time
        return self

    def info(self,info):
        self.p_info = info
        return self
    
    def mode(self,mode):
        self.p_mode = mode
        return self

    def build(self):
        Node = ProcessNode(self)
        return Node
    
    def __str__(self):
        msg = """process_id : {process_id},
                 start_time : {start_time},
                 end_time   : {end_time},
                 info       : {info},
                 mode       : {mode}""".format(
                     process_id = self.get_process_id(),
                     start_time = self.get_start_time(),
                     end_time = self.get_end_time(),
                     info = self.get_info(),
                     mode = self.get_mode()
                 )
        return msg



class ProcessNodeBuilder:
    def __init__(self, process_id, start_time, end_time = None, info = None, mode = None):
        self.p_process_id = process_id
        self.p_start_time = start_time
        self.p_end_time = end_time
        self.p_info = info
        self.p_mode = mode

    def end_time(self,end_time):
        self.p_end_time = end_time
        return self

    def info(self,info):
        self.p_info = info
        return self
    
    def mode(self,mode):
        self.p_mode = mode
        return self

    def build(self):
        Node = ProcessNode(self)
        return Node