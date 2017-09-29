#import Inventory as I

# Class stores all information about the player character.
# tracks the player state and relevant values for progression

class Player:

    def __init__ (self):
        self.health = 100
        self.mana = 100
        self.strength = 20
        self.damres = 0
        self.agility = 20
        self.healthcapacity = 100
        self.armor = (False, null)
        self.firstfinger  = (False, null)
        self.secondfinger = (False, null)
        self.firsthand = (False, null)
        self.secondhand = (False, null)
        self.skills = {}
        self.xp = 0
        self.level = 1
        
        self.inventory = None # I.Inventory()


    #max health

    def addHealthCap(self, num):
        self.healthcapacity += num

    def removeHealthCap(self, num):
        self.healthcapacity -= num

# addHealth() will add num to the health of the user.
    
    def addHealth(self, num):
        if num <= self.health and num <= self.healthcapacity:
            self.health += num
            
# removeHealth() will remove amount num from the health of the user.
            
    def removeHealth(self, num):
        if num <= self.mana and num <= self.healthcapacity:
            self.mana -= num

# addMana() will add num to the mana of the user.

    def addMana(self, num):
        self.mana += num

# removeMana() will remove amount num from the mana of the user.

    def removeMana(self, num):
        if num <= self.mana:
            self.mana -= num

# addStrength() will add num to the strength of the user.

    def addStrength(self, num):
        self.strength += num

# removeStrength() will remove num from the strength of the user.

    def removeStrength(self, num):
        if num <= self.strength:
            self.strength -= num

# addAgility() will add num to the agility of the user.

    def addAgility(self, num):
        self.agility += num

# removeAgility() will remove num from the agility of the user.

    def removeAgility(self, num):
        if num <= self.agility:
            self.agility -= num
            
# equip() will equip either armor, ring, or weapon on the user.

#drudgery

    def equipArmor(self, item):
            self.armor = (True, item)

    def removeArmor(self, item):
            self.armor = (False, null)

    def equipRighthand(self, item):
            self.righthand = (True, item)

    def removeRighthand(self, item):
            self.righthand = (False, null)

    def equipLefthand(self,item):
            self.lefthand = (True, item)

    def removeLefthand(self, item):
            self.lefthand = (False, null)
            
    def equipFirstfinger(self, item):
           self.firstfinger = (True, item)

    def removeFirstfinger(self, item):
           self.firstfinger = (False, null)

    def equipSecondfinger(self, item):
           self.secondfinger = (True, item)

    def removeSecondfinger(self, item):
           self.secondfinger = (False, null) 

# addXp() will add amount num to the xp of the user.

    def addXp(self, num):
        self.xp += num

# getLevel() will convert xp points accrued to a level ranking.

    def getLevel(self):
        xpState = self.xp
        levelState = self.level
        if   xpState <= 25:
             levelState = 1
        elif xpState <= 50:
             levelState = 2
        # addAgility(x)
        elif xpState <= 75:
             levelState = 3
        elif xpState <= 100:
             levelState = 4
        elif xpState <= 125:
             levelState = 5
        elif xpState <= 150:
             levelState = 6
        elif xpState <= 175:
             levelState = 7
        elif xpState <= 200:
             levelState = 8
        elif xpState <=225:
             levelState = 9
        elif xpState <=250:
             levelState = 10
        return self.level 
        
    

