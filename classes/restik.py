class Restaraunt():
	"""docstring fos Restaraunt"""
	def __init__(self, rest_name, rest_type):
		self.rest_name = rest_name
		self.rest_type = rest_type
		self.numb_served = 0

	def desc_rest(self):
		print('rest name is '+ self.rest_name + ' and type is ' + self.rest_type)

	def open_rest(self):
		print('rest is open')

	def set_numb_served(self,set_num):
		self.numb_served = set_num

	def incr_num_served(self,incr_num):
		self.numb_served += incr_num