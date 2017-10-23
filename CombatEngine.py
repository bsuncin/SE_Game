import Enemies as E
import random
import queue

class Combat:
    def __init__(self, player, enemy):
    
    # Returns how much damage a single weapon owned by the player will 
    # do to an enemy 
    def calcWeaponDam(Pweapon, enemy):
        if Pweapon.dtype == "magic"
            return int(player.wiz + (Pweapon.damage * (enemy.mres / 100)))
        elif Pweapon.dtype == "physical" and Pweapon.hands == 1
            return int((player.strength / 2) + (Pweapon.damage * (enemy.armor / 100)))
        elif Pweapon.dtype == "physical" and Pweapon.hands == 2
            return int(player.strength + (Pweapon.damage * (enemy.armor / 100)))
    
    # Returns the total damage the player will do to and enemy
    def calcPlayerDamage(player, enemy):
        if player.firsthand[0] == True and player.secondhand[0] == True
            hand1 = calcWeaponDam(player.firsthand[1], enemy)
            hand2 = calcWeaponDam(player.secondhand[1], enemy)
            return (hand1 + hand2)
        elif player.firsthand[0] == True
            return calcWeaponDam(player.firsthand[1], enemy)
        else return int(player.strength / 4)
    
    # Returns how much damage an enemy will do to the player
    def calcEnemyDamage(player, enemy):
        return (enemy.damage * (player.armor/100))
   
    # Defines what will happen when player hp = 0 during combat
    def loseCase(player)
        player.gold = int(player.gold * .9)
        invn = player.inventory.getInventory()
        item = random.randomchoice(invn)
        player.inventory.removeitem(item[0], 1)
        player.inventory.removeitem(item[0], 1)

    # Defines what will happen when enemy hp = 0 during combat 
    def winCase(player, enemy)
        player.addgold(player, enemy.gold)
        player.xp += enemy.xp
        player.classes[player.cla].addxp(enemy.xp)
        item = random.randomchoice(enemy.drops)
        player.inventory.additem(player, item[0], item[1])
   
