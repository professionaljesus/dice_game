from player import Player

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
		prev_guess.append(guess)
		pindex = (pindex + 1) % nplayers
	
		
	if len(prev_guess) > 1:	
		guess = prev_guess[len(prev_guess) - 2]
		truth = 0
		for player in players:
			truth += player.dice.count(guess[1])
	
		winner_index = (pindex - 2) % nplayers if guess[0] >= truth else (pindex - 1) % nplayers
	else: #first player said bluff
		winner_index = 1	

	ret_players = players[winner_index:]
	ret_players.extend(players[:winner_index]) 
	
	ret_players[nplayers - 1].ndice -= 1	
	if ret_players[nplayers - 1].ndice == 0:
		del ret_players[nplayers - 1] 
	
	return ret_players

if __name__ == "__main__":
	nplayers = 5
	ndice = 6
	players = [Player(ndice) for i in range(nplayers)]

	while len(players) > 1:
		players = round(players)
		print(len(players))
