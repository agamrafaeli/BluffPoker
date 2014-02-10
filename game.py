import random, poker
from deck import Deck


class Game:

	def __init__(self,playerArr):

		self.optionalHands = poker.initOptions()
		self.currentHand = None

		self.players = []
		for player in playerArr:
			newPlayer =
			newPlayer['name'] = player['name']
			newPlayer['agent'] = player['agent']
			newPlayer['numCards'] = 5
			newPlayer['currentHand'] = None
			self.players.append(newPlayer)
		random.shuffle(self.players,random.random)


		winner = 0
		while self.noWinner():
			winner = self.playSingleRound(winner)

	def playSingleRound(self,startingPlayer): pass

	def playSingleTurn(self,announcingPlayerIndex): pass

	def getOptionalHands():
		return list(self.optionalHands)
