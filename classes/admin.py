# from user import User
import user

class Admin(user.User):
    def __init__(self,name,surname,age):
        super().__init__(name,surname,age)
        self.privileges = Privileges()

class Privileges():
	def __init__(self,priv=['show','delete','create']):
		self.priv = priv
	def show_priv(self):
		for privi in self.priv:
			print(privi)

