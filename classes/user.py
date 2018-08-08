class User():
    """class User"""

    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        self.login_atemp = 0

    def user_info(self):
        print(self.name,' ',self.surname,' ',self.age)

    def great_user(self):
        print('Hello ',self.name)

    def increment_login_atemp(self):
        self.login_atemp+=1

    def reset_login_atemp(self):
        self.login_atemp = 0