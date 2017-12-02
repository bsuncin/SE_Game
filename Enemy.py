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
                    
          def isAlive(self):
                    return self.hp > 0
          
          def setHp(self, num):
                    self.hp += num
                    
class Skeleton(Enemy):
          def __init__(self):
                    super().__init__(name ="Skeleton",
                                    gold = 50,
                                    desc = "Watch out for the skelly that drinks a lot of milk",
                                    hp = 100,
                                    mana = 200,
                                    attack = 10,
                                    armor = 0,
                                    mres = 0,
                                    strength = 5,
                                    agl = 8,
                                    drops=[("Leather", 20, 1),("Dagger", 50, 1),
                                           ("Health Potion", 29, 1),("Skelly Eye", 1, 1)] 
                                    )
class ArmorSkeleton(Enemy):
          def __init__(self):
                    super().__init__(name ="Armor Skeleton",
                                    gold = 10,
                                    desc = "Spooky armored Skeleton, major doot doot",
                                    hp = 2000,
                                    mana = 1000,
                                    attack = 75,
                                    armor = 25,
                                    mres = 25,
                                    strength = 30,
                                    agl = 20,
                                    drops=[("Leather", 10, 1),("Dagger", 25, 1),
                                           ("Health Potion", 14, 1),("Skelly Eye", 1, 1)]
                                    )
class Zombie(Enemy):
          def __init__(self):
                    super().__init__(name ="Zombie",
                                    gold = 75,
                                    desc = "Undead Humans that crave brains, youre safe though",
                                    hp = 150,
                                    mana = 200,
                                    attack = 15,
                                    armor = 5,
                                    mres = 5,
                                    strength = 6,
                                    agl = 4,
                                    drops=[("Leather", 1, 1), ("Health Potion", 2, 1),
                                           ("Mana Potion", 2, 1)]
                                    )

class GiantSpider(Enemy):
          def __init__(self):
                    super().__init__(name ="Giant Spider",
                                    gold = 25,
                                    desc = "Dah hell you think it is -_- ",
                                    hp = 300,
                                    mana = 500,
                                    attack = 30,
                                    armor = 15,
                                    mres = 10,
                                    strength = 10,
                                    agl = 10,
                                    drops=[("Club", 2, 1), ("Health Potion", 6, 1),("Fang", 4, 2),
                                           ("Mana Potion", 6, 1), ("Ring of Health", 1, 1)]
                                    )    
class VampireAcolyte(Enemy):
          def __init__(self):
                    super().__init__(name ="Vampire Acolyte",
                                    gold = 25,
                                    desc = "Humans that reaaaally wanna be a true vampy",
                                    hp = 200,
                                    mana = 500,
                                    attack = 25,
                                    armor = 10,
                                    mres = 20,
                                    strength = 10,
                                    agl = 8,
                                    drops=[("Sword", 4, 1), ("Health Potion", 10, 1),
                                           ("Mana Potion", 10, 1), ("Ring of Mana", 1, 1)]
                                    )
class BlueHairedVampire(Enemy):
          def __init__(self):
                    super().__init__(name ="Blue Haired Vampire",
                                    gold = 150,
                                    desc = "The scariest darkest spookiest vampire out there",
                                    hp = 1000,
                                    mana = 2000,
                                    attack = 60,
                                    armor = 20,
                                    mres = 20,
                                    strength = 20,
                                    agl = 15,
                                    drops=[("Sword", 4, 1), ("Health Potion", 10, 3),
                                           ("Mana Potion", 6, 3), ("Ring of Health", 1, 1),
                                           ("Fang", 10, 2)]
                                    ) 
class LordPepe(Enemy):
          def __init__(self):
                    super().__init__(name ="Lord Pepe",
                                    gold = 200,
                                    desc = "Lord of all who are antisocial, Slayer of normies and defender of Weebs",
                                    hp = 800,
                                    mana = 1000,
                                    attack = 65,
                                    armor = 20,
                                    mres = 20,
                                    strength = 20,
                                    agl = 15,
                                    drops=[("Sword", 4, 1), ("Health Potion", 10, 3),
                                           ("Mana Potion", 6, 3), ("Ring of Health", 2, 1),
                                           ("Platemail", 6, 1)]
                                    ) 
                    
class KingOrcha(Enemy):
          def __init__(self):
                    super().__init__(name ="King Orcha",
                                    gold = 400,
                                    desc = "If a Orc and an Orca had a child dis be it ",
                                    hp = 2000,
                                    mana = 1000,
                                    attack = 75,
                                    armor = 25,
                                    mres = 25,
                                    strength = 30,
                                    agl = 20,
                                    drops=[("Ring of Health", 5, 1),("sword",3,1),("Platemail",2,1),
                                           ("Health Potion",5,3),("Mana Potion", 5, 3)] 
                                    )
class OrchaMinion(Enemy):
          def __init__(self):
                    super().__init__(name ="Orcha Minion",
                                    gold = 3,
                                    desc = "Penguins, theyre penguins.... ",
                                    hp = 10,
                                    mana = 100,
                                    attack = 2,
                                    armor = 0,
                                    mres = 0,
                                    strength = 2,
                                    agl = 20,
                                    drops=[("Fang", 5, 2),("Health Potion", 3, 1),("Mana Potion", 2, 1)] 
                                    )                    
class FlemSpitter(Enemy):
          def __init__(self):
                    super().__init__(name ="Flem Spitter",
                                    gold = 40,
                                    desc = "Spits some nasty gook on ya",
                                    hp = 150,
                                    mana = 300,
                                    attack = 30,
                                    armor = 5,
                                    mres = 0,
                                    strength = 5,
                                    agl = 20,
                                    drops=[("Fang", 5, 2),("Health Potion", 3, 1),("Mana Potion", 2, 1),
                                          ("Chainmail", 4, 1),("Leather", 5, 1), ("Ring of Health", 1, 1)] 
                                    )                       
class Velociraptor(Enemy):
          def __init__(self):
                    super().__init__(name ="Velociraptor",
                                    gold = 40,
                                    desc = "is clever girl",
                                    hp = 300,
                                    mana = 500,
                                    attack = 30,
                                    armor = 15,
                                    mres = 10,
                                    strength = 15,
                                    agl = 20,
                                    drops=[("Fang", 5, 2),("Health Potion", 3, 1),("Mana Potion", 2, 1),
                                          ("Chainmail", 4, 1),("Leather", 5, 1), ("Ring of Health", 1, 1)] 
                                    )
                                           
class TheCage(Enemy):
          def __init__(self):
                    super().__init__(name ="Nickolas 'The Cage' Cage",
                                    gold = 100,
                                    desc = "THE CAGE NEEDS NO INTRODUCTION",
                                    hp = 500,
                                    mana = 1000,
                                    attack = 30,
                                    armor = 30,
                                    mres = 15,
                                    strength = 20,
                                    agl = 30,
                                    drops=[("Fang", 5, 2),("Health Potion", 3, 1),("Mana Potion", 2, 1),
                                          ("Chainmail", 4, 1),("Leather", 5, 1), ("Ring of Health", 1, 1)] 
                                    )                                           
                                           
class Dragon(Enemy):
          def __init__(self):
                    super().__init__(name ="Dragon",
                                    gold = 600,
                                    desc = "a bigger clever girl",
                                    hp = 1500,
                                    mana = 2000,
                                    attack = 80,
                                    armor = 40,
                                    mres = 20,
                                    strength = 25,
                                    agl = 20,
                                    drops=[("Greater Health Potion", 3, 3),("Greater Mana Potion", 2, 3),
                                          ("Platemail", 4, 1), ("Ring of Health", 1, 1)] 
                                    )                                           
                                           
class EvilWhiteRabbit(Enemy):
          def __init__(self):
                    super().__init__(name ="Evil White Rabbit",
                                    gold = 40,
                                    desc = "RUN AWAY RUN AWAY",
                                    hp = 200,
                                    mana = 500,
                                    attack = 30,
                                    armor = 5,
                                    mres = 5,
                                    strength = 15,
                                    agl = 50,
                                    drops=[("Fang", 5, 2),("Health Potion", 3, 1),("Mana Potion", 2, 1),
                                          ("Chainmail", 4, 1),("Leather", 5, 1), ("Ring of Health", 1, 1)] 
                                    )                                           
                                           
class ExGirlfriend(Enemy):
          def __init__(self):
                    super().__init__(name ="Ex-Girlfriend",
                                    gold = 1000,
                                    desc = "ya dead son",
                                    hp = 4000,
                                    mana = 5000,
                                    attack = 50,
                                    armor = 10,
                                    mres = 10,
                                    strength = 15,
                                    agl = 15,
                                    drops=[("Fang", 5, 2),("Health Potion", 3, 1),("Mana Potion", 2, 1),
                                          ("Chainmail", 4, 1),("Leather", 5, 1), ("Ring of Health", 1, 1)] 
                                    )                                           
class Wolf(Enemy):
          def __init__(self):
                    super().__init__(name ="Wolf",
                                    gold = 20,
                                    desc = "big ol bork bork",
                                    hp = 200,
                                    mana = 500,
                                    attack = 20,
                                    armor = 5,
                                    mres = 5,
                                    strength = 10,
                                    agl = 15,
                                    drops= [("Fang", 4, 2),("Health Potion",3 , 1),("Mana Potion", 3,1)]
                                    ) 

class AlphaWolf(Enemy):
           def __init__(self):
                    super().__init__(name ="Alpha Wolf",
                                    gold = 50,
                                    desc = "The biggest ol bork bork",
                                    hp = 400,
                                    mana = 1000,
                                    attack = 35,
                                    armor = 10,
                                    mres = 10,
                                    strength = 20,
                                    agl = 20,
                                    drops= [("Fang", 4, 2),("Health Potion",3 , 1),("Mana Potion", 3,1)]
                                    ) 
                                            
class HouseCat(Enemy):
          def __init__(self):
                    super().__init__(name ="House Cat",
                                    gold = 15,
                                    desc = "Dont go for the belly, ITS A TRAP!!",
                                    hp = 150,
                                    mana = 200,
                                    attack = 15,
                                    armor = 5,
                                    mres = 5,
                                    strength = 5,
                                    agl = 20,
                                    drops = [("Health Potion", 1, 1),("Mana Potion", 1 ,1)]
                                    )

class Bat(Enemy):
          def __init__(self):
                    super().__init__(name ="Bat",
                                    gold = 50,
                                    desc = "maybe youll become the batman",
                                    hp = 100,
                                    mana = 200,
                                    attack = 10,
                                    armor = 5,
                                    mres = 5,
                                    strength = 10,
                                    agl = 20,
                                    drops = [("Health Potion", 1 , 1),("Mana Potion", 1 ,1)]
                                    )
class LandDolphin(Enemy):
          def __init__(self):
                    super().__init__(name ="Land Dolphin",
                                    gold = 150,
                                    desc = "dat hell....dat dolphins on land",
                                    hp = 300,
                                    mana = 500,
                                    attack = 25,
                                    armor = 10,
                                    mres = 10,
                                    strength = 15,
                                    agl = 5,
                                    drops = [("Health Potion", 1, 1),("Mana Potion", 1 ,1)]
                                    ) 
   
class Llamas(Enemy):
          def __init__(self):
                    super().__init__(name ="Llama",
                                    gold = 100,
                                    desc = "CCCCAAAAARARRRRRLLLLLLLLLLLLL",
                                    hp = 250,
                                    mana = 500,
                                    attack = 20,
                                    armor = 10,
                                    mres = 10,
                                    strength = 15,
                                    agl = 10,
                                    drops = [("Health Potion", 1 , 1),("Mana Potion", 1 ,1)]
                                    ) 

class SludgeMonster(Enemy):
          def __init__(self):
                    super().__init__(name ="Sludge Monster",
                                    gold = 300,
                                    desc = "A big ball of slimmy trash that throws parts of itself at you",
                                    hp = 400,
                                    mana = 500,
                                    attack = 35,
                                    armor = 15,
                                    mres = 20,
                                    strength = 20,
                                    agl = 5,
                                    drops = [("Health Potion", 1 , 1),("Mana Potion", 1 ,1)]
                                    ) 
                    
class LazerShark(Enemy):
          def __init__(self):
                    super().__init__(name ="Lazer Shark",
                                    gold = 300,
                                    desc = "A shark WIF LAZERS BROOOOO",
                                    hp = 400,
                                    mana = 500,
                                    attack = 35,
                                    armor = 15,
                                    mres = 20,
                                    strength = 20,
                                    agl = 5,
                                    drops = [("Health Potion", 1 , 1),("Mana Potion", 1 ,1)]
                                    ) 
    
class Gerdzilla(Enemy):
          def __init__(self):
                    super().__init__(name ="Gerdzilla",
                                    gold = 500,
                                    desc = "rawr xD",
                                    hp = 700,
                                    mana = 1000,
                                    attack = 45,
                                    armor = 20,
                                    mres = 20,
                                    strength = 30,
                                    agl = 10,
                                    drops = [("Health Potion", 1 , 1),("Mana Potion", 1 ,1)]
                                    ) 
                    
                                            
enemies = { 'Skeleton'          : Skeleton(),               
          'Armored Skeleton'    : ArmorSkeleton(),       
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
          'Ex-Girlfriend'       : ExGirlfriend(),
          'Wolf'                : Wolf(),
          'Alpha Wolf'          : AlphaWolf(),
          'House Cat'           : HouseCat(),
          'Bat'                 : Bat(),
          'Land Dolphin'        : LandDolphin(),
          'Sludge Monster'      : SludgeMonster(),
          'Lazer Shark'         : LazerShark(),
          'Gerdzilla'           : Gerdzilla(),
          'TheCage'             : TheCage()
        }

enemyGroups = { 'Skellies' :            ['Skeleton', 'Skeleton', 'Skeleton'],
               'Hard Skellies' :        ['Armored Skeleton', 'Skeleton', 'Skeleton'],
               'Boss 1' :               ['Lord Pepe'],
               'Vamp Bitches' :         ['Blue Haired Vampire', 'Vampire Acolyte', 'Vampire Acolyte'],
               'Wolf Pack' :            ['Wolf', 'Wolf', 'Wolf'],
               'Aplha Pack' :           ['Alpha Wolf', 'Wolf', 'Wolf'],
               'Full Alpha' :           ['Alpha Wolf', 'Alpha Wolf', 'Alpha Wolf'],
               'De Bats' :              ['Bat', 'Bat', 'Bat'],
               'Undead Group' :         ['Skeleton', 'Zombie', 'Zombie'],
               'Spider Group' :         ['Giant Spider','Giant Spider','Giant Spider'],
               'Cage Match' :           ['Velociraptor', 'The Cage', 'Velociraptor'],
               'Boss 2' :               ['Dragon'],
               'Cute Group' :           ['House Cat', 'Evil White Rabbit', 'House Cat'],
               'Aqua Group' :           ['Lazer Shark', 'Land Dolphin', 'Land Dolphin'],
               'Garbage Group' :        ['Sludge Monster','Sludge Monster','Sludge Monster'],
               'Dino Group' :           ['Gerdzilla', 'Velociraptor', 'Velociraptor'],
               'Orcha Squad' :          ['King Orcha', 'Orcha Minion', 'Orcha Minion', 'Orcha Minion', 'Orcha Minion'],
               'Boss 3' :               ['Ex-Girlfriend']
               }
                                           
                                           
                                           
