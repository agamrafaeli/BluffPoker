import random

class Deck:

	def suits(self):
		return ["Heart","Diamond","Spade","Clover"]

	def numbers(self):
		return range(2,15);

	def __init__(self):
		cards = []
		for suit in self.suits():
			for number in self.numbers():
				cards.append((number,suit))
		random.shuffle(cards,random.random)
		self.cards = cards

	def dealCard(self):
		dealtCard = self.cards.pop()
		return dealtCard
