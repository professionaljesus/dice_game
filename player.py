import random

class Player:

	def __init__(self, ndice):
		self.ndice = ndice
		self.dice = [random.randint(1,6) for i in range(self.ndice)]
	
	def cast(self):
		self.dice = [random.randint(1,6) for i in range(self.ndice)]
	
	#(Number of dice, value of die), None if bluff
	def guess(self, player_index, previous_guesses, nplayers, players_ndice):
		other_dice = 0
		for nd in players_ndice:
			other_dice += nd

		other_dice -= self.ndice;
		
		if len(previous_guesses) > 0:
			guess = previous_guesses[len(previous_guesses) - 1]
			if (1.0/6.0)*other_dice + self.dice.count(guess[1]) < guess[0]:
				return None
			else:
				return (guess[0] + 1, guess[1])  
		
		n_of_each = [0]*6
		for d in self.dice:
			n_of_each[d - 1] += 1
		
		fmax = max(n_of_each)
		most_of = n_of_each.index(fmax) + 1
		n_of_that = int(1.0/6.0*other_dice) + fmax
		return (n_of_that, most_of)
