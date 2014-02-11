import random, poker
from deck import Deck
from pokerPlayers import pokerPlayerFactory
from poker import Poker


class Game:

	def __init__(self,playerArr,debugMessage,roundStats):
		# STARTING GAME
		self.pokerRules = Poker()
		self.writeDebugMessages = debugMessage
		self.roundStats = roundStats

		# CREATING PLAYERS
		playerFactory = pokerPlayerFactory()
		self.players = []
		for player in playerArr:
			playerName = player[0]
			playerType = player[1]
			newPlayer = playerFactory.newPokerPlayer(playerName,playerType)
			self.players.append(newPlayer)
		random.shuffle(self.players,random.random)


		# PLAYER ORDER
		playerOrder = []
		for player in self.players:
			playerOrder.append(player.name)
		self.debugMessage("PLAYER ORDER WILL BE "+str(playerOrder))

	def startGame(self):

		# ACTUAL GAMEPLAY
		roundNum = 0
		while self.playersLeftForGame():
			startingPlayerIndex = roundNum % len(self.players)
			if self.roundStats:
				print "**********************************"
				print "************ROUND "+str(roundNum)+"***************"
				self.printRoundStats()
				print "**********************************"
			self.playSingleRound(startingPlayerIndex)
			roundNum += 1


		for player in self.players:
			if player.cardsLeft > 0:
				self.debugMessage("THE WINNER IS "+player.name)
				return player.name

	def printRoundStats(self):
		printLen = ""
		for player in self.players:
			printLen += player.name+":"+str(player.cardsLeft)+"\t"
		print printLen

	def playersLeftForGame(self):
		playersWithCards = 0
		for player in self.players:
			if player.cardsLeft > 0:
				playersWithCards += 1
		return playersWithCards > 1


	def playSingleRound(self,startingPlayerIndex):

		self.dealCards()

		for player in self.players:
			player.calibrateStrategy(self)

		self.currentAnnouncedHand=[]

		self.announcingPlayerIndex = startingPlayerIndex

		stillAnnouncing = True
		while stillAnnouncing:

			#Get the next player that is still in the game to announce
			while self.players[self.announcingPlayerIndex].cardsLeft == 0:
					self.announcingPlayerIndex += 1
					self.announcingPlayerIndex %= len(self.players)

			#ANNOUNCEMENT
			self.currentAnnouncedHand = self.players[self.announcingPlayerIndex].announce(self)

			self.debugMessage(self.players[self.announcingPlayerIndex].name+" has announced: "+str(self.currentAnnouncedHand))

			self.firstChallenger = True
			for increment in xrange(1,len(self.players)):
				challengingPlayerIndex = (self.announcingPlayerIndex + increment) % len(self.players)
				if self.players[challengingPlayerIndex].cardsLeft == 0:
					#This player is not in the game anymore
					continue
				if self.players[challengingPlayerIndex].challenge(self):
					#Challenge occured
					stillAnnouncing = False
					self.debugMessage(self.players[challengingPlayerIndex].name+" has decided to challenge!!!!!!!")
					break
				self.debugMessage(self.players[challengingPlayerIndex].name+" has decided not to challenge")
				self.firstChallenger = False
			if stillAnnouncing:
				#Get the index for the next player
				self.announcingPlayerIndex = (self.announcingPlayerIndex + 1) % len(self.players)

		cardsOnTable = self.getNumCardsOnTable()


		self.debugMessage("There will be a standoff now between:")
		self.debugMessage("Announcer:\t"+self.players[self.announcingPlayerIndex].name)
		self.debugMessage("Challenger:\t"+self.players[challengingPlayerIndex].name)
		self.debugMessage("Hand:\t"+str(self.currentAnnouncedHand))
		if self.pokerRules.standOff(cardsOnTable,self.currentAnnouncedHand):
			#STANDOFF!!
			self.players[challengingPlayerIndex].cardsLeft -= 1
			self.debugMessage("The hand was on the table")
		else:
			self.players[self.announcingPlayerIndex].cardsLeft -= 1
			self.debugMessage("The bluff was exposed")

		# reset player settings
		for player in self.players:
			player.resetSettings()



	def debugMessage(self,msg):
		if self.writeDebugMessages:
			print msg

	def dealCards(self):
		theDeck = Deck()

		# DEALING CARDS
		for player in self.players:
			player.cardsInHand = []
			player.playersHand = []
			for i in xrange(player.cardsLeft):
				player.recieveCard(theDeck.dealCard())
			self.debugMessage(player.name+"'s cards are:\t"+str(player.cardsInHand))

	def getNumCardsOnTable(self):
		cardsOnTable = []
		for player in self.players:
			for cardFromPlayer in player.playersHand:
				existOnTable = False
				for cardOnTable in cardsOnTable:
					if cardFromPlayer[0] == cardOnTable[0]:
						cardOnTable[1] += cardFromPlayer[1]
						existOnTable = True

				if not existOnTable:
					cardsOnTable.append(cardFromPlayer)
		return cardsOnTable

	def getNumOfCardsInPlay(self):
		numOfCardsInPlay = 0
		for player in self.players:
			numOfCardsInPlay += len(player.cardsInHand)
		return numOfCardsInPlay
