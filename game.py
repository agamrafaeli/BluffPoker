import random
from deck import Deck
from poker import testHand

class Game:

	def __init__(self,playerArr):

		self.players = []
		for player in playerArr:
			newPlayer = dict()
			newPlayer['name'] = player['name']
			newPlayer['agent'] = player['agent']
			newPlayer['numCards'] = 5
			newPlayer['currentHand'] = None
			self.players.append(newPlayer)
		random.shuffle(self.players,random.random)
		self.currentHand = None
		winner = 0
		while self.noWinner():
			winner = self.playSingleRound(winner)

	def playSingleRound(self,startingPlayer):
		roundDeck = deck()
		currentPlayer = int(startingPlayer)
		for player in self.players():
			#Only elgible players??
			for i in xrange(player['numCards']):
				newCard = roundDeck.dealCard()
				player['currentHand'].append(newCard)
		while True:
			(wasChallenge,losingPlayerIndex) = self.playSingleTurn(currentPlayer)
			self.players[losingPlayerIndex]['numCards'] -= 1
			if wasChallenge:
				break
			currentPlayer = (currentPlayer + 1) % len(self.players)


	def playSingleTurn(self,announcingPlayerIndex):
		announcedHand = self.players[announcingPlayerIndex]['agent'].announce(self)
		challenged = False
		for i in xrange(announcingPlayerIndex,len(self.players)):
			if self.players[i]['agent'].challenge(self):
				challengingPlayerIndex = i
				challenged = True
				break
		if challenged:
			cardsInPlay = []
			for player in self.players:
				cardsInPlay = cardsInPlay + list(player['currentHand'])
				if poker.legalHand(cardsInPlay,self.currentHand):
					return (True,challengingPlayerIndex)
				else
					return (True,announcingPlayerIndex)
		return (False,-1)


