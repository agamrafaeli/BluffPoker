from random import random
from poker import Poker


class pokerPlayerFactory(object):
    def newPokerPlayer(self,name,playerType):
        if playerType == "CONSERVATIVE": 		return ultraConservativePlayer(name)
        if playerType == "BIG_MOUTH": 			return bigMouthPlayer(name)
        if playerType == "CAUTIOUS_BLUFFER":	return cautiousBlufferPlayer(name)
        if playerType == "HUMAN":				return humanPlayer(name)
        # if playerType == "HEURISTIC_PLAYER":	return heuristicPlayer(name)
        # if playerType == "LEARNING_PLAYER":		return learningPlayer(name)


class pokerPlayer(object):
    def __init__(self,name):
        self.cardsInHand = [];
        self.playersHand=[];
        self.cardsLeft = 5
        self.name = name;
        self.lowestHand = None
        self.highestHand = None

    def hasHand(self,hand):
        for demand in hand:
            countInPlayer = 0
            for card in self.cardsInHand:
                if card[0] == demand[0]:
                    countInPlayer += 1
            if countInPlayer < demand[1]:
                return False
        return True

    def announce(self,game): pass

    def challenge(self,game): pass

    def learn(self,game): pass

    def calibrateStrategy(self,game):
        for hand in game.getRemainingHands():
            if self.hasHand(hand):
                self.lowestHand = list(hand)
                break
        for hand in list(game.getRemainingHands()).reverse():
            if self.hasHand(hand):
                self.highestHand = list(hand)
                break

    def recieveCard(self,card):

        existInHand = False
        for cardVal in self.playersHand:
            if card[0]==cardVal[0]:
                cardVal[1] += 1
                existInHand = True

        if not existInHand:
            self.playersHand.append(([card[0],1]))


        self.cardsInHand.append(card)

    def lostGame(self):
        self.cardsLeft -= 1

class bigMouthPlayer(pokerPlayer):

    def __init__(self,name):
        super(bigMouthPlayer,self).__init__(name)
        print "Created bigMouthPlayer named "+ self.name
        self.challengedCounter = 0

    def announce(self,game):
        return game.getRemainingHands()[0]
        #check what was anounced till now
        #Can he win the last announced hand?
            #if can, anounce the next strong hand he can anounce and back up

    def challenge(self,game):
        self.challengedCounter += 1
        challengeProbability = -0.5
        for i in xrange(1,self.challengedCounter):
            challengeProbability += (1.0/i) - (1.0/(i+1.0))
        return random.random() <= challengeProbability


class ultraConservativePlayer(pokerPlayer):

    #works with certain hands
    #challenges if last anouncement is better than his best certain hand

    def __init__(self,name):
        super(ultraConservativePlayer,self).__init__(name)
        print "Created ultra Conservative Player named "+self.name

    def announce(self,game):
        myCertainHands = game.pokerRules.myCertainHands(self.playersHand)
        currentAnnouncedHand = game.currentAnnouncedHand
        return game.pokerRules.getBestWeakestHandToAnnounce(myCertainHands,currentAnnouncedHand)

    def challenge(self,game):
        handAnnounced = game.currentAnnouncedHand
        highestAvailableHand = game.pokerRules.myCertainHands(self.playersHand)[-1]
        if game.pokerRules.handStandoff(highestAvailableHand,handAnnounced):
        	if game.firstChallenger:
	            #The player will not challenge
	            #this is because he is certain to have a hand that
	            # is stronger then what was announced
	            return True
        return False



class cautiousBlufferPlayer(pokerPlayer):
    #Calls ascending hands continuously. With increasing probability calls "Bluff!"
    #Asaf will do this

    def __init__(self,name):
        super(cautiousBlufferPlayer,self).__init__(name)
        print "Created Cautious Bluffer Player named "+self.name
        self.challengedCounter = 0

    def announce(self,game):
        poker = Poker()

        # says the next best hand he can say after the current anouncement
        handToAnnounce = poker.getBestWeakestHandToAnnounce(poker.initHandsOptions(),self.getCurrentAnnouncedHand())
        return handToAnnounce

    def challenge(self,game):
        self.challengedCounter += 1
        challengeProbability = 0.025
        for i in xrange(1,self.challengedCounter):
            challengeProbability += 0.025

        return random.random() <= challengeProbability


class humanPlayer(pokerPlayer):

       def __init(self,name):
               super(bigMouthPlayer,self).__init__(name)
               print "Created human player named "+self.name

       def announce(self,game):
               self.printStats(game)

               print "To select:"
               print "0 for high card.\t 1 for pair. \t\t2 for two pairs."
               print "3 for triplets.\t\t 4 for straight.\t5 for full house."
               print "6 for quad."
               typeOfHand = int(raw_input("Type of hand you are announcing: "))
               secondQuestionFlag = False
               if typeOfHand == 0:
                       value = int(raw_input("High card at what level? "))
                       return [(value,1)]
               if typeOfHand == 1:
                       value = int(raw_input("A pair of what? "))
                       return [(value,2)]
               if typeOfHand == 2:
                       firstValue = int(raw_input("The first pair is of what value? "))
                       secondValue = int(raw_input("And the second pair? "))
                       return [(firstValue,2),(secondValue,2)]
               if typeOfHand == 3:
                       value = int(raw_input("The triplets are of what value? "))
                       return [(value,3)]
               if typeOfHand == 4:
                       value = int(raw_input("What is the highest value of the straight? "))
                       return [(value-4,1),(value-3,1),(value-2,1),(value-1,1),(value,1)]
               if typeOfHand == 5:
                       firstValue = int(raw_input("What value are the triplets? "))
                       secondValue = int(raw_input("And what value is the pair? "))
                       return [(firstValue,3),(secondValue,2)]
               if typeOfHand == 6:
                       value = int(raw_input("What value is the quad?"))
                       return [(value,4)]


               print "###################ERROR###################"
               print "BAD TYPE OF HAND ENTERED"
               raw_input("Ctrl+c to break the program")

       def printStats(self,game):
               print "#######################"
               playerStatLine = ""
               for player in game.players:
                       playerStatLine += player.name+": "+str(player.cardsLeft)+"\t\t"
               print "Cards left in hands of other players:"
               print playerStatLine
               print "Your cards are:"
               cardLine = ""
               for card in self.cardsInHand:
                       cardLine += str(card[0])+" of "+card[1]+"s,"
               print cardLine
               #TODO: Need to add current hand

       def challenge(self,game):
               self.printStats(game)

               print "Are you challenging this current hand?"
               print "1 for YES. \tSomething else for no:\t"
               value = int(raw_input(""))
               if value == 1:
                       return True
               return False
