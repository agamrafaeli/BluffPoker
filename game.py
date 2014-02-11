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
		print "PLAYER ORDER WILL BE "+str(playerOrder)


		# ACTUAL GAMEPLAY
		roundNum = 0
		while self.playersLeftForGame():
			startingPlayerIndex = roundNum % len(self.players)
			print "**********************************"
			print "************ROUND "+str(roundNum)+"***************"
			self.printRoundStats()
			print "**********************************"
			self.playSingleRound(startingPlayerIndex)
			roundNum += 1


		for player in self.players:
			if player.cardsLeft > 0:
				print "THE WINNER IS "+player.name
				break

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

		theDeck = Deck()

		# DEALING CARDS
		for player in self.players:
			player.cardsInHand = []
			for i in xrange(player.cardsLeft):
				player.recieveCard(theDeck.dealCard())
			print player.name+"'s cards are:\t"+str(player.cardsInHand)

		self.currentAnnouncedHand=[]


		announcingPlayerIndex = startingPlayerIndex
		stillAnnouncing = True
		while stillAnnouncing:
			#ANNOUNCEMENT
			print self.players[announcingPlayerIndex].name+" will announce now:"
			self.currentAnnouncedHand = self.players[announcingPlayerIndex].announce(self)
			print "He has announced: "+str(self.currentAnnouncedHand)
			self.firstChallenger = True
			for increment in xrange(1,len(self.players)):
				challengingPlayerIndex = (announcingPlayerIndex + increment) % len(self.players)
				if self.players[challengingPlayerIndex].cardsLeft == 0:
					#PLAYER NOT IN GAME ANYMORE
					continue
				print self.players[challengingPlayerIndex].name+" is deciding whether to challenge now:"
				if self.players[challengingPlayerIndex].challenge(self):	#CHALLENGE
					# print self.players[challengingPlayerIndex].name+" has challenged"
					stillAnnouncing = False
					print "He has decided to challenge!!!!!!!"
					break
				print "He has decided not to challenge"
				self.firstChallenger = False
				# else:
				# 	print self.players[challengingPlayerIndex].name+" kept silent"
			if stillAnnouncing:
				#GET NEXT ANNOUNCING PLAYER
				announcingPlayerIndex = (announcingPlayerIndex + 1) % len(self.players)
				while self.players[announcingPlayerIndex].cardsLeft == 0:
					announcingPlayerIndex = (announcingPlayerIndex + 1) % len(self.players)

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

		print "There will be a standoff now between:"
		print "Announcer:\t"+self.players[announcingPlayerIndex].name
		print "Challenger:\t"+self.players[challengingPlayerIndex].name
		print "Hand:\t"+str(self.currentAnnouncedHand)
		if self.pokerRules.standOff(cardsOnTable,self.currentAnnouncedHand):		#STANDOFF!!
			self.players[challengingPlayerIndex].cardsLeft -= 1
			print "The hand was on the table"
		else:
			self.players[announcingPlayerIndex].cardsLeft -= 1
			print "The bluff was exposed"

		# reset player settings
		for player in self.players:
			player.resetSettings()
		raw_input("")


	def getOptionalHands():
		return list(self.optionalHands)
