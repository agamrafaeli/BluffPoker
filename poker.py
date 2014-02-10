__author__ = 'aliveanu'
from deck import Deck





def initOptions():
    handsOptions=[]
    theDeck = Deck()

    #HighCard
    handsOptions.extend(getAllHighCards(theDeck.numbers()))


    #ZUG
    handsOptions.extend(getAllPairs(theDeck.numbers()))
    #13

    #ZUGAIM
    handsOptions.extend(getAllDoublePair(getAllPairs(theDeck.numbers())))
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



def initHandsOptions():
    return initOptions()

def printHandOptions():
    print initOptions()

def standOff(cardsOnTable,anouncement):

    for combination in anouncement:
        ifCombinationExists = False
        val = combination[0]
        amountOfVal = combination[1]
        for playerCardsInTheGame in cardsOnTable:
            for card in playerCardsInTheGame:
                if card[0] == val:
                    amountOfVal = amountOfVal - card[1]
                    if amountOfVal <= 0:
                        ifCombinationExists = True
        if (ifCombinationExists):
            continue
        else:
            return False
    return True

cardsOnTable = ([(2,2),(3,2)],[(6,1),(7,1),(8,1),(9,1),(10,1)])
print standOff(cardsOnTable,([(2,2),(3,3)]))
# print standOff(cardsOnTable,([[2,3]]))
