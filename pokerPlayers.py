from random import random
from poker import Poker


class pokerPlayerFactory(object):
    def newPokerPlayer(self,name,playerType):
        if playerType == "CONSERVATIVE": 		return ultraConservativePlayer(name)
        if playerType == "BIG_MOUTH": 			return bigMouthPlayer(name)
        # if playerType == "CAUTIOUS_BLUFFER":	return cautiousBlufferPlayer(name)
        # if playerType == "HUMAN":				return humanPlayer(name)
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
        self.currentAnnouncedHand=[]



    def getCurrentAnnouncedHand(self):
        return  self.currentAnnouncedHand

    def setCurrentAnnouncedHAnd(self, hand):
        self.currentAnnouncedHand = hand

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

    #works with certain and challenges if last anouncement is better then his best certain hand

    def __init__(self,name):
        super(ultraConservativePlayer,self).__init__(name)
        print "Created ultra Conservative Player named "+self.name
        self.challengedCounter = 0

    def announce(self,game):
        poker = Poker()
        handToAnnounce = poker.getBestWeakestHandToAnnounce(poker.myCertainHands(),self.getCurrentAnnouncedHand())
        return handToAnnounce

    def challenge(self,game):
        handAnnounced = self.getCurrentAnouncedHand()
        poker = Poker()
        highestAvailableHand = poker.myCertainHands()[len(game.getRemainingHands()-1)]
        if poker.handStandoff(handAnnounced,highestAvailableHand):
            #The player will not challenge because he is certain to have a hand in hand that
            # is stronger then what was announced
            return False
        self.challengedCounter += 1
        return True



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




