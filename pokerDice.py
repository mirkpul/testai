import random as r

#Utility functions
def checkPokerPlus(res):
    assert res
    assert len(res) == 6
    ret = []
    for singleRes in res:
        if res[singleRes] == 5 :
            ret.append(singleRes)
    return ret
    
def checkPoker(res):
    assert res
    assert len(res) == 6
    ret = []
    for singleRes in res:
        if res[singleRes] == 4 :
            ret.append(singleRes)
    return ret

def checkStraight(res):
    assert res
    assert len(res) == 6
    contDice = 0
    ret = []
    for singleRes in res:
        if res[singleRes] == 1 :
            contDice += 1
            ret.append(singleRes)
            if(contDice == 5): 
                return ret
        else:
            contDice = 0
            ret = []
    if(contDice == 5):
        return ret
    else:
        return []

def checkFull(res):
    assert res
    assert len(res) == 6
    ret = []
    retTris = checkTris(res)
    retPair = checkPair(res)
    if retTris and retPair:
        ret.append(retTris[0])
        ret.append(retPair[0])
        return ret
    else:
        return [] 

def checkTris(res):
    assert res
    assert len(res) == 6
    ret = []
    for singleRes in res:
        if res[singleRes] == 3 :
            ret.append(singleRes)
    return ret 

def checkTwoPairs(res):
    assert res
    assert len(res) == 6
    ret = []
    for singleRes in res:
        if res[singleRes] == 2 :
            ret.append(singleRes)
    if len(ret) == 2:
        return ret
    else:
        return []

def checkPair(res):
    assert res
    assert len(res) == 6
    ret = []
    for singleRes in res:
        if res[singleRes] == 2 :
            ret.append(singleRes)
    if len(ret) == 1:
        return ret
    else:
        return []

def checkBust(res):
    assert res
    assert len(res) == 6
    maxNum = 0
    for singleRes in res:
        if res[singleRes] == 1 and maxNum < singleRes:
            maxNum = singleRes
    ret = []
    ret.append(maxNum)
    return ret
        
"""
0 - Bust
1 - A pair
2 - Two Pairs
3 - Tris
4 - Straight
5 - Full
6 - Poker
7 - Poker Plus
"""
def calculateResult(dices):
    assert dices
    assert len(dices) == 5
    dices.sort(key=takeDiceStatus)
    
    ret = {"result":0,"detail":[]}
    res = {1:0,2:0,3:0,4:0,5:0,6:0}
    for dice in dices:
        res[dice._status] += 1
    #how to make them sortable?
    #self._dices.sort()
    #how to assign in an if statement?
    if checkPokerPlus(res):
        ret["result"] = 7
        ret["detail"] = checkPokerPlus(res)
        return ret
    elif checkPoker(res):
        ret["result"] = 6
        ret["detail"] = checkPoker(res)
        return ret
    elif checkFull(res):
        ret["result"] = 5
        ret["detail"] = checkFull(res)
        return ret
    elif checkStraight(res):
        ret["result"] = 4
        ret["detail"] = checkStraight(res)
        return ret
    elif checkTris(res):
        ret["result"] = 3
        ret["detail"] = checkTris(res)
        return ret
    elif checkTwoPairs(res):
        ret["result"] = 2
        ret["detail"] = checkTwoPairs(res)
        return ret
    elif checkPair(res):
        ret["result"] = 1
        ret["detail"] = checkPair(res)
        return ret
    else:
        ret["result"] = 0
        ret["detail"] = checkBust(res)
        return ret

def takeDiceStatus(dice):
    return dice._status

def isDiceRolled(dice):
    print(dice._status)
    if (dice._status != None and (dice._status >= 1 and dice._status<=dice._faces)):
        return True
    else:
        return False

class Dice():
    def __init__(self, faces):
        self._faces = faces
        self._status = None
        
    def setFaces(self,faces):
        self._faces = faces
    
    def printFaces(self):
        print(self._faces)
    
    def roll(self):
        self._status = r.randint(1, self._faces)
        
    @classmethod
    def getDice(cls,numFaces):
        return cls(numFaces)
        
class Hand():
    def __init__(self, diceNum, cls, numFaces):
        self._diceNum = diceNum
        self._cls = cls
        self._numFaces = numFaces
        self._dices = []
        i = 0
        while (i < diceNum):
            #da verificare!!!
            self._dices.append(Dice.getDice(numFaces))
            self._dices[i].roll()
            i += 1

class PokerDice(Dice):
    def __init__(self):
        super().__init__(6)

class PokerHand(Hand):
     
    def __init__(self):
        super().__init__(5,PokerDice,6)
        self._result = 0;
        self._result = calculateResult(self._dices)
        self._keepList = [];
    
    def getResult(self):
        if self._result["result"] == 7:
            print("A wonderful poker plus of {0}".format(self._result["detail"][0]))
        elif self._result["result"] == 6:
            print("A poker of {0}".format(self._result["detail"][0]))
        elif self._result["result"] == 5:
            print("A full made up of a tris of {0} and a pair of {1}".format(self._result["detail"][0],self._result["detail"][1]))
        elif self._result["result"] == 4:
            print("A straight with:")
            print(self._result["detail"])
        elif self._result["result"] == 3:
            print("A tris of {0}".format(self._result["detail"][0]))
        elif self._result["result"] == 2:
            print("Two pairs of {0} and {1}".format(self._result["detail"][0],self._result["detail"][1]))
        elif self._result["result"] == 1:
            print("A pair of {0}".format(self._result["detail"][0]))
        elif self._result["result"] == 0:
            print("Bust, Max number: {0}".format(self._result["detail"][0]))
    
    def keep(self,dice):
        if(not self._keepList.contains(dice)):
            self._keepList.append(dice)
            
    def rollAgain(self):
        for dice in self._dices:
            if not self._keepList.contains(dice):
                dice.roll();
        self._keepList = []

#try:
print("Hello World")
#Simple Dice creation
simpleDice = Dice(2)
assert simpleDice._faces == 2
simpleDice.setFaces(3)
assert simpleDice._faces == 3
simpleDice.printFaces()
simpleDice.roll()
assert isDiceRolled(simpleDice)
print("Dice rolled!")
print(simpleDice._status)

#Simple Hand Creation
simpleHand = Hand(3,Dice,3)
assert len(simpleHand._dices) == 3
for dice in simpleHand._dices:
    assert isDiceRolled(dice)

#Poker Dice creation
pokerDice = PokerDice()
assert pokerDice._status == None
assert pokerDice._faces == 6
pokerDice.roll();
assert isDiceRolled(pokerDice)
print("Poker Dice rolled!")
print(pokerDice._status)

#Simple Poker Hand Creation
pokerHand = PokerHand()
print("Poker Dice in Hand:")
assert len(pokerHand._dices) == 5
for dice in pokerHand._dices:
    assert isDiceRolled(dice)

#checkStraight
straight = {1:1,2:1,3:1,4:1,5:0,6:1}
assert not checkStraight(straight)
straight = {1:0,2:1,3:2,4:1,5:0,6:1}
assert not checkStraight(straight)
straight = {1:0,2:1,3:1,4:1,5:1,6:1}
assert checkStraight(straight)
straight = {1:1,2:1,3:1,4:1,5:1,6:0}
assert checkStraight(straight)
straight = {1:1,2:1,3:1,4:1,5:1,6:0}
assert checkStraight(straight)
    
print("You have in hand:")
print(pokerHand.getResult())

count = 1
while(pokerHand._result["result"] != 4):
    pokerHand = PokerHand()
    count += 1

print("After {0} trials you finally got a straight with:".format(count))
print(pokerHand.getResult())

#Let's keep the second and fourth dice of the straight
pokerHand.keep(pokerHand._dices[1])
pokerHand.keep(pokerHand._dices[3])
pokerHand.rollAgain()
print("Your new ewsukt is; {0}".format(pokerHand.getResult()))



#except:
#    print("Got exception during execution")
