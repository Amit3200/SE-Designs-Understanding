import time
from datetime import datetime
from otp_generator import OtpAlgorithm, clean_skey

class User:
    def __init__(self, username, email, password, service):
        self.username = username
        self.email    = email
        self.password = password
        self.otp      = None
        self.service  = service
        self.valid    = False
        self.secret_k = "algoTestingDummy"
    
    def get_otp_instance(self):
        otp = OtpAlgorithm(clean_skey(self.secret_k))
        return otp
        
    def request_otp(self):
        otp = self.get_otp_instance()
        token = otp.generate_otp()
        if type(token) != "" and len(token) == 6:
            self.otp = token
            self.valid = True
            del otp
        return token

    def verify_otp(self):
        otp = self.get_otp_instance()
        if otp.verify_otp(self.otp):
            return True
        else: 
            self.valid = False
            del otp
            return False

    def access_function(self, idx = -1):
        if self.verify_otp():
            print("[Application Log tc {idx}] {dt} : Access Granted {obj} : {service}".format(dt = str(datetime.now()), obj = self, service = self.service, idx = idx))
        else:
            print("[Application Log tc {idx}] {dt} : Access Denied  {obj} : {service}".format(dt = str(datetime.now()), obj = self, service = self.service, idx = idx))


class UserHelperLayer:
    def __init__(self):
        pass 


    def main(self):
        idx = 1
        p1,p2 = False, False
        user1, user2 = None, None
        while idx <= 35:
            if not p1:
                user1 = User("takumiFujiwara","takumiFujiwara@initiald.com","password","drifting")
                p1 = True 
                print("[Application Log]",user1.username,"has generated",user1.request_otp())
            user1.access_function(idx)
            idx += 1
            if not p2:
                user2 = User("kurt","kurtweller@blindspot.com","password","detective")
                p2 = True 
                print("[Application Log]",user2.username,"has generated",user2.request_otp())
            user2.access_function(idx)
            time.sleep(1)


uhsl = UserHelperLayer()

uhsl.main()