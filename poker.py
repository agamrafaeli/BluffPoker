__author__ = 'aliveanu'
from deck import Deck


handsOptions=[]


def initOptions():
    theDeck = Deck()
    from itertools import product
    for num in theDeck.numbers():
        singleNum=[]
        singleNum.append(num)
        numOptions = list(product(singleNum,theDeck.suits()))
        pairs = createDouble(numOptions)

        #ZUGAIM
        tmp = list (pairs)
        for couple in pairs:
            tmp.remove(couple)
            for couple1 in tmp:
                #no need to add this
                if (couple[0][0] == couple1[0][0]):
                    continue
                zugaim = (couple + couple1)
                handsOptions.append(zugaim)

        triplets= createTriplets(num,theDeck.suits())

        #full House
        for couple in pairs:
            for trip in triplets:
                #no need to add this
                if (couple[0][0] == trip[0][0]):
                    continue
                t = (couple + trip)
                handsOptions.append(t)

        handsOptions.extend(pairs)
        handsOptions.extend(triplets)
        createFoursom(num,theDeck.suits())

    # createFlush(theDeck)
    createStright(theDeck)



def createDouble(cardOptions):
    pairs = []
    c1 = list(cardOptions)
    for card in cardOptions:
        c1.remove(card);
        for card2 in c1:
            if card[0]==card2[0]:
                if card[1] !=card2[1]:
                    pairs.append((card,card2))

    return pairs


def createTriplets(num,suites):
    triplets= []
    triplets.append(((num,suites[0]),(num,suites[1]),(num,suites[2])))
    triplets.append(((num,suites[0]),(num,suites[1]),(num,suites[3])))
    triplets.append(((num,suites[0]),(num,suites[2]),(num,suites[3])))
    triplets.append(((num,suites[1]),(num,suites[2]),(num,suites[3])))
    return triplets

def createFoursom(num,suites):
    handsOptions.append(((num,suites[0]),(num,suites[1]),(num,suites[2]),(num,suites[3])))

def createFlush(theDeck):
    for suite in theDeck.suits():
        handsOptions.append(((10,suite),(11,suite),(12,suite),(13,suite),(14,suite)))

def createStright(theDeck):
    a=[]
    b=[]
    for suite in theDeck.suits():
        for suite1 in theDeck.suits():
            for suite2 in theDeck.suits():
                for suite3 in theDeck.suits():
                    for suite4 in theDeck.suits():
                            for num in xrange(2,11):
                                a.append(((num,suite),(num+1,suite1),(num+2,suite2),(num+3,suite3),(num+4,suite4)))
                                b.extend(a)
                                a=[]
        for num in xrange(2,11):
            b.remove(((num,suite),(num+1,suite),(num+2,suite),(num+3,suite),(num+4,suite)))

    handsOptions.extend(b)

def getHandsOptions():
    return handsOptions

def initHandsOptions():
    initOptions()

def printHandsOptions():
    for hand in handsOptions:
        print hand

def printHandsNum():
    print len(handsOptions)

initHandsOptions()

def standOff(cardsOnTable,handToCheck):
    for hand in handToCheck:
        flag = False
        type = hand[0]
        num = hand[1]
        for handOption in cardsOnTable:
            for card in handOption:
                if card[0] == type :
                    num = num-1
                    if num==0:
                        flag = True
        if (flag):
            continue
        else:
            return False
    return True

print handsOptions
cardsOnTable = (((12, 'Heart'), (12, 'Spade'), (5, 'Heart'), (5, 'Spade'), (5, 'Clover')),
                ((13, 'Heart'), (13, 'Spade'), (4, 'Heart'), (4, 'Spade'), (4, 'Clover')))

# print standOff(handsOptions,((2,4),(3,2)))
# print standOff(cardsOnTable,[(13,3)])
