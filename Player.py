import Inventory as I
import Skills as S
from math import log

# Class stores all information about the player character.
# tracks the player state and relevant values for progression

class Player:

    def __init__ (self):
        self.health = 100
        self.maxHealth
        self.mana = 100
        self.maxMana = 100
        self.strength = 20
        self.damres = 0
        self.agility = 20
        self.armor = (False, null)
        self.firstfinger  = (False, null)
        self.secondfinger = (False, null)
        self.firsthand = (False, null)
        self.secondhand = (False, null)
        self.skills = S.pSkills
        self.xp = 0
        self.level = 1
        self.inventory = I.Inventory()
        
    def isAlive(self):
        return self.health > 0

#max health

    def checkMaxHealth(self):
        if self.health > self.maxHealth:
            self.health = self.maxHealth

# addHealth() will add num to the health of the user.
    
    def addHealth(self, num):
        self.health += num
        checkMaxHealth()
            
# removeHealth() will remove amount num from the health of the user.
            
    def removeHealth(self, num):
        self.health -= num
        return isAlive()
    
    def checkMaxMana(self):
        if self.mana > self.maxMana:
            self.mana = self.maxMana

# addMana() will add num to the mana of the user.

    def addMana(self, num):
        self.mana += num
        checkMaxMana()

# removeMana() will remove amount num from the mana of the user.

    def removeMana(self, num):
        self.mana -= num

# addStrength() will add num to the strength of the user.

    def addStrength(self, num):
        self.strength += num

# addAgility() will add num to the agility of the user.

    def addAgility(self, num):
        self.agility += num
            
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

    def checkLevelUp(self):
        if self.xp == 0:
            return false
        else:
            if self.level < 
            
        
    

