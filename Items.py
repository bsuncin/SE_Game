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

#Armor Items##############################################################################

class Platemail(Armor):
    def __init__(self):
        super().__init__(name="Platemail",
                         value=800,
                         desc="Heavy armor made of steel.",
                         defence=15,
                         wieght="heavy",
                         dtype="physical",
                         stype="blunt",
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
