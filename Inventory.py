import Items as I

# Inventory will act as a way to store information in a structured way to
# keep the users item data. The values it tracks are the amount of gold,
# tokens, tickets, and what items the user has.

class Inventory:

    def __init__(self):
        self.gold = 0
        self.tickets = 0
        self.tokens = 0
        self.inventory = {}
        
        for x in I.items:
            self.inventory[x] = [I.items[x], 0]
    
# addGold(num) will add num to the amount of gold the user has.    

    def addGold(self, num):
        self.gold += num
        
# removeGold(num) will remove amount num from the gold the user has.
# If the user has enough gold returns 0, else returns -1.

    def removeGold(self, num):
        if num <= self.gold:
            self.gold -= num
            return 0
        return -1
    
# addTokens(num) will add num to the amount of tokens the user has.    

    def addTokens(self, num):
        self.tokens += num        
        
# removeTokens(num) will remove amount num from the tokens the user has.
# If the user has enough tokens returns 0, else returns -1.

    def removeTokens(self, num):
        if num <= self.tokens:
            self.tokens -= num
            return 0
        return -1
    
# addTickets(num) will add num to the amount of tickets the user has.    

    def addTickets(self, num):
        self.tickets += num    
        
# removeTickets(num) will remove amount num from the tickets the user has.
# If the user has enough tickets returns 0, else returns -1.

    def removeTickets(self, num):
        if num <= self.tickets:
            self.tickets -= num            
            return 0
        return -1
    
# addItem(item, num) will add an amount num of item item from the items data 
# if it exists. If an error occurs returns -1, else returns 0.            

    def addItem(self, item, num):
        if item in self.inventory:
            self.inventory[item][1] += num
            return 0
        return -1
            
# removeItem(item, num) will remove the amount num of item item from the 
# inventory if the item is in the inventory.  If an error occurs 
# returns -1, else returns 0.           

    def removeItem(self, item, num):
        if item in self.inventory:
            if num <= self.inventory[item][1]:
                self.inventory[item][1] -= num
                return 0
            return -1
        return -1            
                
# checkAmount(item) will return item item's amount in the inventory.
# Returns -1 if an error is encountered.
    
    def checkAmount(self, item):
        if item in self.inventory:
            return self.inventory[item][1]
        return -1;
    
# getItem(item) will return the item item from the inventory.
# Returns -1 if it encounters an error.

    def getItem(self, item):
        if item in self.inventory:
            return self.inventory[item][0]
        return -1
    
# getInventory() will return an array of the current inventory only 
# including items with an amount above 0.

    def getInventory(self):
        return [(x, self.inventory[x][1]) for x in self.inventory if self.inventory[x][1] >= 1]
