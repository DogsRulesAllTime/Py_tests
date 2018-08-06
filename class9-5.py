class User():
    """class User"""

    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

    def user_info(self):
        print(self.name,' ',self.surname,' ',self.age)

    def great_user(self):
        print('Hello ',self.name)


pavel = User('Pavel','Zobov',23)

pavel.user_info()

pavel.great_user()
