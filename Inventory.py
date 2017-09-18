import Item as I

# Inventory will act as a way to store information in a structured way to
# keep the users item data. The values it tracks are the amount of gold,
# tokens, tickets, and what items the user has.

class Inventory:

    def __init__(self):
        self.gold = 0
        self.tickets = 0
        self.tokens = 0
        self.inventory = {}
        
# getGold() will return the gold amount the user has.        

    def getGold(self):
        return self.gold
    
# addGold(num) will add num to the amount of gold the user has.    

    def addGold(self, num):
        self.gold += num
        
# removeGold(num) will remove amount num from the gold the user has.        

    def removeGold(self, num):
        if num <= self.gold:
            self.gold -= num
            
# getTokens() will return the token amount the user has.        

    def getTokens(self):
        return self.tokens    
    
# addTokens(num) will add num to the amount of tokens the user has.    

    def addTokens(self, num):
        self.tokens += num    
        
# removeTokens(num) will remove amount num from the tokens the user has.        

    def removeTokens(self, num):
        if num <= self.tokens:
            self.tokens -= num
            
            
# getTickets() will return the ticket amount the user has.        

    def getTickets(self):
        return self.tickets   
    
# addTickets(num) will add num to the amount of tickets the user has.    

    def addTickets(self, num):
        self.tickets += num    
        
# removeTickets(num) will remove amount num from the tickets the user has.        

    def removeTickets(self, num):
        if num <= self.tickets:
            self.tickets -= num            
            
# addItem(item, num) will add an amount num of item item from the items data 
# if it exists.            

    def addItem(self, item, num):
        if item in self.inventory:
            self.inventory[item][1] += num
        else:
            self.inventory[item] = (I.Item(item), num)
            
# removeItem(item, num) will remove the amount num of item item from the 
# inventory if the item is in the inventory.            

    def removeItem(self, item, num):
        if item in self.inventory:
            if self.inventory[item][1] > num:
                self.inventory[item][1] -= num
            elif self.inventory[item][1] == num:
                del self.inventory[item]
                
 # checkAmount(item) will return item item's amount in the inventory.
    
    def checkAmount(self, item):
        if item in self.inventory:
            return self.inventory[item][1]
        return 0;
