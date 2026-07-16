## Encapsulation

# #1. Private Username
class UserProfile:
    def __init__(self, username):
        self.__username = username
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, new_username):
        self.__username = new_username
        

profile = UserProfile("alice99")   
print(profile.username)

print(profile.__username)






