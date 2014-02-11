__author__ = 'aliveanu'
from deck import Deck
class Poker:
    def initOptions(self):
        handsOptions=[]
        theDeck = Deck()

        #HighCard
        handsOptions.extend(self.getAllHighCards(theDeck.numbers()))


        #ZUG
        handsOptions.extend(self.getAllPairs(theDeck.numbers()))
        #13

        #ZUGAIM
        handsOptions.extend(self.getAllDoublePair(self.getAllPairs(theDeck.numbers())))
        #78

        #Triple
        handsOptions.extend(self.getAllTriplets(theDeck.numbers()))
        #13

        #straight
        handsOptions.extend(self.getAllStraightOptions(theDeck.numbers()))
        #9


        #full House
        handsOptions.extend(self.getAllFullHouseOptions(self.getAllPairs(theDeck.numbers()),self.getAllTriplets(theDeck.numbers())))
        #156

        #foursome
        handsOptions.extend(self.getAllFoursome(theDeck.numbers()))

        return handsOptions

    def getAllHighCards(self,numbersInDeck):
        highCardsList = []
        for num in numbersInDeck:
            highCardsList.append([(num,1)])
        return highCardsList

    def getAllPairs(self,numbersInDeck):
        pairs=[]
        for pairNumber in numbersInDeck:
            pairs.append([(pairNumber,2)])
        return pairs

    def getAllTriplets(self,numbersInDeck):
        triplets=[]
        for tripNumber in numbersInDeck:
            triplets.append([(tripNumber,3)])
        return triplets

    def getAllDoublePair(self,allSinglePairs):
        doublePairList = []
        secondPairOptions = list (allSinglePairs)
        for firstPair in allSinglePairs:
            secondPairOptions.remove(firstPair)
            for secondPair in secondPairOptions:
                singleDoubleTemp = []
                singleDoubleTemp.extend(firstPair)
                singleDoubleTemp.extend(secondPair)
                doublePairList.append(singleDoubleTemp)
        return doublePairList

    def getAllStraightOptions(self,numbersInDeck):
        straightList=[]
        for firstNum in xrange(2,11):
            straightList.append([(firstNum,1),(firstNum+1,1),(firstNum+2,1),(firstNum+3,1),(firstNum+4,1)])
        return straightList

    def getAllFullHouseOptions(self,pairOptions, tripleOptions):
        fullHouseList =[]
        for pair in pairOptions:
            for triple in tripleOptions:
                if pair[0] == triple[0]:
                    continue
                singleFullHouseTuple = []
                singleFullHouseTuple.extend(pair)
                singleFullHouseTuple.extend(triple)
                fullHouseList.append(singleFullHouseTuple)
        return fullHouseList

    def getAllFoursome(self,numbersInDeck):
        foursomeList = []
        for num in numbersInDeck:
            foursomeList.append([(num,4)])
        return foursomeList



    def initHandsOptions(self):
        return self.initOptions()

    def printHandOptions(self):
        print self.initOptions()

    def standOff(self,cardsOnTable,announcement):

        for combination in announcement:
            ifCombinationExists = False
            val = combination[0]
            amountOfVal = combination[1]
            for card in cardsOnTable:
                if card[0] == val:
                    amountOfVal = amountOfVal - card[1]
                if amountOfVal <= 0:
                    ifCombinationExists = True
            if (ifCombinationExists):
                continue
            else:
                return False
        return True

    def myCertainHands(self,hand):
        certainHandsList = []
        for optionalHand in self.initHandsOptions():
            if (self.standOff(hand,optionalHand)):
                certainHandsList.append(optionalHand)
        return certainHandsList

    def isOptionalHAnd(self,hand,optionalHand):
        for cardInHand in hand:
            for cardInOptionalHand in optionalHand:
                if cardInHand[0]==cardInOptionalHand[0]:
                    return True

    def myOptionalHands(self,hand):
        optionalHandsList = []
        for optionalHand in self.initHandsOptions():
            if (self.isOptionalHAnd(hand,optionalHand)):
                optionalHandsList.append(optionalHand)
        print optionalHandsList
        return optionalHandsList

#returns the actual possible strongest hand
    def getStrongestHandFromHand(self,hand):
        handCertainHands = self.myCertainHands(hand)
        return handCertainHands[len(handCertainHands)-1]


#return int value (strength) of the hand
    def getHandStrength(self,hand):
        count = 1
        for handToCheck in self.initHandsOptions():
            if hand==handToCheck:
                return count
            count += 1


#Which hand is stronger = What hand can create the strongest combination
    def handStandoff(self,hand1,hand2):
        hand1Power = self.getHandStrength(self.getStrongestHandFromHand(hand1))
        hand2Power = self.getHandStrength(self.getStrongestHandFromHand(hand2))
        if  hand1Power < hand2Power:
            return True
        return False


#Returns the best weakest hand that the list of vertain hands has that beats the hand to beat
    def getBestWeakestHandToAnnounce(self,listOfCertainHands,handToBeat):
        for hand in listOfCertainHands:
            if self.getHandStrength(hand) > self.getHandStrength(handToBeat):
                return hand
        return []




