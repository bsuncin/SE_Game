import Player as PL
import CombatEngine as CE


pl = PL.Player()
enemy = "Bat"

combat = CE.Combat(pl, enemy)
alive, pl = combat.combat_intro()
print("Alive = ", str(alive))
print(pl.inventory.getInventory())
print(pl.inventory.gold)
del combat


combat = CE.Combat(pl, enemy)
alive, pl = combat.combat_intro()
print("Alive = ", str(alive))
print(pl.inventory.getInventory())
print(pl.inventory.gold)
