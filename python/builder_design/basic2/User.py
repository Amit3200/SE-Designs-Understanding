# author : amit3200 [Amit Singh Sansoya]
"""
User : Creates User Object. Only Getters. No Setters.
"""
class User:
    __first_name:str = None 
    __last_name:str = None 
    __age:str = None 
    __phone:str = None 
    __address:str = None

    def __init__(self,builder):
        self.__first_name = builder.b_first_name
        self.__last_name = builder.b_last_name
        self.__age = builder.b_age
        self.__phone = builder.b_phone 
        self.__address = builder.b_address
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age
    
    def get_phone(self):
        return self.__phone
    
    def get_address(self):
        return self.__address
    
    def __str__(self):
        msg = """
        Name    :{first_name} {last_name},
        Age     :{age},
        Phone   :{phone},
        Address :{address}""".format(
            first_name = self.get_first_name(),
            last_name = self.get_last_name(),
            age = self.get_age(),
            phone = self.get_phone(),
            address = self.get_address()
        )
        return msg

    

