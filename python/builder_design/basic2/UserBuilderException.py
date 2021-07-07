"""
Custom Exception Class. Nothing much here.
"""
class UserBuilderException(Exception):

    def __init__(self,*args):
        if args:
            msg = ""
            for exception_logs in args:
                msg += exception_logs + "\n"
            self.message = msg
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "UserBuilderException : {message}".format(message = self.message)
        else:
            return "UserBuilderException : Unknow Exception Occured."
