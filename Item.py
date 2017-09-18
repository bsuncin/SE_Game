import Items as I

# Item defines what an item is and how other mudules
# will interact with items.

class Item:
    
# The init function will take an item name and
# define the items attributes from the Items file.
# Assumes that the item exists in the database Items.

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
        self.AddHealth = I.items[n][8]
        self.AddMana = I.items[n][9]

# getName() will return the name of the item.

    def getName(self):
        return self.name

# getValue() will return the gold value of the item.

    def getValue(self):
        return self.value

# getPAtt() will return the physical attack value.

    def getPAtt(self):
        return self.patt
        
# getPDef() will return the physical defence of the item.        
        
    def getPDef(self):
        return self.pdef

# getMAtt() will return the magic attack of the item.    
    
    def getMAtt(self):
        return self.matt
    
# getMDef() will return the magic defence value of the item.    

    def getMDef(self):
        return self.mdef
    
# getType() will return the type of the item.    

    def getType(self):
        return self.type
    
# getHeal() will return how much the item will heal the user.    

    def getHeal(self):
        return self.heal
    
# getMana() will return the amount of mana the item returns to the user.    

    def getMana(self):
        return self.mana
    
# getAddHealth() will return the amount of health the item adds to the user.

    def getAddHealth(self):
        return self.AddHealth
    
# getAddMana() will return the amount of mana an item will add to the user.

    def getAddMana(self):
        return self.AddMana

