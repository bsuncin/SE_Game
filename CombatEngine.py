import Enemies as E
import random
import queue

class Combat:
    def __init__(self, player, enemy):
        
    def calcWeaponDam(Pweapon, enemy):
        if Pweapon.dtype == "magic"
            return int(player.wiz + (Pweapon.damage * (enemy.mres / 100)))
        elif Pweapon.dtype == "physical" and Pweapon.hands == 1
            return int((player.strength / 2) + (Pweapon.damage * (enemy.armor / 100)))
        elif Pweapon.dtype == "physical" and Pweapon.hands == 2
            return int(player.strength + (Pweapon.damage * (enemy.armor / 100)))
        
    def calcPlayerDamage(player, enemy):
        if player.firsthand[0] == True and player.secondhand[0] == True
            hand1 = calcWeaponDam(player.firsthand[1], enemy)
            hand2 = calcWeaponDam(player.secondhand[1], enemy)
            return (hand1 + hand2)
        elif player.firsthand[0] == True
            return calcWeaponDam(player.firsthand[1], enemy)
        else return int(player.strength / 4)

    def calcEnemyDamage(player, enemy):
        return (enemy.damage * (player.armor/100))
   
    def loseCase(player)
        player.gold = int(player.gold * .9)
        invn = player.inventory.getInventory()
        item = random.randomchoice(invn)
        player.inventory.removeitem(item[0], 1)
        player.inventory.removeitem(item[0], 1)

    def winCase(player, enemy)
        player.addgold(player, enemy.gold)
        player.xp += enemy.xp
        player.classes[player.cla].addxp(enemy.xp)
        item = random.randomchoice(enemy.drops)
        player.inventory.additem(player, item[0], item[1])
   
