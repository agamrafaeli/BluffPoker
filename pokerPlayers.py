import random
from poker import Poker


class pokerPlayerFactory(object):
	def newPokerPlayer(self,name,playerType):
		if playerType == "CONSERVATIVE": 		return ultraConservativePlayer(name)
		if playerType == "BIG_MOUTH": 			return bigMouthPlayer(name)
		if playerType == "CAUTIOUS_BLUFFER":	return cautiousBlufferPlayer(name)
		if playerType == "HUMAN":				return humanPlayer(name)
		if playerType == "HEURISTIC_PLAYER":	return heuristicPlayer(name)
	# if playerType == "LEARNING_PLAYER":		return learningPlayer(name)


class pokerPlayer(object):
	def __init__(self,name):
		self.cardsInHand = [];
		self.playersHand=[];
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

	def calibrateStrategy(self,game):
		self.myCertainHands = game.pokerRules.myCertainHands(self.playersHand)
		self.myOptionalHands = game.pokerRules.myOptionalHands(self.playersHand)

	def learn(self,game): pass

	def resetSettings(self): pass

	def recieveCard(self,card):

		existInHand = False
		for cardVal in self.playersHand:
			if card[0]==cardVal[0]:
				cardVal[1] += 1
				existInHand = True

		if not existInHand:
			self.playersHand.append(([card[0],1]))


		self.cardsInHand.append(card)

	def lostGame(self):
		self.cardsLeft -= 1

class ultraConservativePlayer(pokerPlayer):

	#works with certain hands
	#challenges if last anouncement is better than his best certain hand

	def __init__(self,name):
		super(ultraConservativePlayer,self).__init__(name)

	def announce(self,game):

		currentAnnouncedHand = game.currentAnnouncedHand
		return game.pokerRules.getBestWeakestHandToAnnounce(self.myCertainHands,currentAnnouncedHand)

	def challenge(self,game):
		handAnnounced = game.currentAnnouncedHand
		if self.myCertainHands == [] and game.firstChallenger:
			return True
		highestAvailableHand = self.myCertainHands[-1]
		if game.pokerRules.handStandoff(highestAvailableHand,handAnnounced) or \
			game.pokerRules.equalHands(highestAvailableHand,handAnnounced):
			if game.firstChallenger:
				#The player will not challenge
				#this is because he is certain to have a hand that
				# is stronger then what was announced
				return True
		return False




class cautiousBlufferPlayer(pokerPlayer):
	#Calls ascending hands continuously. With increasing probability calls "Bluff!"
	#Asaf will do this

	def __init__(self,name):
		super(cautiousBlufferPlayer,self).__init__(name)
		self.challengeProbability = 0.04

	def announce(self,game):
		# says the next best hand he can say after the current anouncement

		currentAnnouncedHand = game.currentAnnouncedHand
		handToAnnounce = game.pokerRules.getBestWeakestHandToAnnounce(self.myCertainHands,currentAnnouncedHand)
		if handToAnnounce == []:
			allHandsInGame = game.pokerRules.allHandOptions
			handToAnnounce = game.pokerRules.getBestWeakestHandToAnnounce(allHandsInGame,currentAnnouncedHand)

		return handToAnnounce

	def challenge(self,game):
		self.challengeProbability += 0.01
		probability = self.challengeProbability
		if not game.firstChallenger:
			probability = probability * 0.1
		randomNum = random.random()

		game.debugMessage("probability to challenge now is: "+str(probability))
		game.debugMessage("random number is: "+str(randomNum))
		return  randomNum <= probability

	def resetSettings(self):
		self.challengeProbability = 0.04


class bigMouthPlayer(pokerPlayer):

	def __init__(self,name):
		super(bigMouthPlayer,self).__init__(name)

	def announce(self,game):

		#Can he win the last announced hand?
		#if can, announce the next strong hand he can announce and back up

		currentAnnouncedHand = game.currentAnnouncedHand
		handToAnnounce = game.pokerRules.getBestWeakestHandToAnnounce(self.myCertainHands,currentAnnouncedHand)
		if handToAnnounce == []:
		# says the next best hand he can optionally backup after the current anouncement
			handToAnnounce = game.pokerRules.getBestWeakestHandToAnnounce(self.myOptionalHands,currentAnnouncedHand)
			if handToAnnounce == []:
				allHandsInGame = game.pokerRules.allHandOptions
				handToAnnounce = game.pokerRules.getBestWeakestHandToAnnounce(allHandsInGame,currentAnnouncedHand)

		return handToAnnounce
	def challenge(self,game):
		return False


class humanPlayer(pokerPlayer):

	def __init(self,name):
		super(humanPlayer,self).__init__(name)

	def announce(self,game):
		self.printStats(game)

		print "To select:"
		print "0 for high card.\t 1 for pair. \t\t2 for two pairs."
		print "3 for triplets.\t\t 4 for straight.\t5 for full house."
		print "6 for quad."
		typeOfHand = int(raw_input("Type of hand you are announcing: "))
		secondQuestionFlag = False
		if typeOfHand == 0:
			value = int(raw_input("High card at what level? "))
			return [(value,1)]
		if typeOfHand == 1:
			value = int(raw_input("A pair of what? "))
			return [(value,2)]
		if typeOfHand == 2:
			firstValue = int(raw_input("The first pair is of what value? "))
			secondValue = int(raw_input("And the second pair? "))
			return [(firstValue,2),(secondValue,2)]
		if typeOfHand == 3:
			value = int(raw_input("The triplets are of what value? "))
			return [(value,3)]
		if typeOfHand == 4:
			value = int(raw_input("What is the highest value of the straight? "))
			return [(value-4,1),(value-3,1),(value-2,1),(value-1,1),(value,1)]
		if typeOfHand == 5:
			firstValue = int(raw_input("What value are the triplets? "))
			secondValue = int(raw_input("And what value is the pair? "))
			return [(firstValue,3),(secondValue,2)]
		if typeOfHand == 6:
			value = int(raw_input("What value is the quad?"))
			return [(value,4)]


		print "###################ERROR###################"
		print "BAD TYPE OF HAND ENTERED"
		raw_input("Ctrl+c to break the program")

	def printStats(self,game):
		print "#######################"
		playerStatLine = ""
		for player in game.players:
			playerStatLine += player.name+": "+str(player.cardsLeft)+"\t\t"
		print "Cards left in hands of other players:"
		print playerStatLine
		print "Your cards are:"
		cardLine = ""
		for card in self.cardsInHand:
			cardLine += str(card[0])+" of "+card[1]+"s,"
		print cardLine
		#TODO: Need to add current hand

	def challenge(self,game):
		self.printStats(game)
		print "Are you challenging this current hand?"
		print "1 for YES. \tSomething else for no:\t"
		value = int(raw_input(""))
		if value == 1:
			   return True
		return False

class heuristicPlayer(pokerPlayer):

	def __init__(self,name):
		super(heuristicPlayer,self).__init__(name)
		self.cumulative = 0.0

	def announce(self,game):
		currentAnnouncedHand = game.currentAnnouncedHand
		announcementToGive = game.pokerRules.getBestWeakestHandToAnnounce(self.myCertainHands,currentAnnouncedHand)
		if announcementToGive == []:
			announcementToGive = game.pokerRules.findWeakestStrongestCardShortHand\
					(self.myOptionalHands,self.myCertainHands,currentAnnouncedHand,1,self.playersHand)
			if announcementToGive==[]:
				announcementToGive = game.pokerRules.findWeakestStrongestCardShortHand \
					(self.myOptionalHands,self.myCertainHands,currentAnnouncedHand,2,self.playersHand)
				if announcementToGive==[]:
					announcementToGive = game.pokerRules.findWeakestStrongestCardShortHand \
							(self.myOptionalHands,self.myCertainHands,currentAnnouncedHand,3,self.playersHand)

		return announcementToGive

	def challenge(self,game):

		self.cumulative += 0.025

		numCardsInAnnouncedHand = 0
		for condition in game.currentAnnouncedHand:
			numCardsInAnnouncedHand += condition[1]

		numCardsAnnouncingPlayerHas = len(game.players[game.announcingPlayerIndex].cardsInHand)
		numCardsIHave = len(self.cardsInHand)
		numCardsOnTable = game.getNumCardsOnTable()
		numUnknownCards = numCardsOnTable - numCardsIHave - numCardsAnnouncingPlayerHas
		numCardsIDontSupport = game.pokerRules.cardsMissingToSupportHand(self.playersHand,game.currentAnnouncedHand)


		#If the current hand requires more cards than are in play then challenges
		if numCardsInAnnouncedHand > game.getNumOfCardsInPlay():
			return True

		#If announcing player doesn't have enough cards to support the announced hand
		if numCardsAnnouncingPlayerHas + numUnknownCards < numCardsIDontSupport:
			return True


		probability = 0;

		if numCardsAnnouncingPlayerHas + numUnknownCards == numCardsIDontSupport:
			probability = 0.3
			# print game.roundNum

		# if numCardsIHave > numCardsAnnouncingPlayerHas:
		# 	probability += (0.07*numCardsIDontSupport)

		if random.random() <= probability + self.cumulative:
			return True
		return False



	def resetSettings(self):
		self.cumulative = 0.0


