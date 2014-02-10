import random, poker
from deck import Deck
from pokerPlayers import pokerPlayerFactory


class Game:

	def __init__(self,playerArr):
		print "*****STARTING GAME*****"
		self.optionalHands = poker.initOptions()
		self.currentHand = None

		print "*****CREATING PLAYERS*****"
		playerFactory = pokerPlayerFactory()

		self.players = []
		for player in playerArr:
			playerName = player[0]
			playerType = player[1]
			newPlayer = playerFactory.newPokerPlayer(playerName,playerType)
			self.players.append(newPlayer)
		random.shuffle(self.players,random.random)

		print "*****DEALING CARDS*****"

		print "The player to go first is "+self.players[0].name


	def playSingleRound(self,startingPlayer): pass

	def playSingleTurn(self,announcingPlayerIndex): pass

	def getOptionalHands():
		return list(self.optionalHands)
