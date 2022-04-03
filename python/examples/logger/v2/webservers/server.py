from flask import Flask, request, render_template, redirect
from flask_sock import Sock
import pathlib
import os

log_directory = pathlib.Path().absolute()
app = Flask(__name__)
sock = Sock(app)
@app.route("/")
def index():
    return "Hello World!"

# last 5 lines of files
@app.route("/files/<filename>")
def show_file(filename):
    data = None
    current_log_file = str(log_directory)+'\\'+filename
    with open(current_log_file,"r") as fd:
        data = fd.readlines()
    tail = "\n".join(data[-5:])
    return render_template("main.html",tail = tail)

@app.route("/receive")
def receive_ack():
    print("ack recevied")
    return "cool"

@app.route("/rec_data",methods = ["POST"])
def rec_data():
    if request.method == "POST":
        print(request.form)
    return "Done"

@app.route("/logs/<filename>")
def show_logs(filename):
    data = None
    current_log_file = str(log_directory)+'\\'+filename
    with open(current_log_file,"r") as fd:
        data = fd.readlines()
    tail = "\n".join(data[-20:])
    return render_template("logUpdater.html",tail = tail)


def log_file_update(content):
    current_log_file = str(log_directory)+'\\'+"log.txt"
    with open(current_log_file,"a+") as fd:
        fd.writelines(content)
    return True


def reload_content(filename):
    data = None
    current_log_file = str(log_directory)+'\\'+filename
    with open(current_log_file,"r") as fd:
        data = fd.readlines()
    tail = "\n".join(data[-5:])
    return tail

@sock.route("/echo")
def echo(sock):
    while True:
        data = sock.receive()
        # log_file_update(data)
        print("here",data)
        sock.send(data)



if __name__== '__main__':
    app.run(debug = True)

