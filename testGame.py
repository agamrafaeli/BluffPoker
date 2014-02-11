from pokerPlayers import pokerPlayer, pokerPlayerFactory
from game import Game
from poker import Poker
from deck import Deck
import random, sys


def playGame(players):
	scores = dict()
	for player in players:
		scores[player[0]] = 0

	for i in xrange(int(sys.argv[1])):
		theGame = Game(players,False,False)
		winner = theGame.startGame()
		scores[winner] += 1
	printLine = "Iterator:"+str(i)+"\t"
	for key in scores:
		percent = int((float(scores[key]) / i) * 100)
		printLine += key+": "+str(percent)+"%\t"
	print printLine

players = []
players.append(["Conservative1","CONSERVATIVE"])
players.append(["Heuristic","HEURISTIC_PLAYER"])
# players.append(["Conservative2","CONSERVATIVE"])
# players.append(["Conservative3","CONSERVATIVE"])
# players.append(["Cautious Bluffer1","CAUTIOUS_BLUFFER"])

playGame(players)

players = []
# players.append(["Conservative1","CONSERVATIVE"])
# players.append(["Cautious Bluffer1","CAUTIOUS_BLUFFER"])
players.append(["Big Mouth","BIG_MOUTH"])
players.append(["Heuristic","HEURISTIC_PLAYER"])
playGame(players)

players = []
# players.append(["Conservative1","CONSERVATIVE"])
players.append(["Cautious Bluffer1","CAUTIOUS_BLUFFER"])
players.append(["Heuristic","HEURISTIC_PLAYER"])
playGame(players)

# players = []
# players.append(["Conservative1","CONSERVATIVE"])
# players.append(["Heuristic","HEURISTIC_PLAYER"])
# players.append(["Big Mouth","BIG_MOUTH"])
# playGame(players)

# players = []
# players.append(["Cautious Bluffer1","CAUTIOUS_BLUFFER"])
# players.append(["Heuristic","HEURISTIC_PLAYER"])
# players.append(["Big Mouth","BIG_MOUTH"])
# playGame(players)

# players = []
# players.append(["Heuristic","HEURISTIC_PLAYER"])
# players.append(["Cautious Bluffer1","CAUTIOUS_BLUFFER"])
# playGame(players)
# # players.append(["Cautious Bluffer2","CAUTIOUS_BLUFFER"])

# players = []
# players.append(["Heuristic","HEURISTIC_PLAYER"])
# players.append(["Big Mouth","BIG_MOUTH"])
# playGame(players)



# cardsMissingToSupportHand tests
# for j in xrange(10):
# 	p = Poker()
# 	deck = Deck()
# 	factory = pokerPlayerFactory()
# 	player = factory.newPokerPlayer("John","BIG_MOUTH")
# 	for i in xrange(random.randint(2,20)):
# 		player.recieveCard(deck.dealCard())
# 	group = player.playersHand
# 	hand = p.allHandOptions[random.randint(0,len(p.allHandOptions))]
# 	missing = p.cardsMissingToSupportHand(group,hand)
# 	print "******************************"
# 	print "Group:\t\t"+str(group)
# 	print "Hand:\t\t"+str(hand)
# 	print "Missing:\t"+str(missing)

