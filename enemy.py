enemy = { 
          "Skeleton":                    (100, 5, 10, 0, 0, 5, 2, 8, ),
          "Armored Skeleton":            (100, 10, 15, 10, 5, 5, 2, 4, ),
          "Zombie":                      (150, 15, 15, 5, 5, 6, 3, 4, ),
          "Giant Spider":                (300, 25, 30, 15, 10, 10, 5, 8, ), 
          "Vampire Acolyte":             (200, 25, 25, 10, 20, 10, 8, 8, ),
          "Blue Haired Vampire":         (1000, 150, 60, 20, 20, 20, 15, 15, ),
          "Lord Dio":                    (800, 180, 65, 20, 20, 20, 15, 15, ),
          "King Orcha":                  (2000, 400, 75, 25, 25, 30, 20, 20, ),
          "Orcha Minion":                (10, 3, 2, 0, 0, 2, 2, 20, ),
          "Flem Spitter":                (150, 25, 30, 5, 0, 5, 10, 20, ),
          "Velociraptor":                (300, 35, 30, 15, 10, 15, 10, 20, ),
          "Nickolas 'The Cage' Cage":    (200, 15, 15, 10, 0, 10, 10, 10, ),
          "Dragon":                      (1500, 600, 80, 40, 20, 25, 30, 20, ),
          "Evil White Rabbit":           (150, 20, 15, 5, 5, 15, 10, 50, ),
          "Ex-Girlfriend":               (4000, 1000, 50, 10, 10, 15, 10, 15, ),
          }

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
                                    drops=[(Leather, 20, 1),(dagger, 50, 1),
                                           (healthpotion, 29, 1),(skullyeye, 1, 1)] 
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
                                    drops=[(Leather, 10, 1),(dagger, 25, 1),
                                           (healthpotion, 14, 1),(skullyeye, 1, 1)]
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
                                    drops=[(Leather, 1, 1), (healthpotion, 2, 1),
                                           (manapotion, 2, 1)]
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
                                    drops=[(Club, 2, 1), (healthpotion, 6, 1),(fang, 4, 2),
                                           (manapotion, 6, 1), (RingOfHealth, 1, 1)]
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
                                    drops=[(Sword, 4, 1), (healthpotion, 10, 1),
                                           (manapotion, 10, 1), (RingOfMana, 1, 1)]
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
                                    drops=[(Sword, 4, 1), (healthpotion, 10, 3),
                                           (manapotion, 6, 3), (RingOfHealth, 1, 1),
                                           (fang, 10, 2)]
                                    ) 
                    
class KingOrcha(Enemy):
          def __init__(self):
                    super().__init__(name ="King Orcha",
                                    gold = 400,
                                    decs = "The Mightiest of all the Orchas",
                                    hp = 2000,
                                    mana = 1000,
                                    attack = 75,
                                    armor = 25,
                                    mres = 25,
                                    strength = 30,
                                    agl = 20,
                                    drops=[(fang, 5),(skully eye, 1)] 
                                    )
