import Item as I

class Inventory:

    def __init__(self):
        self.gold = 0
        self.inventory = {}

    def getGold(self):
        return self.gold

    def addGold(self, num):
        self.gold += num

    def removeGold(self, num):
        if num <= self.gold:
            self.gold -= num

    def addItem(self, item, num):
        if item in self.inventory:
            self.inventory[item][1] += num
        else:
            self.inventory[item] = (I.Item(item), num)

    def removeItem(self, item, num):
        if item in self.inventory:
            if self.inventory[item][1] > num:
                self.inventory[item][1] -= num
            elif self.inventory[item][1] == num:
                del self.inventory[item]
