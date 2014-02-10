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

    def getAllHighCards(numbersInDeck):
        highCardsList = []
        for num in numbersInDeck:
            highCardsList.append([(num,1)])
        return highCardsList

    def getAllPairs(numbersInDeck):
        pairs=[]
        for pairNumber in numbersInDeck:
            pairs.append([(pairNumber,2)])
        return pairs

    def getAllTriplets(numbersInDeck):
        triplets=[]
        for tripNumber in numbersInDeck:
            triplets.append([(tripNumber,3)])
        return triplets

    def getAllDoublePair(allSinglePairs):
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

    def getAllStraightOptions(numbersInDeck):
        straightList=[]
        for firstNum in xrange(2,11):
            straightList.append([(firstNum,1),(firstNum+1,1),(firstNum+2,1),(firstNum+3,1),(firstNum+4,1)])
        return straightList

    def getAllFullHouseOptions(pairOptions, tripleOptions):
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

    def getAllFoursome(numbersInDeck):
        foursomeList = []
        for num in numbersInDeck:
            foursomeList.append([(num,4)])
        return foursomeList



    def initHandsOptions(self):
        return self.initOptions()

    def printHandOptions(self):
        print self.initOptions()

    def standOff(cardsOnTable,announcement):

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
