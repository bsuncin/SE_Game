enemy = { //have yet to add drops for enemies.
          "Skeleton":            (100, 5, 10, 0, 0, 5, 2, 8, ),
          "Armored Skeleton":    (100, 10, 15, 10, 5, 5, 2, 4, ),
          "Zombie":              (150, 15, 15, 5, 5, 6, 3, 4, ),
          "Giant Spider":        (300, 25, 30, 15, 10, 10, 5, 8, ), 
          "Vampire Acolyte":     (200, 25, 25, 10, 20, 10, 8, 8, ),
          "Blue Haired Vampire": (1000, 150, 60, 20, 20, 20, 15, 15, ),
          "Lord Dio(BOSS)":      (800, 180, 65, 20, 20, 20, 15, 15, ),
          "King Orca(BOSS)":     (2000, 400, 75, 25, 25, 30, 20, 20, ),
          "Orca Minion":         (10, 3, 2, 0, 0, 2, 2, 20, ),
          "Flem Spitter":        (150, 25, 30, 5, 0, 5, 10, 20, ),
          "Velociraptor":        (300, 35, 30, 15, 10, 15, 10, 20, ),
          "Nickolas 'The Cage' Cage":(200, 15, 15, 10, 0, 10, 10, 10, ),
          "Dragon(BOSS)":        (1500, 600, 80, 40, 20, 25, 30, 20, ),
          "Evil White Rabbit":   (150, 20, 15, 5, 5, 15, 10, 50, ),
          "Ex-Girlfriend":       (4000, 1000, 50, 10, 10, 15, 10, 15, ),
          }

class Enemy:
          def __init__(self, name, gold, desc, hp, mana, armor, attack, mres, strength, agl, drops):
                    self.name = name
                    self.gold = gold
                    
                    
class Orcha(Enemy):
          def __init__(self):
                    super().__init__(name="Orcha",
                                    )
