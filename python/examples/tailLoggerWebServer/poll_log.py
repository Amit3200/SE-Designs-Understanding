# Redundant not required.
import os, requests
log_file_path = "c:/Users/tusha/Desktop/tailFbrowserStack/logs/log.txt"
last_modified_time = os.path.getmtime(log_file_path)
while True:
    if last_modified_time < os.path.getmtime(log_file_path):
        requests.get('http://127.0.0.1:5000/')
        last_modified_time = os.path.getmtime(log_file_path)

