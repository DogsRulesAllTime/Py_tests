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


class Privileges():
	def __init__(self,priv=['show','delete','create']):
		self.priv = priv
	def show_priv(self):
		for privi in self.priv:
			print(privi)


class Admin(User):
    def __init__(self,name,surname,age):
        super().__init__(name,surname,age)
        self.privileges = Privileges()

odmen = Admin('Oleg','Velikiq',25)
odmen.privileges.show_priv()        

