__author__ = 'aliveanu'
from deck import Deck





def initOptions():
    handsOptions=[]
    theDeck = Deck()

    #HighCard


    #ZUG
    handsOptions.extend(getAllPairs(theDeck.numbers()))
    #13

    #ZUGAIM
    handsOptions.extend(getAllDoublePair(handsOptions))
    #78

    #Triple
    handsOptions.extend(getAllTriplets(theDeck.numbers()))
    #13

    #straight
    handsOptions.extend(getAllStraightOptions(theDeck.numbers()))
    #9


    #full House
    handsOptions.extend(getAllFullHouseOptions(getAllPairs(theDeck.numbers()),getAllTriplets(theDeck.numbers())))
    #156

    #foursome
    handsOptions.extend(getAllFoursome(theDeck.numbers()))

    return handsOptions

def getAllPairs(numbersInDeck):
    pairs=[]
    for pairNumber in numbersInDeck:
        pairs.append([pairNumber,pairNumber])
    return pairs

def getAllTriplets(numbersInDeck):
    triplets=[]
    for tripNumber in numbersInDeck:
        triplets.append([tripNumber,tripNumber,tripNumber])
    return triplets

def getAllDoublePair(allSinglePairs):
    doublePairList = []
    secondPairOptions = list (allSinglePairs)
    for firstPair in allSinglePairs:
        secondPairOptions.remove(firstPair)
        for secondPair in secondPairOptions:
            doublePairList.append(firstPair+secondPair)
    return doublePairList

def getAllStraightOptions(numbersInDeck):
    straightList=[]
    for firstNum in xrange(2,11):
        straightList.append([firstNum,firstNum+1,firstNum+2,firstNum+3,firstNum+4])
    return straightList

def getAllFullHouseOptions(pairOptions, tripleOptions):
    fullHouseList =[]
    for pair in pairOptions:
        for triple in tripleOptions:
            if pair[0] == triple[0]:
                continue
            fullHouseList.append(pair + triple)
    return fullHouseList

def getAllFoursome(numbersInDeck):
    foursomeList = []
    for num in numbersInDeck:
        foursomeList.append([num,num,num,num])
    return foursomeList



def initHandsOptions():
    return initOptions()

def printHandOptions():
    print initOptions()

def standOff(cardsOnTable,anouncement):
    for combination in anouncement:
        ifCombinationExists = False
        val = combination[0]
        amountOfVal = combination[1]
        for palyerCardsIntheGame in cardsOnTable:
            for card in palyerCardsIntheGame:
                if card == type :
                    amountOfVal = amountOfVal-1
                    if amountOfVal==0:
                        ifCombinationExists = True
        if (ifCombinationExists):
            continue
        else:
            return False
    return True

cardsOnTable = ([2,2,2,3,4],[6,7,8,9,10,11])
# print standOff(handsOptions,((2,4),(3,2)))
print standOff(cardsOnTable,([[2,3]]))
