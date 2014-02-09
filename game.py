import random, Deck


class Game:

	def __init__(self,playerAgents):

		self.players = []
		for agent in playerAgents:
			newPlayer = dict()
			newPlayer['agent'] = agent
			newPlayer['numCards'] = 5
			newPlayer['current hand'] = None
			self.players.append(newPlayer)
		random.shuffle(self.players,random.random)

	def playSingleRound(self):
		roundDeck = deck()
		for player in self.players():
			player['current hand'] = None

