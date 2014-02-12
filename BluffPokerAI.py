from pokerPlayers import pokerPlayer, pokerPlayerFactory
from game import Game
from poker import Poker
from deck import Deck
import random, sys, pickle, os, learning


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
			printLine = "Games Played:"+str(i)+"\t"
			for key in scores:
				percent = '{percent:.2%}'.format(percent=(float(scores[key]) / float(i)))
				printLine += key+": "+percent+"\t"
			print printLine

def playRandomLearningGames(amountOfGames,updateEvery):

	learning.initLearning()

	players = []
	players.append(["Learner","LEARNING_PLAYER"])
	for i in xrange(2):
		newPlayerType = random.choice(["CONSERVATIVE","BIG_MOUTH","CAUTIOUS_BLUFFER","HEURISTIC_PLAYER"])
		players.append(["Other Player",newPlayerType])

	scores = dict()
	scores["Other Players"] = 0
	scores["Learner"] = 0

	for i in xrange(1,amountOfGames+1):

		players = []
		players.append(["Learner","LEARNING_PLAYER"])
		for j in xrange(2):
			newPlayerType = random.choice(["CONSERVATIVE","BIG_MOUTH","CAUTIOUS_BLUFFER","HEURISTIC_PLAYER"])
			players.append(["Other Players",newPlayerType])

		theGame = Game(players)
		winner = theGame.startGame()
		scores[winner] += 1
		if i%updateEvery == 0:
			printLine = "TRAINING LEARNER: GamesPlayed:"+str(i)+"\t"
			for key in scores:
				percent = '{percent:.2%}'.format(percent=(float(scores[key]) / float(i)))
				printLine += key+": "+percent+"\t"
			print printLine

			learning.updateLearning(updateEvery)

def runDuel(numPlayers,numGames):
	playerTypes = []
	for x in xrange(numPlayers):
		print "Choosing player #"+str(x+1)
		print "1 - Conservative"
		print "2 - Big Mouth"
		print "3 - Cautious Bluffer"
		print "4 - Heuristics"
		print "5 - Human"
		print "6 - Reinforced Learner(2000 games)"
		playerType = raw_input("Enter your choice:")
		while (int(playerType) not in [1,2,3,4,5,6]) or (int(playerType) == 6 and 6 in playerTypes):
			if playerType not in [1,2,3,4,5,6]:
				playerType = raw_input("Invalid choice. Enter your choice:")
			if playerType == 6 and 6 in playerTypes:
				playerType = raw_input("Can't choose two reinforced learners. Enter your choice:")
		playerTypes.append(int(playerType))

	players = []
	playerNum = 1
	for playerType in playerTypes:
		if playerType == 1:
			newPlayer = ["Conservative #"+str(playerNum),"CONSERVATIVE"]
		if playerType == 2:
			newPlayer = ["Big Mouth #"+str(playerNum),"BIG_MOUTH"]
		if playerType == 3:
			newPlayer = ["Cautious Bluffer #"+str(playerNum),"CAUTIOUS_BLUFFER"]
		if playerType == 4:
			newPlayer = ["Heuristics #"+str(playerNum),"HEURISTIC_PLAYER"]
		if playerType == 5:
			newPlayer = ["Human #"+str(playerNum),"HUMAN"]
		if playerType == 6:
			print "Learning will now begin for the RL player."
			print "It will run for 2000 games"
			print "Please be patient...(magic is happening)"
			playRandomLearningGames(2000,50)
			newPlayer = ["Reinforced Learner #"+str(playerNum),"LEARNING_PLAYER"]

		players.append(newPlayer)

		playerNum += 1

	print "######################################"
	print "######################################"
	print "######################################"
	print "######################################"
	print "Games now starting"
	playGame(players,numGames)
	os.remove("learningStats.p")
	print "Done. Thank you for all the fish"


def runAlgorithm():
	if os.path.isfile("learningStats.p"):
		os.remove("learningStats.p")

	print "Welcome to Intro2AI Bluff Poker Project by Asaf & Agam"
	print "How many games would you like them to play?"

	numGames = raw_input("Enter your choice:")
	while int(numGames) <= 0 :
		numGames = raw_input("Invalid choice enter. New choice:")

	print "Which type of match would you like to run:"
	print "1 - one on one"
	print "2 - three way duel"
	print "3 - four way battle"
	numPlayers = raw_input("Enter your choice:")
	while int(numPlayers) not in [1,2,3]:
		numPlayers = raw_input("Invalid choice enter. New choice:")

	runDuel(int(numPlayers)+1,int(numGames))

runAlgorithm()
