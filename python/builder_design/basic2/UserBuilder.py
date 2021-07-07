# author : amit3200 [Amit Singh Sansoya]
"""
UserBuilder : As one can see this does the actual work of creating the object with the minimum support possible.
              Giving the options to expand the details of the attributes of the object by providing a layer of methods.
              Validates Object against the check to ensure that Object is valid.
"""

from User import User
from UserBuilderException import UserBuilderException

class UserBuilder:
    b_first_name:str = None 
    b_last_name:str = None 
    b_age:str = None 
    b_phone:str = None 
    b_address:str = None

    def __init__(self,first_name,last_name):
        self.b_first_name = first_name
        self.b_last_name = last_name
    
    def age(self,age):
        self.b_age = age
        return self 
    
    def phone(self,phone):
        self.b_phone = phone
        return self 
    
    def address(self,address):
        self.b_address = address
        return self
    
    def validate_user_object(self,user):
        if user.get_first_name() == None and user.get_last_name() == None:
            raise UserBuilderException("First_Name and Last_Name not initialized. Violates User Object Build.")
        if user.get_phone() == None:
            raise UserBuilderException("Phone_Number not initialized. Violates User Object Build.")
    
    def build(self):
        user = User(self)
        self.validate_user_object(user)
        return user 
    
