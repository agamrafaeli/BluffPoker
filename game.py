import random, poker
from deck import Deck
from pokerPlayers import pokerPlayerFactory
from poker import Poker


class Game:

	def __init__(self,playerArr):
		# STARTING GAME
		self.pokerRules = Poker()

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

	def startGame(self):

		# ACTUAL GAMEPLAY
		self.roundNum = 0
		while self.playersLeftForGame():
			startingPlayerIndex = self.roundNum % len(self.players)
			self.playSingleRound(startingPlayerIndex)
			self.roundNum += 1

		# FINDING THE WINNER
		for player in self.players:
			if player.cardsLeft > 0:
				return player.name

	def playersLeftForGame(self):
		playersWithCards = 0
		for player in self.players:
			if player.cardsLeft > 0:
				playersWithCards += 1
		return playersWithCards > 1

	def playSingleRound(self,startingPlayerIndex):

		# ROUND INIT
		self.dealCards()
		for player in self.players:
			player.calibrateStrategy(self)
		self.currentAnnouncedHand=[]
		self.announcingPlayerIndex = startingPlayerIndex
		stillAnnouncing = True

		# ROUND ACTUAL PLAY
		while stillAnnouncing:

			#Get the next player that is still in the game to announce
			while self.players[self.announcingPlayerIndex].cardsLeft == 0:
					self.announcingPlayerIndex += 1
					self.announcingPlayerIndex %= len(self.players)


			#ANNOUNCEMENT
			self.currentAnnouncedHand = self.players[self.announcingPlayerIndex].announce(self)
			self.firstChallenger = True

			for increment in xrange(1,len(self.players)):
				challengingPlayerIndex = (self.announcingPlayerIndex + increment) % len(self.players)

				if self.players[challengingPlayerIndex].cardsLeft == 0:
					#This player is not in the game anymore
					continue

				if self.currentAnnouncedHand == [(14,4)]:
					# Highest available hand
					stillAnnouncing = False
					break

				if self.players[challengingPlayerIndex].challenge(self):
					#Challenge occured
					stillAnnouncing = False
					break

				self.firstChallenger = False

			#Get the index for the next player
			if stillAnnouncing:
				self.announcingPlayerIndex = (self.announcingPlayerIndex + 1) % len(self.players)


		# STANDOFF
		goodChallenge = self.pokerRules.standOff(self.cardsOnTable,self.currentAnnouncedHand)


		# PLAYERS LEARN AND RECALIBERATE
		for player in self.players:
			player.learn(self,goodChallenge)
			player.resetSettings()

		# UPDATE PLAYERS CARD QUOTA AFTER STANDOFF
		if goodChallenge:
			self.players[self.announcingPlayerIndex].cardsLeft -= 1
		else:
			self.players[challengingPlayerIndex].cardsLeft -= 1

	def dealCards(self):
		theDeck = Deck()

		# DEALING CARDS
		counter = 0
		for player in self.players:
			player.cardsInHand = []
			player.playersHand = []
			for i in xrange(player.cardsLeft):
				player.recieveCard(theDeck.dealCard())
				counter += 1

		# INITING TABLE VARIABLES
		cardsOnTable = []
		self.numCardsOnTable = 0
		for player in self.players:
			for cardFromPlayer in player.playersHand:
				self.numCardsOnTable += cardFromPlayer[1]
				existOnTable = False
				for cardOnTable in cardsOnTable:
					if cardFromPlayer[0] == cardOnTable[0]:
						cardOnTable[1] += cardFromPlayer[1]
						existOnTable = True

				if not existOnTable:
					cardsOnTable.append(cardFromPlayer)

		self.cardsOnTable = cardsOnTable

	def getNumCardsOnTable(self):
		return self.numCardsOnTable

