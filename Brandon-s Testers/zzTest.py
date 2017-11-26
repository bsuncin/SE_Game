import Inventory as In
import ShopNPCGreg as NPC

inven = In.Inventory()
inven.addItem('Fang', 20)
inven.addGold(3000)
shop = NPC.Shop(inven, 0)
pinven = shop.shop_intro()
print(pinven.getInventory())
print(pinven.gold)
