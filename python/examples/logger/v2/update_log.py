import requests
log_file_path = "c:/Users/tusha/Desktop/tailFbrowserStack/logs/log.txt"
while True:
    line = '\n'+str(input("Enter Line : "))    
    with open(log_file_path,"a+") as fd:
        fd.writelines(line)
    res = requests.get("http://127.0.0.1:5000/update")
    print(res.text)
    print(res)
    