import random

class Player:

	def __init__(self, ndice):
		self.ndice = ndice
		self.dice = [random.randint(1,7) for i in range(self.ndice)]
	
	def cast(self):
		self.dice = [random.randint(1,7) for i in range(self.ndice)]
	
	#(Number of dice, value of die), None if bluff
	def guess(self, previous_guesses, nplayers):
		if len(previous_guesses) > 0:
			prev_guess = previous_guesses[len(previous_guesses) - 1]



		if random.random() < 0.3:
			return None
		else:	
			return (random.randint(1,7),random.randint(1,7))

