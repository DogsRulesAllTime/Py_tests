class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

class Elec(Car):
	def __init__(self,make,model,year):
		super().__init__(model,make,year)
		self.battery = Battery()

class Battery():
	def __init__(self,bat_size=90):
		self.bat_size = bat_size

	def get(self):
		if self.bat_size == 90:
			print(90)
		elif self.bat_size == 110:
			print(110)

	def bat_siz(self,size):
		self.bat_size = size


c = Elec('tesla','model s',1998)
c.battery.get()
c.battery.bat_siz(110)
c.battery.get()
