from player import Player

def valid_guess(guess, prev_guess):
	if len(prev_guess) == 0:
		return True
	prev_guess = prev_guess[-1]
	if guess is None:
		return True
	if guess[0] > prev_guess[0]:
		return True
	if guess[0] == prev_guess[0] and guess[1] > prev_guess[1]:
		return True

	return False
	

def round(players):
	nplayers = len(players)
	pindex = 0
	prev_guess = []
	guess = (0,0)
	
	player_dice = [0]*nplayers

	for i in range(nplayers):
		players[i].cast()	
		player_dice[i] = players[i].ndice

	while guess is not None:
		player = players[pindex]	
		
		guess = player.guess(pindex, prev_guess, nplayers, player_dice)
		assert valid_guess(guess, prev_guess), 'Invalid guess'
		print(guess)
			
		prev_guess.append(guess)
		pindex = (pindex + 1) % nplayers
	
		
	winner_index = 1	
	if len(prev_guess) > 1:	
		guess = prev_guess[-2]
		truth = 0
		for player in players:
			truth += player.dice.count(guess[1])
		print('truth',truth,'guess',guess[0])
		if guess[0] >= truth:
			winner_index = (pindex - 2) % nplayers 
		else:
			winner_index = (pindex - 1) % nplayers

	ret_players = players[winner_index:]
	ret_players.extend(players[:winner_index]) 
	
	ret_players[-1].ndice -= 1	
	if ret_players[-1].ndice == 0:
		del ret_players[-1] 
	
	return ret_players

if __name__ == "__main__":
	nplayers = 5
	ndice = 6
	players = [Player(ndice) for i in range(nplayers)]

	while len(players) > 1:
		players = round(players)
		print(len(players))
