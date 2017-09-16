import Items as I

class Item:
    def __init__(self, n):
        self.name = n
        self.value = I.items[n][0]
        self.patt = I.items[n][1]
        self.pdef = I.items[n][2]
        self.matt = I.items[n][3]
        self.mdef = I.items[n][4]
        self.type = I.items[n][5]
        self.heal = I.items[n][6]
        self.mana = I.items[n][7]

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getPAtt(self):
        return self.patt
        
    def getPDef(self):
        return self.pdef
    
    def getMAtt(self):
        return self.matt

    def getMDef(self):
        return self.mdef

    def getType(self):
        return self.type

    def getHeal(self):
        return self.heal

    def getMana(self):
        return self.mana

