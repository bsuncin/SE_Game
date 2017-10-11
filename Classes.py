class Class:
    def __init__(self, attack, speed, xp, lvl, damRes, health, mana):
        self.attack = attack
        self.speed = speed
        self.mana = mana
        self.health = health
        self.damres = damres
        self.xp = xp
        self.lvl = lvl
        
    def __show__(self):
        print("Attack =", self.attack)
        print("Speed =", self.speed)
        print("Mana =", self.mana)
        print("Health =", self.health)
        print("DamRes =", self.DamRes)
        print("XP =", self.XP)
        print("LVL =", self.lvl)
        
    def checkLVLUp(self):
        if self.xp == 0:
            return false
        elif self.xp % 800 == 0:
            return true
        
    def lvlUp(self):
        self.attack = int(self.attack * 1.2)
        self.speed = int(self.speed * 1.2) 
        self.mana = int(self.mana * 1.5)
        self.damres = int(self.damres * 1.2)
        self.health = int(self.health * 1.5)
    
    def giveXP(self, num):
        self.xp += num
        if checkLVLUp() == true:
            lvlUp()
            
            
            
class Mage(Class):
    def __init__(self):
        super().__init__(attack = 5, 
                         speed = 2,
                         xp = 0,
                         lvl = 1,
                         damRes = 1,
                         health = 10,
                         mana = 20)
        
class Fighter(Class):
    def __init__(self):
        super().__init__(attack = 10, 
                         speed = 7,
                         xp = 0,
                         lvl = 1,
                         damRes = 5,
                         health = 20,
                         mana = 5)  
        
        
class Tank(Class):
    def __init__(self):
        super().__init__(attack = 10, 
                         speed = 2,
                         xp = 0,
                         lvl = 1,
                         damRes = 10,
                         health = 20,
                         mana = 0) 
        
      
class Duelist(Class):
    def __init__(self):
        super().__init__(attack = 5, 
                         speed = 10,
                         xp = 0,
                         lvl = 1,
                         damRes = 3,
                         health = 5,
                         mana = 10)    
