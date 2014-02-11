from pokerPlayers import pokerPlayer
from game import Game

players = []
players.append(["Conservative1","CONSERVATIVE"])
players.append(["Cautious Bluffer1","CAUTIOUS_BLUFFER"])
players.append(["Cautious Bluffer2","CAUTIOUS_BLUFFER"])
players.append(["Conservative2","CONSERVATIVE"])
# players.append(["Big Mouth","BIG_MOUTH"])

scores = dict()
for player in players:
	scores[player[0]] = 0

for i in xrange(1000):
	theGame = Game(players,False,False)
	winner = theGame.startGame()
	scores[winner] += 1
	if i%50 == 0:
		print scores
print scores

