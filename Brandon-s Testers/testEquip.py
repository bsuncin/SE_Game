import Inventory as In
import Equip_Menu as E
import Player as P

#inven = In.Inventory()
player = P.Player()
player.inventory.addItem('Platemail', 1)
player.inventory.addItem('Leather', 1)
player.inventory.addItem('Tattered Robes', 1)
player.inventory.addItem('Chainmail', 1)
player.inventory.addItem('Sword', 1)
player.inventory.addItem('Dagger', 1)
player.inventory.addItem('Club', 1)
player.inventory.addItem('Broken Stick', 1)
player.inventory.addItem('Ring of Health', 1)
player.inventory.addItem('Ring of Mana', 1)
eq = E.Equipment(player)
pinven = eq.Equip()
print(pinven)
print(player.inventory.getInventory())
