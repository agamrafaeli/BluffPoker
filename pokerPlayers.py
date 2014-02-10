from random import random

class pokerPlayerFactory(object):
	def newPokerPlayer(self,name,playerType):
		if playerType == "CONSERVATIVE": 		return ultraConservativePlayer(name)
		if playerType == "BIG_MOUTH": 			return bigMouthPlayer(name)
		if playerType == "CAUTIOUS_BLUFFER":	return cautiousBlufferPlayer(name)
		if playerType == "HUMAN":				return humanPlayer(name)
		if playerType == "HEURISTIC_PLAYER":	return heuristicPlayer(name)
		if playerType == "LEARNING_PLAYER":		return learningPlayer(name)


class pokerPlayer(object):
	def __init__(self,name):
		self.cardsInHand = [];
		self.cardsLeft = 5
		self.name = name;
		self.lowestHand = None
		self.highestHand = None

	def hasHand(self,hand):
		for demand in hand:
			countInPlayer = 0
			for card in self.cardsInHand:
				if card[0] == demand[0]:
					countInPlayer += 1
			if countInPlayer < demand[1]:
				return False
		return True

	def announce(self,game): pass

	def challenge(self,game): pass

	def learn(self,game): pass

	def calibrateStrategy(self,game):
		for hand in game.getRemainingHands():
			if self.hasHand(hand):
				self.lowestHand = list(hand)
				break
		for hand in list(game.getRemainingHands()).reverse():
			if self.hasHand(hand):
				self.highestHand = list(hand)
				break

	def recieveCard(self,card):
		self.cardsInHand.append(card)

	def lostGame():
		self.cardsLeft -= 1

class bigMouthPlayer(pokerPlayer):

	def __init__(self,name):
		super(bigMouthPlayer,self).__init__(name)
		print "Created bigMouthPlayer named "+self.name
		self.challengedCounter = 0

	def announce(self,game):
		return game.getRemainingHands()[0]

	def challenge(self,game):
		self.challengedCounter += 1
		challengeProbability = -0.5
		for i in xrange(1,self.challengedCounter):
			challengeProbability += (1.0/j) - (1.0/(j+1.0))
		return random.random() <= challengeProbability
