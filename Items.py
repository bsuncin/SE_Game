# Definitions

class Item:
    def __init__(self, name, value, desc):
        self.name = name
        self.value = value
        self.desc = desc

class Weapon(Item):
    def __init__(self, name, value, desc, damage, dtype, style, hands, buff, debuff):
        self.damage = damage
        self.dtype = dtype
        self.style = style
        self.hands = hands
        self.buff = buff
        self.debuff = debuff
        super().__init__(name, value, desc)

    def __show__(self):
        print("Name =", self.name)
        print("Value =", self.value)
        print("Description =", self.desc)
        print("Damage =", self.damage)
        print("Damage Type=", self.dtype)
        print("Damage Style=", self.style)
        print("# Hands =", self.hands)
        print("Buffs =", self.buff)
        print("Debuffs=", self.debuff)

class Armor(Item):
    def __init__(self, name, value, desc, defence, wieght, dtype, stype, buff, debuff):
        self.defence = defence
        self.wieght = wieght
        self.dtype = dtype
        self.stype = stype
        self.buff = buff
        self.debuff = debuff
        super().__init__(name, value, desc)

    def __show__(self):
        print("Name =", self.name)
        print("Value =", self.value)
        print("Description =", self.desc)
        print("Wieght =", self.wieght)
        print("Damage Type =", self.dtype)
        print("Damage Style =", self.stype)
        print("buff =", self.buff)
        print("debuff =", self.debuff)
        
class Ring(Item):
    def __init__(self, name, value, desc, defence, hp, mana, buff, debuff):
        self.defence = defence
        self.hp = hp
        self.mana = mana
        self.buff = buff
        self.debuff = debuff
        super().__init__(name, value, desc)

    def __show__(self):
        print("Name =", self.name)
        print("Value =", self.value)
        print("Description =", self.desc)

class Potion(Item):
    def __init__(self, name, value, desc, hp, mana, buff, debuff):
        self.hp = hp
        self.mana = mana
        self.buff = buff
        self.debuff = debuff
        super().__init__(name, value, desc)

    def __show__(self):
        print("Name =", self.name)
        print("Value =", self.value)
        print("Description =", self.desc)


# Weapon items ###########################################################################

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         value=200,
                         desc="A basic sword.",
                         damage=10,
                         dtype="physical",
                         style="slash",
                         hands=1,
                         buff="none",
                         debuff="none")
        
class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         value=200,
                         desc="A smol sword.",
                         damage=5,
                         dtype="physical",
                         style="pierce",
                         hands=1,
                         buff="none",
                         debuff="none")
        
class Club(Weapon):
    def __init__(self):
        super().__init__(name="Club",
                         value=200,
                         desc="A big ol stick.",
                         damage=15,
                         dtype="physical",
                         style="blunt",
                         hands=1,
                         buff="none",
                         debuff="none")        
   
#Armor Items##############################################################################

class Platemail(Armor):
    def __init__(self):
        super().__init__(name="Platemail",
                         value=800,
                         desc="Heavy armor made of steel.",
                         defence=15,
                         weight="heavy",
                         dtype="physical",
                         stype=["slash","pierce"],
                         buff="none",
                         debuff="slow")

class Leather(Armor):
    def __init__(self):
        super().__init__(name="Leather",
                         value=800,
                         desc="Fashionable clothes crafted from leather... also protecc",
                         defence=5,
                         weight="light",
                         dtype="physical",
                         stype=["none"],
                         buff="none",
                         debuff="slow")
        
class Chainmail(Armor):
    def __init__(self):
        super().__init__(name="Chainmail",
                         value=800,
                         desc="lots of chainlinks put together to keep u safe :^)",
                         defence=10,
                         weight="light",
                         dtype="physical",
                         stype=["slash"],
                         buff="none",
                         debuff="slow")        

#Ring Items#####################################################################

class RingOfHealth(Ring):
    def __init__(self):
        super().__init__(name="Ring of Health",
                       value=500,
                       desc="Increases max health by 50 points",
                       defence=0,
                       hp=50,
                       mana=0,
                       buff="none",
                       debuff="none")
        
class RingOfMana(Ring):
    def __init__(self):
        super().__init__(name="Ring of Mana",
                       value=500,
                       desc="Increases max Mana by 50 points",
                       defence=0,
                       hp=0,
                       mana=50,
                       buff="none",
                       debuff="none") 
        
# Potion Items############################################################################

class HealthPotion(Potion):
    def __init__(self):
        super().__init__(name="HP Potion",
                         value=200,
                         desc="A potion that will recover 50 health.",
                         hp=50,
                         mana=0,
                         buff="none",
                         debuff="none")
        
class ManaPotion(Potion):
    def __init__(self):
        super().__init__(name="Mana Potion",
                         value=200,
                         desc="A potion that will recover 50 mana.",
                         hp=0,
                         mana=50,
                         buff="none",
                         debuff="none")    
        
class GreaterHealthPotion(Potion):
    def __init__(self):
        super().__init__(name="Greater HP Potion",
                         value=200,
                         desc="A potion that will recover 150 health.",
                         hp=150,
                         mana=0,
                         buff="none",
                         debuff="none")
        
class GreaterManaPotion(Potion):
    def __init__(self):
        super().__init__(name="Greater Mana Potion",
                         value=200,
                         desc="A potion that will recover 150 mana.",
                         hp=0,
                         mana=150,
                         buff="none",
                         debuff="none")          

        
        
#Misc Items####################################################################################        

class Fang(Item):
    def __init__(self):
        super().__init__(name="Fang",
                         value=15,
                         desc="A fang from the jaws of a beast.")
        
class SkellyEye(Item):
    def __init__(self):
        super().__init__(name="Skelly Eye",
                         value=2000,
                         desc="How did you even aquire this?")   
        
        
        
 ###Item interface#################################################################################

items = {'fang' : Fang(),
        'skellyEye' : SkellyEye(),
         'hpPotion' : HealthPotion(),
         'manaPotion' : ManaPotion(),
         'greaterHealthPotion' : GreaterHealthPotion(),
         
        }
