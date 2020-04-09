from player import Player

def round(players):
	nplayers = len(players)
	pindex = 0
	prev_guess = []
	guess = (0,0)
	for player in players:
		player.cast()	

	while guess is not None:
		player = players[pindex % nplayers]	
		guess = player.guess(prev_guess, nplayers)
		if guess is not None:
			prev_guess.append(guess)
			pindex += 1
	
		
	if len(prev_guess) > 0:	
		guess = prev_guess[len(prev_guess) - 1]
		truth = 0
		for player in players:
			truth += player.dice.count(guess[1])
	
		winner_index = pindex - 1 % nplayers if guess[0] >= truth else pindex % nplayers
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
