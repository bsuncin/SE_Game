import Inventory as I
import Skills as S
import Classes as C

# Class stores all information about the player character.
# tracks the player state and relevant values for progression

class Player:

    def __init__ (self):
        self.health = 200
        self.maxHealth = 200
        self.mana = 100
        self.maxMana = 100
        self.strength = 20
        self.damres = 0
        self.agility = 20
        self.armor = [False, None]
        self.firstfinger  = [False, None]
        self.secondfinger = [False, None]
        self.firsthand = [False, None]
        self.secondhand = [False, None]
        self.skills = S.skills
        self.cla = None
        self.xp = 0
        self.level = 1
        self.inventory = I.Inventory()
        self.classes = {"Mage" : C.Mage(),
                       "Fighter" : C.Fighter(),
                       "Tank" : C.Tank(),
                       "Duelist" : C.Duelist()}
    def __show__(self):
        print("Health", self.health)
        print("Mana", self.mana)
        print("Strength", self.strength)
        print("Damres", self.damres)
        print("Agility", self.agility)
        print("Armor", self.armor)
        print("Firstfinger", self.firstfinger)
        print("Secondfinger", self.secondfinger)
        print("Firsthand", self.firsthand)
        print("Secondhand", self.secondhand)
        print("Skills", self.skills)
        print("Class", self.cla)
        print("xp", self.xp)
        print("level", self.level)
        
    def isAlive(self):
        return self.health > 0
    
    def setClass(self, ctype):
        self.cla = ctype

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
            self.armor = [True, item]
            self.inventory.removeItem(item, 1)

    def removeArmor(self, item):
            self.armor = [False, None]
            self.inventory.addItem(item, 1)

    def equipRighthand(self, item):
            self.righthand = [True, item]
            self.inventory.removeItem(item, 1)

    def removeRighthand(self, item):
            self.righthand = [False, None]
            self.inventory.addItem(item, 1)

    def equipLefthand(self,item):
            self.lefthand = [True, item]
            self.inventory.removeItem(item, 1)

    def removeLefthand(self, item):
            self.lefthand = [False, None]
            self.inventory.addItem(item, 1)
            
    def equipFirstfinger(self, item):
           self.firstfinger = [True, item]
           self.inventory.removeItem(item, 1)

    def removeFirstfinger(self, item):
           self.firstfinger = [False, None]
           self.inventory.addItem(item, 1)

    def equipSecondfinger(self, item):
           self.secondfinger = [True, item]
           self.inventory.removeItem(item, 1)

    def removeSecondfinger(self, item):
           self.secondfinger = [False, None]
           self.inventory.addItem(item, 1)

# addXp() will add amount num to the xp of the user.

    def addXp(self, num):
        self.xp += num

# getLevel() will convert xp points accrued to a level ranking.

    def checkLevelUp(self):
        if self.xp == 0:
            return false
        else:
            if self.level % 800 == 0:
                self.level += 1
                return true
            
