import random 
z = random.randint(1, 10)

# print(z)

class Die():
	def __init__(self, sides):
		self.sides = sides

	def roll_die(self):
		print(random.randint(1,self.sides))

roll = Die(5)
roll.roll_die()
roll.roll_die()
roll.roll_die()
roll.roll_die()
roll.roll_die()
roll.roll_die()

twenty = Die(20)	
twenty.roll_die()
twenty.roll_die()
ten = Die(10)	
ten.roll_die()
ten.roll_die()