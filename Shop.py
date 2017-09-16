import Item as I
import Inventory as In

class Shop:

    def __init__(self, pinventory, pgold):
        self.playerInventory = pinventory
        self.pgold = pgold
        self.inventory = {}

    def addItem(self, item, amount):
        if item in self.items:
            self.items[item][0] += amount
        else:
            self.items[item] = (amount, I.Items(item).value)

    def removeItem(self, item, amount):
        if item in self.items and self.items[item] > 0:
            if amount <= self.items[item]:
                self.items[item] -= amount
                return true
            else:
                print("Sorry I don't have that many", item + "s")
                return false
        else:
            print("Sorry I don't have a", item)

    def getValue(self, item):
        return self.items[item][1]

    def getPlayerInventory(self, inventory):
        

    

    
        
        
