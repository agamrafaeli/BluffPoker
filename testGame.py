from pokerPlayers import pokerPlayer, pokerPlayerFactory
from game import Game
from poker import Poker
from deck import Deck
import random, sys
import pickle
import learning


def playGame(players,amountOfGames):

	learning.initLearning()

	scores = dict()
	for player in players:
		scores[player[0]] = 0

	for i in xrange(1,amountOfGames+1):

		theGame = Game(players)
		winner = theGame.startGame()
		scores[winner] += 1
		if i%50 == 0:
			printLine = "Iterator:"+str(i)+"\t"
			for key in scores:
				percent = '{percent:.2%}'.format(percent=(float(scores[key]) / float(i)))
				printLine += key+": "+percent+"\t"
			print printLine

def playRandomLearningGames(amountOfGames,updateEvery):

	learning.initLearning()

	players = []
	players.append(["Learning","LEARNING_PLAYER"])
	for i in xrange(3):
		newPlayerType = random.choice(["CONSERVATIVE","BIG_MOUTH","CAUTIOUS_BLUFFER","HEURISTIC_PLAYER"])
		players.append(["Other Player",newPlayerType])

	scores = dict()
	scores["Learning"] = 0
	scores["Other Player"] = 0

	for i in xrange(1,amountOfGames+1):

		players = []
		players.append(["Learning","LEARNING_PLAYER"])
		for j in xrange(3):
			newPlayerType = random.choice(["CONSERVATIVE","BIG_MOUTH","CAUTIOUS_BLUFFER","HEURISTIC_PLAYER"])
			players.append(["Other Player",newPlayerType])

		theGame = Game(players)
		winner = theGame.startGame()
		scores[winner] += 1
		if i%updateEvery == 0:
			printLine = "Iterator:"+str(i)+"\t"
			for key in scores:
				percent = '{percent:.2%}'.format(percent=(float(scores[key]) / float(updateEvery)))
				printLine += key+": "+percent+"\t"
			print printLine

			learning.updateLearning(updateEvery)

			scores = dict()
			for player in players:
				scores[player[0]] = 0

amountOfGames = int(sys.argv[1])
updateEvery = int(sys.argv[2])

playRandomLearningGames(amountOfGames, updateEvery)

# players = []
# # players.append(["Conservative1","CONSERVATIVE"])
# players.append(["Learning","LEARNING_PLAYER"])
# # players.append(["Conservative2","CONSERVATIVE"])
# # players.append(["Conservative3","CONSERVATIVE"])
# players.append(["Cautious Bluffer1","CAUTIOUS_BLUFFER"])

# playGame(players,amountOfGames)
