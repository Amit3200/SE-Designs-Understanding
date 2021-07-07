"""
Main.py - Calls Builder and we pass the necessary attributes required to create the object.
          Expectation is that if the builder object is created it should give the object which should be created as per the
          inputs passed. Here the try was to create the object immutable as possible. In Other compiled languages one can use
          final to attain the case however it creates problem with python.

          Simple Program to understand Builder Pattern.

          Benefit: Particularly if you see the code you will see tomorrow you dont need to write a new constructor to get the object
                    if the new attribute is added. So the usability will increase at the trade off wrting code for setting the new attribute.
                    With the new constructor writing one may needed to change the application code where the object was used. This may have lead to 
                    failure for older objects which are not using that attribute. Or extra changes to handle those would have required."""
from UserBuilder import UserBuilder
def main():

    # This will fail as the validate checks for the phone
    # user1 = UserBuilder(first_name="Shou",last_name="Oma").build()
    # print(user1)

    user2 = UserBuilder(first_name="Takumi",last_name="Fujiwara").phone("817-819-523").build()
    print(user2)

    user3 = UserBuilder(first_name="Inaho",last_name="Kaizuka").phone("811-129-213").address("Tokyo").age("21").build()
    print(user3)

main()