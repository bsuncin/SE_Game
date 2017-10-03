import Inventory as I

# The shop class will contain the processes to run shops in game.
# It will serve to act as an exchange for players and the shop NPC.

class Shop:

# init(inven) will set the shop inventory to the array inven.
# the format of inven should be like below:
# [ 'item', 'item', 'item', ........]

    def __init__(self, inven):
        self.pInventory = None
        self.inventory = I.Inventory()

        for x in inven:
            self.inventory.addItem(x, 1)

# setPlayerIn(pIn) will set pInventory to the inventory pIn.
# pIn will be the player inventory the module recieves.

    def setPlayerIn(self, pIn):
        self.pInventory = pIn

# exchangePToS(pSell) will sell item pSell from pInventory.
# return 0 if successful and -1 if not.

    def exchangePToS(self, pSell, amount):
        if 0 == self.pInventory.removeItem(pSell, amount):
            value = self.inventory.getItem(pSell).value * amount
            self.pInventory.addGold(value)
            return 0
        return -1
        
        
# exchangeSToP(pSell) will buy item pSell from Inventory.
# return 0 if successful and -1 if not.

    def exchangeSToP(self, pSell, amount):
        value = self.inventory.getItem(pSell).value * 3
        if 0 == self.pInventory.removeGold(value):
            if 0 == self.pInventory.addItem(pSell, amount):
                return 0
        return -1



# test inventories
def testPlayerInven():
    inven = I.Inventory()
    inven.addItem('Fang', 20)
    inven.addItem('Ring of Health', 3)
    inven.addItem('Mana Potion', 20)
    inven.addGold(1000)
    return inven

def testShop():
    shop = {'Fang', 'Ring of Health', 'Mana Potion',
            'Skelly Eye', 'Leather'}
    return shop
