class Enemy:
          def __init__(self, name, gold, desc, hp, mana, armor, attack, mres, strength, agl, drops):
                    self.name     = name
                    self.gold     = gold
                    self.decs     = desc
                    self.hp       = hp
                    self.mana     = mana
                    self.armor    = armor
                    self.attack   = attack
                    self.mres     = mres
                    self.strength = strength
                    self.agl      = agl
                    self.drops    = drops
                    
class Skeleton(Enemy):
          def __init__(self):
                    super().__init__(name ="Skeleton",
                                    gold = 5,
                                    decs = "An undead Skeleton, doot doot",
                                    hp = 100,
                                    mana = 200,
                                    attack = 10,
                                    armor = 0,
                                    mres = 0,
                                    strength = 5,
                                    agl = 8,
                                    drops=[("Leather", 20, 1),("dagger", 50, 1),
                                           ("healthpotion", 29, 1),("skellyeye", 1, 1)] 
                                    )
class ArmorSkeleton(Enemy):
          def __init__(self):
                    super().__init__(name ="Armor Skeleton",
                                    gold = 10,
                                    decs = "Spooky armored Skeleton, major doot doot",
                                    hp = 2000,
                                    mana = 1000,
                                    attack = 75,
                                    armor = 25,
                                    mres = 25,
                                    strength = 30,
                                    agl = 20,
                                    drops=[("Leather", 10, 1),("dagger", 25, 1),
                                           ("healthpotion", 14, 1),("skellyeye", 1, 1)]
                                    )
class Zombie(Enemy):
          def __init__(self):
                    super().__init__(name ="Zombie",
                                    gold = 15,
                                    decs = "Undead Hooman",
                                    hp = 150,
                                    mana = 200,
                                    attack = 15,
                                    armor = 5,
                                    mres = 5,
                                    strength = 6,
                                    agl = 4,
                                    drops=[("Leather", 1, 1), ("healthpotion", 2, 1),
                                           ("manapotion", 2, 1)]
                                    )

class GiantSpider(Enemy):
          def __init__(self):
                    super().__init__(name ="Giant Spider",
                                    gold = 25,
                                    decs = "Dah hell you think it is -_- ",
                                    hp = 300,
                                    mana = 500,
                                    attack = 30,
                                    armor = 15,
                                    mres = 10,
                                    strength = 10,
                                    agl = 10,
                                    drops=[("Club", 2, 1), ("healthpotion", 6, 1),("fang", 4, 2),
                                           ("manapotion", 6, 1), ("RingOfHealth", 1, 1)]
                                    )    
class VampireAcolyte(Enemy):
          def __init__(self):
                    super().__init__(name ="Vampire Acolyte",
                                    gold = 25,
                                    decs = "Humans that reaaaally wanna be a true vampy",
                                    hp = 200,
                                    mana = 500,
                                    attack = 25,
                                    armor = 10,
                                    mres = 20,
                                    strength = 10,
                                    agl = 8,
                                    drops=[("Sword", 4, 1), ("healthpotion", 10, 1),
                                           ("manapotion", 10, 1), ("RingOfMana", 1, 1)]
                                    )
class BlueHairedVampire(Enemy):
          def __init__(self):
                    super().__init__(name ="Blue Haired Vampire",
                                    gold = 150,
                                    decs = "The scariest darkest spookiest vampire out there",
                                    hp = 1000,
                                    mana = 2000,
                                    attack = 60,
                                    armor = 20,
                                    mres = 20,
                                    strength = 20,
                                    agl = 15,
                                    drops=[("Sword", 4, 1), ("healthpotion", 10, 3),
                                           ("manapotion", 6, 3), ("RingOfHealth", 1, 1),
                                           ("fang", 10, 2)]
                                    ) 
class LordPepe(Enemy):
          def __init__(self):
                    super().__init__(name ="Lord Pepe",
                                    gold = 200,
                                    decs = "Lord of all who are antisocial, Slayer of normies and defender of Weebs",
                                    hp = 800,
                                    mana = 1000,
                                    attack = 65,
                                    armor = 20,
                                    mres = 20,
                                    strength = 20,
                                    agl = 15,
                                    drops=[("Sword", 4, 1), ("healthpotion", 10, 3),
                                           ("manapotion", 6, 3), ("RingOfHealth", 2, 1),
                                           ("platemail", 6, 1)]
                                    ) 
                    
class KingOrcha(Enemy):
          def __init__(self):
                    super().__init__(name ="King Orcha",
                                    gold = 400,
                                    decs = "",
                                    hp = 2000,
                                    mana = 1000,
                                    attack = 75,
                                    armor = 25,
                                    mres = 25,
                                    strength = 30,
                                    agl = 20,
                                    drops=[("ringOfHealth", 5, 1),("sword",3,1),("platemail",2,1),
                                           ("healthPotion",5,3),("manaPotion", 5, 3)] 
                                    )
class OrchaMinion(Enemy):
          def __init__(self):
                    super().__init__(name ="Orcha Minion",
                                    gold = 3,
                                    decs = "Penguins, theyre penguins.... ",
                                    hp = 10,
                                    mana = 100,
                                    attack = 2,
                                    armor = 0,
                                    mres = 0,
                                    strength = 2,
                                    agl = 20,
                                    drops=[("fang", 5, 2),("healthPotion", 3, 1),("manaPotion", 2, 1)] 
                                    )                    
class FlemSpitter(Enemy):
          def __init__(self):
                    super().__init__(name ="Flem Spitter",
                                    gold = 40,
                                    decs = "Spits some nasty gook on ya",
                                    hp = 150,
                                    mana = 300,
                                    attack = 30,
                                    armor = 5,
                                    mres = 0,
                                    strength = 5,
                                    agl = 20,
                                    drops=[("fang", 5, 2),("healthPotion", 3, 1),("manaPotion", 2, 1)
                                          ("Chainmail", 4, 1),("Leather", 5, 1), ("ringOfHealth, 1, 1)] 
                                    )                       
class Velociraptor(Enemy):
          def __init__(self):
                    super().__init__(name ="Velociraptor",
                                    gold = 40,
                                    decs = "is a clever girl",
                                    hp = 300,
                                    mana = 500,
                                    attack = 30,
                                    armor = 15,
                                    mres = 10,
                                    strength = 15,
                                    agl = 20,
                                    drops=[("fang", 5, 2),("healthPotion", 3, 1),("manaPotion", 2, 1)
                                          ("Chainmail", 4, 1),("Leather", 5, 1), ("ringOfHealth, 1, 1)] 
                                    )
                                           
class TheCage(Enemy):
          def __init__(self):
                    super().__init__(name ="Nickolas 'The Cage' Cage",
                                    gold = 100,
                                    decs = "is a clever girl",
                                    hp = 500,
                                    mana = 1000,
                                    attack = 30,
                                    armor = 30,
                                    mres = 15,
                                    strength = 20,
                                    agl = 30,
                                    drops=[("fang", 5, 2),("healthPotion", 3, 1),("manaPotion", 2, 1)
                                          ("Chainmail", 4, 1),("Leather", 5, 1), ("ringOfHealth, 1, 1)] 
                                    )                                           
                                           
class Dragon(Enemy):
          def __init__(self):
                    super().__init__(name ="Dragon",
                                    gold = 600,
                                    decs = "a bigger clever girl",
                                    hp = 1500,
                                    mana = 2000,
                                    attack = 80,
                                    armor = 40,
                                    mres = 20,
                                    strength = 25,
                                    agl = 20,
                                    drops=[("GreaterHealthPotion", 3, 3),("GreaterManaPotion", 2, 3)
                                          ("platemail", 4, 1), ("ringOfHealth, 1, 1)] 
                                    )                                           
                                           
class EvilWhiteRabbit(Enemy):
          def __init__(self):
                    super().__init__(name ="Evil White Rabbit",
                                    gold = 40,
                                    decs = "RUN AWAY RUN AWAY",
                                    hp = 200,
                                    mana = 500,
                                    attack = 30,
                                    armor = 5,
                                    mres = 5,
                                    strength = 15,
                                    agl = 50,
                                    drops=[("fang", 5, 2),("healthPotion", 3, 1),("manaPotion", 2, 1)
                                          ("Chainmail", 4, 1),("Leather", 5, 1), ("ringOfHealth, 1, 1)] 
                                    )                                           
                                           
class ExGirlfriend(Enemy):
          def __init__(self):
                    super().__init__(name ="Ex-Girlfriend",
                                    gold = 1000,
                                    decs = "ya dead son",
                                    hp = 4000,
                                    mana = 5000,
                                    attack = 50,
                                    armor = 10,
                                    mres = 10,
                                    strength = 15,
                                    agl = 15,
                                    drops=[("fang", 5, 2),("healthPotion", 3, 1),("manaPotion", 2, 1)
                                          ("Chainmail", 4, 1),("Leather", 5, 1), ("ringOfHealth, 1, 1)] 
                                    )                                           
                                           
                                           
enemy = { 'Skeleton'            : Skeleton(),               
          'Armored Skeleton'    : ArmoredSkeleton(),       
          'Zombie'              : Zombie(),                   
          'Giant Spider'        : GiantSpider(),             
          'Vampire Acolyte'     : VampireAcolyte(),          
          'Blue Haired Vampire' : BlueHairedVampire(),
          'Lord Pepe'           : LordPepe(),               
          'King Orcha'          : KingOrcha(),               
          'Orcha Minion'        : OrchaMinion(),              
          'Flem Spitter'        : FlemSpitter(),             
          'Velociraptor'        : Velociraptor(),            
          'The Cage'            : TheCage(), 
          'Dragon'              : Dragon(),                   
          'Evil White Rabbit'   : EvilWhiteRabbit(),       
          'Ex-Girlfriend'       : ExGirlfriend()
        }
                                           
                                           
                                           
                                           
