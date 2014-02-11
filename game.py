import random, poker
from deck import Deck
from pokerPlayers import pokerPlayerFactory


class Game:

	def __init__(self,playerArr):
		# STARTING GAME

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
			raw_input("")
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

		announcingPlayerIndex = startingPlayerIndex
		stillAnnouncing = True
		while stillAnnouncing:
			#ANNOUNCEMENT
			announcedHand = self.players[announcingPlayerIndex].announce(self)
			for increment in xrange(1,len(self.players)):
				challengingPlayerIndex = (announcingPlayerIndex + increment) % len(self.players)
				if self.players[challengingPlayerIndex].cardsLeft == 0:
					#PLAYER NOT IN GAME ANYMORE
					continue
				if self.players[challengingPlayerIndex].challenge(self):	#CHALLENGE
					# print self.players[challengingPlayerIndex].name+" has challenged"
					stillAnnouncing = False
					break
				# else:
				# 	print self.players[challengingPlayerIndex].name+" kept silent"
			if stillAnnouncing:
				#GET NEXT ANNOUNCING PLAYER
				announcingPlayerIndex = (announcingPlayerIndex + 1) % len(self.players)
				while self.players[announcingPlayerIndex].cardsLeft == 0:
					announcingPlayerIndex = (announcingPlayerIndex + 1) % len(self.players)


		#Add info for standoff

		if poker.standOff(announcedHand) <= 0.5:		#STANDOFF!!
			self.players[challengingPlayerIndex].cardsLeft -= 1
		else:
			self.players[announcingPlayerIndex].cardsLeft -= 1


	def getOptionalHands():
		return list(self.optionalHands)
