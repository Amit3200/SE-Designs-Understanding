from message_producer import MessageProducer
from werkzeug.utils import secure_filename
from threading import Thread
import time
import os

ALLOWED_EXTENSION   =  {'txt','png','jpg','json'} 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSION


def handle_file_upload(data, user_data, app):
    if 'file' not in data:
        print('No File Part')
        return """INVALID"""
    file = data['file']
    if file.filename == '':
        print('No selected file')
        return """INVALID"""
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        thread1 = Thread(target = file.save,args = (upload_file_path,))
        thread2 = Thread(target = handle_user_data,args = (user_data, upload_file_path))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        return """SUCCESS"""
    return """INVALID"""
    

def handle_user_data(user_data, upload_file_path = None):
    params      = user_data
    print(params)
    print("working")
    if params == None:
        params = dict({})
    username    = params.get('username',None)
    department  = params.get('department',None)
    message     = params.get('message',None)
    ts          = time.time()*1000.0
    upload_path = upload_file_path
    content = {
        'username':username,
        'department':department,
        'message':message,
        'creation_time':ts,
        'upload_path':upload_path
    }
    broker = MessageProducer()
    broker.send(content = content)
    


def process_request(data, user_data, app):
    response = handle_file_upload(data, user_data, app)
    return response