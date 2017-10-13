# Definitions
class foodmachinebroke:        
    def __init_(self, name, value, desc, hcost, mcost, damage, dtype, aoe, buff, debuff, level, exp):
        self.name = name
        self.value = value
        self.desc = desc
        self.hcost = hcost
        self.mcost = mcost
        self.damage = damage
        self.dtype = dtype
        self.aoe = aoe
        self.buff = buff
        self.debuff = debuff
        self.level = level
        self.exp = exp

    def __show__(self):
        print("Name =", self.name)
        print("Value =", self.value)
        print("Description =", self.desc)
        print("HealthCost =", self.hcost)
        print("ManaCost =", self.mcost)
        print("Damage =", self.damage)
        print("Damage Type =", self.dtype)
        print("Area of Effect? =", self.aoe)
        print("Buffs =", self.buff)
        print("Debuffs =", self.debuff)
        print("Level =", self.level)
        print("Experience =", self.exp)

# Attack Skills ##########################################################

class Fire(foodmachinebroke):
    def __init__(self):
        #spells above a certain level will gain aoe when labled maybe
        super().__init__(name="Fire",
                         value=0,
                         desc="fire bad.",
                         hcost=0,
                         mcost=5,
                         damage=10,
                         dtype="magical",
                         aoe = "maybe",
                         buff="none",
                         debuff="on fire",
                         level=1,
                         exp=0)
        
class Ice(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Ice",
                         value=0,
                         desc="a blast of cold capable of freezing foes.",
                         hcost=0,
                         mcost=5,
                         damage=10,
                         dtype="magical",
                         aoe="maybe",
                         buff="none",
                         debuff="frozen",
                         level=1,
                         exp=0)
        
class Thunder(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Thunder",
                         value=0,
                         desc="Truly shocking.",
                         hcost=0,
                         mcost=5,
                         damage=10,
                         dtype="magical",
                         aoe="maybe",
                         buff="none",
                         debuff="shock",
                         level=1,
                         exp=0)
        
class Inferno(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Inferno",
                         value=0,
                         desc="Enough flames to evaporate an lake.",
                         hcost=20,
                         mcost=50,
                         damage=100,
                         dtype="magical"
                         aoe="yes",
                         buff="none",
                         debuff="on fire",
                         level=1,
                         exp=0)
        
class Blizzard(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Blizzard",
                         value=0,
                         desc="an absolute cold capable of freezing the very air.",
                         hcost=20,
                         mcost=50,
                         damage=100,
                         dtype="magical",
                         aoe="yes",
                         buff="none",
                         debuff="frozen",
                         level=1,
                         exp=0)
        
class Tempest(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Tempest",
                         value=0,
                         desc="Is that the air cracking, or their bones?",
                         hcost=20,
                         mcost=50,
                         damage=100,
                         dtype="magical",
                         aoe="yes",
                         buff="none",
                         debuff="shock",
                         level=1,
                         exp=0)
        
class Explosion(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="EXPLOSION",
                         value=0,
                         desc="a blast of cold capable of freezing foes.",
                         hcost=currenthp-1,
                         mcost=0,
                         damage=currenthp-1,
                         dtype="magical",
                         aoe="maybe",
                         buff="none",
                         debuff="none",
                         level=1,
                         exp=0)
        
class Obliterate(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="OBLITERATE",
                         value=0,
                         desc="a blast of cold capable of freezing foes.",
                         hcost=0,
                         mcost=currentmana,
                         damage=currentmana,
                         dtype="magical",
                         aoe="maybe",
                         buff="none",
                         debuff="none",
                         level=1,
                         exp=0)
        
class HeavySwing(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Heavy Swing",
                         value=0,
                         desc="swing so hard you pull a muscle.",
                         hcost=5,
                         mcost=0,
                         damage=15,
                         dtype="physcial",
                         aoe="no",
                         buff="none",
                         debuff="none",
                         level=1,
                         exp=0)
       
        # No Health Cost if wearing a helmet/armor rating is above a certain amount
        
class Headbutt(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Headbutt",
                         value=0,
                         desc="Nobody wins in a headbutt.",
                         hcost=20,
                         mcost=0,
                         damage=20,
                         dtype="physcial",
                         aoe="no",
                         buff="none",
                         debuff="none",
                         level=1,
                         exp=0)
        
class Cleave(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Cleave",
                         value=0,
                         desc="A rather large swing, capable of hitting multiple foes.",
                         hcost=10,
                         mcost=0,
                         damage=10,
                         dtype="physcial",
                         aoe="yes",
                         buff="none",
                         debuff="none",
                         level=1,
                         exp=0)
        
class LasStrike(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Lascerating Strike",
                         value=0,
                         desc="A carefully placed stab to incite bleeding.",
                         hcost=10,
                         mcost=10,
                         damage=5,
                         dtype="physcial",
                         aoe="no",
                         buff="none",
                         debuff="bleeding",
                         level=1,
                         exp=0)
        
class LastGamble(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Last Gamble",
                         value=0,
                         desc="A fools attempt at a lost battle",
                         hcost=0,
                         mcost=20,
                         damage=20, #based on missing health
                         dtype="physcial",
                         aoe="no",
                         buff="none",
                         debuff="none",
                         level=1,
                         exp=0)
        
        
class Heal(foodmachinebroke):
    def __init__(self):
        super().__init__(name="Heal",
                         value=0,
                         desc="like a bandaid.",
                         hcost=0,
                         mcost=5,
                         damage=-20,
                         dtype="none",
                         aoe="no",
                         buff="none",
                         debuff="none",
                         level=1,
                         exp=0)
        
class GreatHeal(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Great Heal",
                         value=0,
                         desc="like a NEW bandaid.",
                         hcost=0,
                         mcost=20,
                         damage=-50,
                         dtype="none",
                         aoe="no",
                         buff="none",
                         debuff="none",
                         level=1,
                         exp=0)
        
class Concentration(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Concentration",
                         value=50,
                         desc="building mana is hard.",
                         hcost=5,
                         mcost=-20,
                         damage=0,
                         dtype="none",
                         aoe="no",
                         buff="none",
                         debuff="none",
                         level=1,
                         exp=0)
        
class Clarity(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Clarity",
                         value=0,
                         desc="building mana is easy.",
                         hcost=20,
                         mcost=-50,
                         damage=0,
                         dtype="none",
                         aoe="no",
                         buff="none",
                         debuff="none",
                         level=1,
                         exp=0)
        
class Rage(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Rage",
                         value=0,
                         desc="anger serves to increase your strength.",
                         hcost=0,
                         mcost=10,
                         damage=0,
                         dtype="none",
                         aoe="no",
                         buff="atk+",
                         debuff="none",
                         level=1,
                         exp=0)
        
class Fortify(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Fortify",
                         value=0,
                         desc="strengthens skin to bolster defense.",
                         hcost=0,
                         mcost=10,
                         damage=0,
                         dtype="none",
                         aoe="no",
                         buff="pdef+",
                         debuff="none",
                         level=1,
                         exp=0)
        
class Meditate(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Meditate",
                         value=0,
                         desc="builds mental barriers to increase magic resistance.",
                         hcost=0,
                         mcost=10,
                         damage=0,
                         dtype="none",
                         aoe="no",
                         buff="mdef+",
                         debuff="none",
                         level=1,
                         exp=0)
        
class Stretch(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Stretch",
                         value=0,
                         desc="limber up to increase agility.",
                         hcost=0,
                         mcost=10,
                         damage=0,
                         dtype="none",
                         aoe="no",
                         buff="agl+",
                         debuff="none",
                         level=1,
                         exp=0)
        
class FireWeapon(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Fire Weapon",
                         value=0,
                         desc="engulf your weapon in flames.",
                         hcost=0,
                         mcost=30,
                         damage=50,
                         dtype="magical",
                         aoe="no",
                         buff="none",
                         debuff="on fire",
                         level=1,
                         exp=0)
        
class IceWeapon(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Ice Weapon",
                         value=0,
                         desc="cool your blade with frost.",
                         hcost=0,
                         mcost=30,
                         damage=50,
                         dtype="magical",
                         aoe="no",
                         buff="none",
                         debuff="frozen",
                         level=1,
                         exp=0)
        
class ThunWeapon(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Thunder Weapon",
                         value=0,
                         desc="coat your weapon with lighting.",
                         hcost=0,
                         mcost=30,
                         damage=50,
                         dtype="magical",
                         aoe="no",
                         buff="none",
                         debuff="shock",
                         level=1,
                         exp=0)
        
class Examine(foodmachinebroke):
    def __init__(self):
        super().__init__(name="Examine",
                         value=0,
                         desc="shows an enemy's weakness.",
                         hcost=0,
                         mcost=0,
                         damage=0,
                         dtype="none",
                         aoe="no",
                         buff="none",
                         debuff="show weakness",
                         level=1,
                         exp=0)
        
class Cripple(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Cripple",
                         value=500,
                         desc="Lowers an enemy's attack.",
                         hcost=0,
                         mcost=20,
                         damage=0,
                         dtype="none",
                         aoe="maybe",
                         buff="none",
                         debuff="atk-",
                         level=1,
                         exp=0)
        
class Pierce(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Pierce",
                         value=0,
                         desc="Lowers an enemy's defense.",
                         hcost=0,
                         mcost=20,
                         damage=0,
                         dtype="none",
                         aoe="no",
                         buff="none",
                         debuff="pdef-",
                         level=1,
                         exp=0)
        
class MentProbe(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Mental Probe",
                         value=0,
                         desc="Lowers an enemy's magical resistance.",
                         hcost=0,
                         mcost=20,
                         damage=0,
                         dtype="none",
                         aoe="no",
                         buff="none",
                         debuff="mdef-",
                         level=1,
                         exp=0)
        
class Entangle(foodmachinebroke):
    def __init__(self):        
        super().__init__(name="Entangle",
                         value=0,
                         desc="Lowers an enemy's agility",
                         hcost=0,
                         mcost=20,
                         damage=0,
                         dtype="none",
                         aoe="no",
                         buff="none",
                         debuff="sgl-",
                         level=1,
                         exp=0)


        
