#import Player as P
#import Inventory as I

class State:
    def __init__(self):
        self.worldState = 1
        self.arcadeSate = 1
        self.dungeonState = 1
    
        self.worldS = {1 : "Start state",
                  2 : "Player beat mid dungeon",
                  3 : "PLayer beat dungeon"}

        self.arcadeS = {1 : "First game unlocked",
                   2 : "Second game unlocked",
                   3 : "Third game unlocked",
                   4 : "Fourth game unlocked"}

        self.dungeonS = {1 : "First floor entrance",
                    2 : "Fifth floor save",
                    3 : "Tenth floor save",
                    4 : "Fifteenth floor save",
                    5 : "Twentieth floor save",
                    6 : "Dungeon maze room save"}

        def increaseWorldS(self):
            self.worldState += 1
            
        def increaseArcadeS(self):
            self.arcadeSate += 1
    
