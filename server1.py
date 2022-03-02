# amit3200 [Amit Singh Sasnsoya]
from flask import Flask, render_template
from flask_socketio import SocketIO
from dataclasses import dataclass
from datetime import datetime
import os


app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')

log_file_path = "c:/Users/tusha/Desktop/tailFbrowserStack/logs/log.txt"
last_modified_time = os.path.getmtime(log_file_path)

client_holders = dict()
thread = None


class Reader:
    __instance = None
    file_end   = 0
    @staticmethod
    def getInstance():
        if Reader.__instance == None:
            Reader()
        return Reader.__instance

    def __init__(self):
        if Reader.__instance != None:
            raise Exception("Singleton Class : Attempted Multiple Instance Creation")
        else:
            Reader.__instance = self

    # needs optimization    
    def initial_read_file(self):
        data = None
        with open(log_file_path,"r") as fd:
            data = fd.readlines()
        self.file_end = len(data)
        response = data[-10:]
        return "\n".join(response[-10:])

    def read_delta(self):
        data = None
        with open(log_file_path,"r") as fd:
            data = fd.readlines()
        response = data[self.file_end:]
        self.file_end += len(response)
        return "\n".join(response)

read = Reader()

@dataclass
class Client:
    id : int 
    meta_msg : str
    creation_time : datetime


def background_thread():
    global last_modified_time
    while True:
        if last_modified_time != os.path.getmtime(log_file_path):
            print("There was a update")
            last_modified_time = os.path.getmtime(log_file_path)
            logs = read.read_delta()
            socketio.emit('update_logs',{'logs':logs},broadcast = True)


@app.route("/")
def index():
    return render_template("display.html")


@socketio.on('initial')
def client_onboard(data):
    global thread
    logs = read.initial_read_file()
    cobj = Client(data['socket_id'],"connected",datetime.now())
    client_holders[data['socket_id']] = cobj
    socketio.emit('push_logs',{'logs':logs},broadcast = True)
    if thread is None:
        print("Thread Created")
        thread = socketio.start_background_task(target = background_thread)

# @socketio.on('update')
# @app.route('/update')
# def delta_onboard():
#     global thread
#     if thread is None:
#         thread = socketio.start_background_task(background_thread)

@socketio.on('destroy')
def destroy_client(data):
    if "socket_id" in data.keys():
        sid = data['socket_id']
        if sid in client_holders:
            del client_holders[sid]
            print("Deleted")
        else:
            print("Doesn't Exists")
        
if __name__ == '__main__':
    socketio.run(app, debug = True)