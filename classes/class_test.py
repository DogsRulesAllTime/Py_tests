class User():
	""" User comment"""
	def __init__(self,name,mail):
		self.name = name 
		self.mail = mail
		self.acc_data = {}

	def reg(self,login,psw):
		self.login = login
		self.psw = psw
		self.acc_data['login'] = self.login
		self.acc_data['psw'] = self.psw

	def logiq(self,login,psw):
		if str(login) == self.acc_data['login'] and str(psw) == self.acc_data['psw']:
			print('u are loged on')
		else:
			print('wrong login or psw')	

lol = User('qq','mk@,ail.ru')

lol.reg('wierd',123456)

print(lol.acc_data)

lol.reg('log','psw')

print(lol.acc_data)

lol.logiq('log','psw')