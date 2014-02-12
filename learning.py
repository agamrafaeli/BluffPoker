import pickle
from poker import Poker
import os

challengeStates = None
numGames = 0

def initLearning():
	global challengeStates
	global numGames
	if os.path.isfile("learningStats.p"):
		(challengeStates,numGames) = pickle.load(open("learningStats.p","rb"))
	else:
		poker = Poker()
		challengeStates = [0] * len(poker.allHandOptions)
		allHands = poker.allHandOptions
		for hand in xrange(len(allHands)):
			challengeStates[hand] = [[[0 for x in xrange(5)] for y in xrange(16)] for z in xrange(6)]
		pickle.dump((challengeStates,0),open("learningStats.p","wb"))
		challengeStates = challengeStates


def updateState(handNum,numOfAnnouncerHands,numOfUnknownCards,numOfMissingCards,goodChallenge):
	global challengeStates
	change = -0.025
	if goodChallenge:
		change = 0.015
	try:
		challengeStates[handNum][numOfAnnouncerHands][numOfUnknownCards][numOfMissingCards] += change
	except:
		print "************************************"
		print numOfAnnouncerHands
		print challengeStates[handNum][numOfAnnouncerHands]
		print numOfUnknownCards
		print challengeStates[handNum][numOfAnnouncerHands][numOfUnknownCards]
		print numOfMissingCards
		print challengeStates[handNum][numOfAnnouncerHands][numOfUnknownCards][numOfMissingCards]

def getStateChange(handNum,numOfAnnouncerHands,numOfUnknownCards,numOfMissingCards):
	global challengeStates
	try:
		return challengeStates[handNum][numOfAnnouncerHands][numOfUnknownCards][numOfMissingCards]
	except:
		print "************************************"
		print handNum
		print challengeStates[handNum]
		print numOfAnnouncerHands
		print challengeStates[handNum][numOfAnnouncerHands]
		print numOfUnknownCards
		print challengeStates[handNum][numOfAnnouncerHands][numOfUnknownCards]
		print numOfMissingCards
		print challengeStates[handNum][numOfAnnouncerHands][numOfUnknownCards][numOfMissingCards]

def updateLearning(playedGames):
	global challengeStates
	global numGames
	numGames += playedGames
	pickle.dump((challengeStates,numGames),open("learningStats.p","wb"))

def totalGamesLearned():
	global numGames
	print "Playing after learning from "+str(numGames)+" games"


