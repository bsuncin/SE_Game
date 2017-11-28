import Inventory as In
import Equip_Menu as E
import Player as P

inven = In.Inventory()
player = P.Player()
inven.addItem('Platemail', 1)
inven.addItem('Leather', 1)
inven.addItem('Tattered Robes', 1)
inven.addItem('Chainmail', 1)
inven.addItem('Sword', 1)
inven.addItem('Dagger', 1)
inven.addItem('Club', 1)
inven.addItem('Broken Stick', 1)
inven.addItem('Ring of Health', 1)
inven.addItem('Ring of Mana', 1)
eq = E.Equipment(inven,player)
pinven = eq.Equip()
print(pinven)
