# author : Amit Singh Sansoya [@amit3200]
# this is just a test class refer to the pyotp library on git for proprer backend.
import os
import json 
import hmac 
import time
import base64
import hashlib
import unicodedata
from datetime import datetime


class OtpAlgorithm:
    def __init__(self, secret):
        self.secret     = secret
        self.interval   = 30
        self.digit      = 6 
        self.hash_algo  = hashlib.sha1

    def throw_exception(self,msg):
        print("[Error Message] {} : {}"%str(datetime.now())%msg)

    def check_and_validate(self, key):
        if key == None:
            self.throw_exception("Secret Key Invalid. Can't Generate Otp")
    
    @staticmethod
    def int_to_bytestring(i, padding = 8):
        result = bytearray()
        while i != 0:
            result.append(i & 0xFF)
            i >>= 8
        return bytes(bytearray(reversed(result)).rjust(padding, b'\0'))


    def get_otp(self,secret_key, interval):
        key         = base64.b32decode(secret_key.upper(), casefold = True)
        hasher      = hmac.new(key, self.int_to_bytestring(interval), self.hash_algo)
        hmac_hash   = bytearray(hasher.digest())
        offset      = hmac_hash[-1] & 0xf
        code        = ((hmac_hash[offset] & 0x7f) << 24 |   (hmac_hash[offset + 1] & 0xff) << 16 |  (hmac_hash[offset + 2] & 0xff) << 8 |   (hmac_hash[offset + 3] & 0xff))
        str_code = str(code % 10 ** self.digit)
        while len(str_code) < self.digit:
            str_code = '0' + str_code
        return str_code
    
    
    def get_totp_token(self, offset = 0):
        interval = int((time.time()+offset)/self.interval)
        return self.get_otp(self.secret, interval)
        
    
    def generate_otp(self):
        return self.get_totp_token()


    def verify_otp(self, otp, attemps = None):
        notp    = self.generate_otp()
        # print(otp,notp)
        s1      = unicodedata.normalize('NFKC', otp)
        s2      = unicodedata.normalize('NFKC', notp)
        # print(s1,s2)
        return hmac.compare_digest(s1.encode("utf-8"), s2.encode("utf-8"))


    # def test(self):
    #     idx = 0
    #     code = self.generate_otp()
    #     print("code : ", code)
    #     while idx < 40:
    #         code1 = self.generate_otp()
    #         print("code1 : ", code1)
    #         s1 = unicodedata.normalize('NFKC', code)
    #         s2 = unicodedata.normalize('NFKC', code1)
    #         print("Test {tc}: ".format(tc = idx+1),s1,s2,hmac.compare_digest(s1.encode("utf-8"), s2.encode("utf-8")))
    #         time.sleep(1)
    #         idx += 1

def clean_skey(secret_key):
    missing_padding = len(secret_key) % 8
    if missing_padding != 0:
        secret_key += '=' * (8 - missing_padding)
    return secret_key

# ss = clean_skey("scsdfcsdfsrewdxxdasd")
# obj = OtpAlgorithm(ss)
# # obj.main()
# obj.test()

    