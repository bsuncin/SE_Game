import pygame
import time
import random
import Items

pygame.init()


display_width = 1200
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
grey = (128,128,128)
 
block_color = (53,115,255)
 
quitgame = pygame.quit
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dungeons of Optional Doom')
clock = pygame.time.Clock()

shopImg = pygame.image.load('Greg.png')
shopImg = pygame.transform.scale(shopImg, (200, 200))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("times",20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def text(msg,x,y,w,h,ic):
    pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("times",20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('Shop.png', [0,0])

#-------------------------------------------------------------------------------




class Shop:
    def __init__(self, PInven, state):
        self.PInven = PInven
        self.state = state
        self.sMessages = ["Hey ya chump",
                          "Oh wow you entered the dungeon you little shite",
                          "Mid floor, aren't you a strong one you arsehole",
                          "So you comleted the dungeon I guess you aren't that worthless."]
        self.sMessage = self.sMessages[self.state]
        self.introDia = ["Welcome!!!!?",
                         "Fine weather ey?",
                         "How's it goin?",
                         "How's it hangin?",
                         "Buy something",
                         "Welcome to the Shop of Destiny!"]
        self.introDia.append(self.sMessage)
        self.buyDia = ["Buy something",
                       "Ya ready to go broke",
                       "Drugs?",
                       "Weed",
                       "Want some candy"]
        self.sellDia = ["Whatcha sellin?",
                        "You gonna sell or what?",
                        "Gimme drugs",
                        "Ya makin me broke"]
        self.purchases = []
        self.sales = []
        self.inventories = [['Fang', 'Ring of Health', 'Sword', 'Health Potion', 'Mana Potion', 'Skelly Eye', 'Leather'],
                            ['Fang', 'Ring of Health', 'Sword', 'Health Potion', 'Mana Potion', 'Skelly Eye', 'Leather', 'Ring of Mana', 'Chainmail'],
                            ['Fang', 'Ring of Health', 'Sword', 'Health Potion', 'Mana Potion', 'Skelly Eye', 'Leather', 'Ring of Mana', 'Chainmail', 'Greater Mana Potion', 'Greater Health Potion', 'Platemail', 'Dagger'],
                            ['Fang', 'Ring of Health', 'Sword', 'Health Potion', 'Mana Potion', 'Skelly Eye', 'Leather', 'Ring of Mana', 'Chainmail', 'Greater Mana Potion', 'Greater Health Potion', 'Platemail', 'Dagger']
                            ]
        self.currInven = self.inventories[self.state]
        self.currGold = self.PInven.gold
        self.Run = True
        self.shop = True
        self.buttons = {'Fang': 0, 'Ring of Health': 0, 'Ring of Mana': 0, 'Mana Potion': 0, 'Greater Mana Potion': 0, 'Health Potion': 0,
                        'Greater Health Potion': 0, 'Skelly Eye': 0, 'Leather': 0, 'Chainmail': 0, 'Platemail': 0, 'Dagger': 0, 'Sword': 0}
            

#Button Controllers-----------------------------------------------------------------------------------------------------------------

    def resetAll(self):
        for item in self.buttons.keys():
            self.buttons[item] = 0

    def decreaseFang(self):
        self.buttons['Fang'] -= 1

    def increaseFang(self):
        self.buttons['Fang'] += 1

    def buyFang(self):
        self.PInven.addItem('Fang', self.buttons['Fang'])
        self.PInven.gold -= (self.buttons['Fang'] * self.PInven.getPrice('Fang'))
        self.resetAll()

    def sellFang(self):
        self.PInven.removeItem('Fang', self.buttons['Fang'])
        self.PInven.gold += (self.buttons['Fang'] * self.PInven.getPrice('Fang'))
        self.resetAll()
    
    def decreaseROH(self):
        self.buttons['Ring of Health'] -= 1

    def increaseROH(self):
        self.buttons['Ring of Health'] += 1

    def buyROH(self):
        self.PInven.addItem('Ring of Health', self.buttons['Ring of Health'])
        self.PInven.gold -= (self.buttons['Ring of Health'] * self.PInven.getPrice('Ring of Health'))
        self.buttons['Ring of Health'] = 0
        self.resetAll()

    def sellROH(self):
        self.PInven.removeItem('Ring of Health', self.buttons['Ring of Health'])
        self.PInven.gold += (self.buttons['Ring of Health'] * self.PInven.getPrice('Ring of Health'))
        self.resetAll()

    def decreaseSword(self):
        self.buttons['Sword'] -= 1

    def increaseSword(self):
        self.buttons['Sword'] += 1

    def buySword(self):
        self.PInven.addItem('Sword', self.buttons['Sword'])
        self.PInven.gold -= (self.buttons['Sword'] * self.PInven.getPrice('Sword'))
        self.buttons['Sword'] = 0
        self.resetAll()

    def sellSword(self):
        self.PInven.removeItem('Sword', self.buttons['Sword'])
        self.PInven.gold += (self.buttons['Sword'] * self.PInven.getPrice('Sword'))
        self.resetAll()

    def decreaseHealthPotion(self):
        self.buttons['Health Potion'] -= 1

    def increaseHealthPotion(self):
        self.buttons['Health Potion'] += 1

    def buyHealthPotion(self):
        self.PInven.addItem('Health Potion', self.buttons['Health Potion'])
        self.PInven.gold -= (self.buttons['Health Potion'] * self.PInven.getPrice('Health Potion'))
        self.buttons['Health Potion'] = 0
        self.resetAll()

    def sellHealthPotion(self):
        self.PInven.removeItem('Health Potion', self.buttons['Health Potion'])
        self.PInven.gold += (self.buttons['Health Potion'] * self.PInven.getPrice('Health Potion'))
        self.resetAll()

    def decreaseManaPotion(self):
        self.buttons['Mana Potion'] -= 1

    def increaseManaPotion(self):
        self.buttons['Mana Potion'] += 1

    def buyManaPotion(self):
        self.PInven.addItem('Mana Potion', self.buttons['Mana Potion'])
        self.PInven.gold -= (self.buttons['Mana Potion'] * self.PInven.getPrice('Mana Potion'))
        self.buttons['Mana Potion'] = 0
        self.resetAll()

    def sellManaPotion(self):
        self.PInven.removeItem('Mana Potion', self.buttons['Mana Potion'])
        self.PInven.gold += (self.buttons['Mana Potion'] * self.PInven.getPrice('Mana Potion'))
        self.resetAll()
        
    def decreaseSkellyEye(self):
        self.buttons['Skelly Eye'] -= 1

    def increaseSkellyEye(self):
        self.buttons['Skelly Eye'] += 1

    def buySkellyEye(self):
        self.PInven.addItem('Skelly Eye', self.buttons['Skelly Eye'])
        self.PInven.gold -= (self.buttons['Skelly Eye'] * self.PInven.getPrice('Skelly Eye'))
        self.buttons['Skelly Eye'] = 0
        self.resetAll()

    def sellSkellyEye(self):
        self.PInven.removeItem('Skelly Eye', self.buttons['Skelly Eye'])
        self.PInven.gold += (self.buttons['Skelly Eye'] * self.PInven.getPrice('Skelly Eye'))
        self.resetAll()
        
    def decreaseLeather(self):
        self.buttons['Leather'] -= 1

    def increaseLeather(self):
        self.buttons['Leather'] += 1

    def buyLeather(self):
        self.PInven.addItem('Leather', self.buttons['Leather'])
        self.PInven.gold -= (self.buttons['Leather'] * self.PInven.getPrice('Leather'))
        self.buttons['Leather'] = 0
        self.resetAll()

    def sellLeather(self):
        self.PInven.removeItem('Leather', self.buttons['Leather'])
        self.PInven.gold += (self.buttons['Leather'] * self.PInven.getPrice('Leather'))
        self.resetAll()
        
    def decreaseChainmail(self):
        self.buttons['Chainmail'] -= 1

    def increaseChainmail(self):
        self.buttons['Chainmail'] += 1

    def buyChainmail(self):
        self.PInven.addItem('Chainmail', self.buttons['Chainmail'])
        self.PInven.gold -= (self.buttons['Chainmail'] * self.PInven.getPrice('Chainmail'))
        self.buttons['Chainmail'] = 0
        self.resetAll()

    def sellChainmail(self):
        self.PInven.removeItem('Chainmail', self.buttons['Chainmail'])
        self.PInven.gold += (self.buttons['Chainmail'] * self.PInven.getPrice('Chainmail'))
        self.resetAll()
        
    def decreaseManaRing(self):
        self.buttons['Ring of Mana'] -= 1

    def increaseManaRing(self):
        self.buttons['Ring of Mana'] += 1

    def buyManaRing(self):
        self.PInven.addItem('Ring of Mana', self.buttons['Ring of Mana'])
        self.PInven.gold -= (self.buttons['Ring of Mana'] * self.PInven.getPrice('Ring of Mana'))
        self.buttons['Ring of Mana'] = 0
        self.resetAll()

    def sellManaRing(self):
        self.PInven.removeItem('Ring of Mana', self.buttons['Ring of Mana'])
        self.PInven.gold += (self.buttons['Ring of Mana'] * self.PInven.getPrice('Ring of Mana'))
        self.resetAll()
        
    def decreaseGreaterManaPotion(self):
        self.buttons['Greater Mana Potion'] -= 1

    def increaseGreaterManaPotion(self):
        self.buttons['Greater Mana Potion'] += 1

    def buyGreaterManaPotion(self):
        self.PInven.addItem('Greater Mana Potion', self.buttons['Greater Mana Potion'])
        self.PInven.gold -= (self.buttons['Greater Mana Potion'] * self.PInven.getPrice('Greater Mana Potion'))
        self.buttons['Greater Mana Potion'] = 0
        self.resetAll()

    def sellGreaterManaPotion(self):
        self.PInven.removeItem('Greater Mana Potion', self.buttons['Greater Mana Potion'])
        self.PInven.gold += (self.buttons['Greater Mana Potion'] * self.PInven.getPrice('Greater Mana Potion'))
        self.resetAll()
        
    def decreasePlatemail(self):
        self.buttons['Platemail'] -= 1

    def increasePlatemail(self):
        self.buttons['Platemail'] += 1

    def buyPlatemail(self):
        self.PInven.addItem('Platemail', self.buttons['Platemail'])
        self.PInven.gold -= (self.buttons['Platemail'] * self.PInven.getPrice('Platemail'))
        self.buttons['Platemail'] = 0
        self.resetAll()

    def sellPlatemail(self):
        self.PInven.removeItem('Platemail', self.buttons['Platemail'])
        self.PInven.gold += (self.buttons['Platemail'] * self.PInven.getPrice('Platemail'))
        self.resetAll()
        
    def decreaseDagger(self):
        self.buttons['Dagger'] -= 1

    def increaseDagger(self):
        self.buttons['Dagger'] += 1

    def buyDagger(self):
        self.PInven.addItem('Dagger', self.buttons['Dagger'])
        self.PInven.gold -= (self.buttons['Dagger'] * self.PInven.getPrice('Dagger'))
        self.buttons['Dagger'] = 0
        self.resetAll()

    def sellDagger(self):
        self.PInven.removeItem('Dagger', self.buttons['Dagger'])
        self.PInven.gold += (self.buttons['Dagger'] * self.PInven.getPrice('Dagger'))
        self.resetAll()
        
    def decreaseGreaterHealthPotion(self):
        self.buttons['Greater Health Potion'] -= 1

    def increaseGreaterHealthPotion(self):
        self.buttons['Greater Health Potion'] += 1

    def buyGreaterHealthPotion(self):
        self.PInven.addItem('Greater Health Potion', self.buttons['Greater Health Potion'])
        self.PInven.gold -= (self.buttons['Greater Health Potion'] * self.PInven.getPrice('Greater Health Potion'))
        self.buttons['Greater Health Potion'] = 0
        self.resetAll()
    
    def sellGreaterHealthPotion(self):
        self.PInven.removeItem('Greater Health Potion', self.buttons['Greater Health Potion'])
        self.PInven.gold += (self.buttons['Greater Health Potion'] * self.PInven.getPrice('Greater Health Potion'))
        self.resetAll()






# Back Controllers-----------------------------------------------------------------------------------
    def back(self):
        self.shop = False

    def escape(self):
        self.Run = False

    def blackout(self):
        counter = 0
        
        while counter != 20:
            
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
            gameDisplay.fill(black)


            pygame.display.update()
            clock.tick(15)
            counter += 1

# Sell ---------------------------------------------------------------------------------------------

    def sell(self):
        dialog = random.choice(self.sellDia)
        while self.shop:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 100)
            medText = pygame.font.SysFont("times",30)
            TextSurf, TextRect = text_objects("Shop of Destiny", largeText, white)
            TextRect.center = ((display_width/2),(display_height/10))

            TextMess, TextLoc = text_objects(dialog, medText, white)
            TextLoc.center = ((display_width/2),(display_height/4))
            
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextMess, TextLoc)


            text("Fang",100,250,100,50,green)
            text(str(int(self.PInven.getPrice('Fang')/2))+ "G",200,250,100,50,white)
            
            if self.buttons['Fang'] == 0:
                text("<--",300,250,50,50,grey)
            else:
                button("<--",300,250,50,50,red,bright_red,self.decreaseFang)
            
            text(str(self.PInven.checkAmount('Fang') - self.buttons['Fang']),350,250,50,50,white)

            if self.PInven.checkAmount('Fang') == self.buttons['Fang']:
                text("-->",400,250,50,50,grey)
            else:
                button("-->",400,250,50,50,red, bright_red,self.increaseFang)
            
            text(str(int(self.PInven.getPrice('Fang') / 2) * self.buttons['Fang']) + "G",450,250,100,50,green)

            if self.buttons['Fang'] == 0:
                text("sell",550,250,50,50,grey)
            else:
                button("sell",550,250,50,50,red,bright_red,self.sellFang)



            text("H Ring",100,300,100,50,green)
            text(str(int(self.PInven.getPrice('Ring of Health')/2))+ "G",200,300,100,50,white)
            
            if self.buttons['Ring of Health'] == 0:
                text("<--",300,300,50,50,grey)
            else:
                button("<--",300,300,50,50,red,bright_red,self.decreaseROH)
            
            text(str(self.PInven.checkAmount('Ring of Health') - self.buttons['Ring of Health']),350,300,50,50,white)

            if self.PInven.checkAmount('Ring of Health') == self.buttons['Ring of Health']:
                text("-->",400,300,50,50,grey)
            else:
                button("-->",400,300,50,50,red, bright_red,self.increaseROH)
            
            text(str(int(self.PInven.getPrice('Ring of Health')/2) * self.buttons['Ring of Health']) + "G",450,300,100,50,green)

            if self.buttons['Ring of Health'] == 0:
                text("sell",550,300,50,50,grey)
            else:
                button("sell",550,300,50,50,red,bright_red,self.sellROH)



            text("Sword",100,550,100,50,green)
            text(str(int(self.PInven.getPrice('Sword')/2))+ "G",200,550,100,50,white)
            
            if self.buttons['Sword'] == 0:
                text("<--",300,550,50,50,grey)
            else:
                button("<--",300,550,50,50,red,bright_red,self.decreaseSword)
            
            text(str(self.PInven.checkAmount('Sword') - self.buttons['Sword']),350,550,50,50,white)

            if self.PInven.checkAmount('Sword') == self.buttons['Sword']:
                text("-->",400,550,50,50,grey)
            else:
                button("-->",400,550,50,50,red, bright_red,self.increaseSword)
            
            text(str(int(self.PInven.getPrice('Sword') / 2) * self.buttons['Sword']) + "G",450,550,100,50,green)

            if self.buttons['Sword'] == 0:
                text("sell",550,550,50,50,grey)
            else:
                button("sell",550,550,50,50,red,bright_red,self.sellSword)



            text("Health Pot",100,350,100,50,green)
            text(str(int(self.PInven.getPrice('Health Potion')/2))+ "G",200,350,100,50,white)
            
            if self.buttons['Health Potion'] == 0:
                text("<--",300,350,50,50,grey)
            else:
                button("<--",300,350,50,50,red,bright_red,self.decreaseHealthPotion)
            
            text(str(self.PInven.checkAmount('Health Potion') - self.buttons['Health Potion']),350,350,50,50,white)

            if self.PInven.checkAmount('Health Potion') == self.buttons['Health Potion']:
                text("-->",400,350,50,50,grey)
            else:
                button("-->",400,350,50,50,red, bright_red,self.increaseHealthPotion)
            
            text(str(int(self.PInven.getPrice('Health Potion')/2) * self.buttons['Health Potion']) + "G",450,350,100,50,green)

            if self.buttons['Health Potion'] == 0:
                text("sell",550,350,50,50,grey)
            else:
                button("sell",550,350,50,50,red,bright_red,self.sellHealthPotion)



            text("Mana Pot",100,400,100,50,green)
            text(str(int(self.PInven.getPrice('Mana Potion')/2))+ "G",200,400,100,50,white)
            
            if self.buttons['Mana Potion'] == 0:
                text("<--",300,400,50,50,grey)
            else:
                button("<--",300,400,50,50,red,bright_red,self.decreaseManaPotion)
            
            text(str(self.PInven.checkAmount('Mana Potion') - self.buttons['Mana Potion']),350,400,50,50,white)

            if self.PInven.checkAmount('Mana Potion') == self.buttons['Mana Potion']:
                text("-->",400,400,50,50,grey)
            else:
                button("-->",400,400,50,50,red, bright_red,self.increaseManaPotion)
            
            text(str(int(self.PInven.getPrice('Mana Potion')/2) * self.buttons['Mana Potion']) + "G",450,400,100,50,green)

            if self.buttons['Mana Potion'] == 0:
                text("sell",550,400,50,50,grey)
            else:
                button("sell",550,400,50,50,red,bright_red,self.sellManaPotion)



            text("Skelly Eye",100,450,100,50,green)
            text(str(int(self.PInven.getPrice('Skelly Eye')/2))+ "G",200,450,100,50,white)
            
            if self.buttons['Skelly Eye'] == 0:
                text("<--",300,450,50,50,grey)
            else:
                button("<--",300,450,50,50,red,bright_red,self.decreaseSkellyEye)
            
            text(str(self.PInven.checkAmount('Skelly Eye') - self.buttons['Skelly Eye']),350,450,50,50,white)

            if self.PInven.checkAmount('Skelly Eye') == self.buttons['Skelly Eye']:
                text("-->",400,450,50,50,grey)
            else:
                button("-->",400,450,50,50,red, bright_red,self.increaseSkellyEye)
            
            text(str(int(self.PInven.getPrice('Skelly Eye')/2) * self.buttons['Skelly Eye']) + "G",450,450,100,50,green)

            if self.buttons['Skelly Eye'] == 0:
                text("sell",550,450,50,50,grey)
            else:
                button("sell",550,450,50,50,red,bright_red,self.sellSkellyEye)



            text("Leather",100,500,100,50,green)
            text(str(int(self.PInven.getPrice('Leather')/2))+ "G",200,500,100,50,white)
            
            if self.buttons['Leather'] == 0:
                text("<--",300,500,50,50,grey)
            else:
                button("<--",300,500,50,50,red,bright_red,self.decreaseLeather)
            
            text(str(self.PInven.checkAmount('Leather') - self.buttons['Leather']),350,500,50,50,white)

            if self.PInven.checkAmount('Leather') == self.buttons['Leather']:
                text("-->",400,500,50,50,grey)
            else:
                button("-->",400,500,50,50,red, bright_red,self.increaseLeather)
            
            text(str(int(self.PInven.getPrice('Leather')/2) * self.buttons['Leather']) + "G",450,500,100,50,green)

            if self.buttons['Leather'] == 0:
                text("sell",550,500,50,50,grey)
            else:
                button("sell",550,500,50,50,red,bright_red,self.sellLeather)

            

            button("Back",50,750,100,50,red,bright_red,self.back)

            pygame.display.update()
            clock.tick(15)




    # buy screen--------------------------------------------------------------------------

    def buy(self):
        dialog = random.choice(self.buyDia)
        
        while self.shop:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 100)
            medText = pygame.font.SysFont("times",30)
            TextSurf, TextRect = text_objects("Shop of Destiny", largeText, white)
            TextRect.center = ((display_width/2),(display_height/10))

            TextMess, TextLoc = text_objects(dialog, medText, white)
            TextLoc.center = ((display_width/2),(display_height/4))
            
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextMess, TextLoc)

            if self.state == 0:
                text("Fang",100,250,100,50,green)
                text(str(self.PInven.getPrice('Fang'))+ "G",200,250,100,50,white)
                
                if self.buttons['Fang'] == 0:
                    text("<--",300,250,50,50,grey)
                else:
                    button("<--",300,250,50,50,red,bright_red,self.decreaseFang)
                
                text(str(self.buttons['Fang']),350,250,50,50,white)

                if (self.PInven.getPrice('Fang') * (self.buttons['Fang'] + 1)) > self.PInven.gold:
                    text("-->",400,250,50,50,grey)
                else:
                    button("-->",400,250,50,50,red, bright_red,self.increaseFang)
                
                text(str(self.PInven.getPrice('Fang') * self.buttons['Fang']) + "G",450,250,100,50,green)

                if self.buttons['Fang'] == 0:
                    text("buy",550,250,50,50,grey)
                else:
                    button("buy",550,250,50,50,red,bright_red,self.buyFang)



                text("H Ring",100,300,100,50,green)
                text(str(self.PInven.getPrice('Ring of Health'))+ "G",200,300,100,50,white)
                
                if self.buttons['Ring of Health'] == 0:
                    text("<--",300,300,50,50,grey)
                else:
                    button("<--",300,300,50,50,red,bright_red,self.decreaseROH)
                
                text(str(self.buttons['Ring of Health']),350,300,50,50,white)

                if (self.PInven.getPrice('Ring of Health') * (self.buttons['Ring of Health'] + 1)) > self.PInven.gold:
                    text("-->",400,300,50,50,grey)
                else:
                    button("-->",400,300,50,50,red, bright_red,self.increaseROH)
                
                text(str(self.PInven.getPrice('Ring of Health') * self.buttons['Ring of Health']) + "G",450,300,100,50,green)

                if self.buttons['Ring of Health'] == 0:
                    text("buy",550,300,50,50,grey)
                else:
                    button("buy",550,300,50,50,red,bright_red,self.buyROH)



                text("Sword",100,550,100,50,green)
                text(str(self.PInven.getPrice('Sword'))+ "G",200,550,100,50,white)
                
                if self.buttons['Sword'] == 0:
                    text("<--",300,550,50,50,grey)
                else:
                    button("<--",300,550,50,50,red,bright_red,self.decreaseSword)
                
                text(str(self.buttons['Sword']),350,550,50,50,white)

                if (self.PInven.getPrice('Sword') * (self.buttons['Sword'] + 1)) > self.PInven.gold:
                    text("-->",400,550,50,50,grey)
                else:
                    button("-->",400,550,50,50,red, bright_red,self.increaseSword)
                
                text(str(self.PInven.getPrice('Sword') * self.buttons['Sword']) + "G",450,550,100,50,green)

                if self.buttons['Sword'] == 0:
                    text("buy",550,550,50,50,grey)
                else:
                    button("buy",550,550,50,50,red,bright_red,self.buySword)



                text("Health Pot",100,350,100,50,green)
                text(str(self.PInven.getPrice('Health Potion'))+ "G",200,350,100,50,white)
                
                if self.buttons['Health Potion'] == 0:
                    text("<--",300,350,50,50,grey)
                else:
                    button("<--",300,350,50,50,red,bright_red,self.decreaseHealthPotion)
                
                text(str(self.buttons['Health Potion']),350,350,50,50,white)

                if (self.PInven.getPrice('Health Potion') * (self.buttons['Health Potion'] + 1)) > self.PInven.gold:
                    text("-->",400,350,50,50,grey)
                else:
                    button("-->",400,350,50,50,red, bright_red,self.increaseHealthPotion)
                
                text(str(self.PInven.getPrice('Health Potion') * self.buttons['Health Potion']) + "G",450,350,100,50,green)

                if self.buttons['Health Potion'] == 0:
                    text("buy",550,350,50,50,grey)
                else:
                    button("buy",550,350,50,50,red,bright_red,self.buyHealthPotion)



                text("Mana Pot",100,400,100,50,green)
                text(str(self.PInven.getPrice('Mana Potion'))+ "G",200,400,100,50,white)
                
                if self.buttons['Mana Potion'] == 0:
                    text("<--",300,400,50,50,grey)
                else:
                    button("<--",300,400,50,50,red,bright_red,self.decreaseManaPotion)
                
                text(str(self.buttons['Mana Potion']),350,400,50,50,white)

                if (self.PInven.getPrice('Mana Potion') * (self.buttons['Mana Potion'] + 1)) > self.PInven.gold:
                    text("-->",400,400,50,50,grey)
                else:
                    button("-->",400,400,50,50,red, bright_red,self.increaseManaPotion)
                
                text(str(self.PInven.getPrice('Mana Potion') * self.buttons['Mana Potion']) + "G",450,400,100,50,green)

                if self.buttons['Mana Potion'] == 0:
                    text("buy",550,400,50,50,grey)
                else:
                    button("buy",550,400,50,50,red,bright_red,self.buyManaPotion)



                text("Skelly Eye",100,450,100,50,green)
                text(str(self.PInven.getPrice('Skelly Eye'))+ "G",200,450,100,50,white)
                
                if self.buttons['Skelly Eye'] == 0:
                    text("<--",300,450,50,50,grey)
                else:
                    button("<--",300,450,50,50,red,bright_red,self.decreaseSkellyEye)
                
                text(str(self.buttons['Skelly Eye']),350,450,50,50,white)

                if (self.PInven.getPrice('Skelly Eye') * (self.buttons['Skelly Eye'] + 1)) > self.PInven.gold:
                    text("-->",400,450,50,50,grey)
                else:
                    button("-->",400,450,50,50,red, bright_red,self.increaseSkellyEye)
                
                text(str(self.PInven.getPrice('Skelly Eye') * self.buttons['Skelly Eye']) + "G",450,450,100,50,green)

                if self.buttons['Skelly Eye'] == 0:
                    text("buy",550,450,50,50,grey)
                else:
                    button("buy",550,450,50,50,red,bright_red,self.buySkellyEye)



                text("Leather",100,500,100,50,green)
                text(str(self.PInven.getPrice('Leather'))+ "G",200,500,100,50,white)
                
                if self.buttons['Leather'] == 0:
                    text("<--",300,500,50,50,grey)
                else:
                    button("<--",300,500,50,50,red,bright_red,self.decreaseLeather)
                
                text(str(self.buttons['Leather']),350,500,50,50,white)

                if (self.PInven.getPrice('Leather') * (self.buttons['Leather'] + 1)) > self.PInven.gold:
                    text("-->",400,500,50,50,grey)
                else:
                    button("-->",400,500,50,50,red, bright_red,self.increaseLeather)
                
                text(str(self.PInven.getPrice('Leather') * self.buttons['Leather']) + "G",450,500,100,50,green)

                if self.buttons['Leather'] == 0:
                    text("buy",550,500,50,50,grey)
                else:
                    button("buy",550,500,50,50,red,bright_red,self.buyLeather)



            elif self.state == 1:
                text("Fang",100,250,100,50,green)
                text(str(self.PInven.getPrice('Fang'))+ "G",200,250,100,50,white)
                
                if self.buttons['Fang'] == 0:
                    text("<--",300,250,50,50,grey)
                else:
                    button("<--",300,250,50,50,red,bright_red,self.decreaseFang)
                
                text(str(self.buttons['Fang']),350,250,50,50,white)

                if (self.PInven.getPrice('Fang') * (self.buttons['Fang'] + 1)) > self.PInven.gold:
                    text("-->",400,250,50,50,grey)
                else:
                    button("-->",400,250,50,50,red, bright_red,self.increaseFang)
                
                text(str(self.PInven.getPrice('Fang') * self.buttons['Fang']) + "G",450,250,100,50,green)

                if self.buttons['Fang'] == 0:
                    text("buy",550,250,50,50,grey)
                else:
                    button("buy",550,250,50,50,red,bright_red,self.buyFang)



                text("H Ring",100,300,100,50,green)
                text(str(self.PInven.getPrice('Ring of Health'))+ "G",200,300,100,50,white)
                
                if self.buttons['Ring of Health'] == 0:
                    text("<--",300,300,50,50,grey)
                else:
                    button("<--",300,300,50,50,red,bright_red,self.decreaseROH)
                
                text(str(self.buttons['Ring of Health']),350,300,50,50,white)

                if (self.PInven.getPrice('Ring of Health') * (self.buttons['Ring of Health'] + 1)) > self.PInven.gold:
                    text("-->",400,300,50,50,grey)
                else:
                    button("-->",400,300,50,50,red, bright_red,self.increaseROH)
                
                text(str(self.PInven.getPrice('Ring of Health') * self.buttons['Ring of Health']) + "G",450,300,100,50,green)

                if self.buttons['Ring of Health'] == 0:
                    text("buy",550,300,50,50,grey)
                else:
                    button("buy",550,300,50,50,red,bright_red,self.buyROH)



                text("Sword",100,350,100,50,green)
                text(str(self.PInven.getPrice('Sword'))+ "G",200,350,100,50,white)
                
                if self.buttons['Sword'] == 0:
                    text("<--",300,350,50,50,grey)
                else:
                    button("<--",300,350,50,50,red,bright_red,self.decreaseSword)
                
                text(str(self.buttons['Sword']),350,350,50,50,white)

                if (self.PInven.getPrice('Sword') * (self.buttons['Sword'] + 1)) > self.PInven.gold:
                    text("-->",400,350,50,50,grey)
                else:
                    button("-->",400,350,50,50,red, bright_red,self.increaseSword)
                
                text(str(self.PInven.getPrice('Sword') * self.buttons['Sword']) + "G",450,350,100,50,green)

                if self.buttons['Sword'] == 0:
                    text("buy",550,350,50,50,grey)
                else:
                    button("buy",550,350,50,50,red,bright_red,self.buySword)



                text("Health Pot",100,350,100,50,green)
                text(str(self.PInven.getPrice('Health Potion'))+ "G",200,350,100,50,white)
                
                if self.buttons['Health Potion'] == 0:
                    text("<--",300,350,50,50,grey)
                else:
                    button("<--",300,350,50,50,red,bright_red,self.decreaseHealthPotion)
                
                text(str(self.buttons['Health Potion']),350,350,50,50,white)

                if (self.PInven.getPrice('Health Potion') * (self.buttons['Health Potion'] + 1)) > self.PInven.gold:
                    text("-->",400,350,50,50,grey)
                else:
                    button("-->",400,350,50,50,red, bright_red,self.increaseHealthPotion)
                
                text(str(self.PInven.getPrice('Health Potion') * self.buttons['Health Potion']) + "G",450,350,100,50,green)

                if self.buttons['Health Potion'] == 0:
                    text("buy",550,350,50,50,grey)
                else:
                    button("buy",550,350,50,50,red,bright_red,self.buyHealthPotion)



                text("Mana Pot",100,400,100,50,green)
                text(str(self.PInven.getPrice('Mana Potion'))+ "G",200,400,100,50,white)
                
                if self.buttons['Mana Potion'] == 0:
                    text("<--",300,400,50,50,grey)
                else:
                    button("<--",300,400,50,50,red,bright_red,self.decreaseManaPotion)
                
                text(str(self.buttons['Mana Potion']),350,400,50,50,white)

                if (self.PInven.getPrice('Mana Potion') * (self.buttons['Mana Potion'] + 1)) > self.PInven.gold:
                    text("-->",400,400,50,50,grey)
                else:
                    button("-->",400,400,50,50,red, bright_red,self.increaseManaPotion)
                
                text(str(self.PInven.getPrice('Mana Potion') * self.buttons['Mana Potion']) + "G",450,400,100,50,green)

                if self.buttons['Mana Potion'] == 0:
                    text("buy",550,400,50,50,grey)
                else:
                    button("buy",550,400,50,50,red,bright_red,self.buyManaPotion)



                text("Skelly Eye",100,450,100,50,green)
                text(str(self.PInven.getPrice('Skelly Eye'))+ "G",200,450,100,50,white)
                
                if self.buttons['Skelly Eye'] == 0:
                    text("<--",300,450,50,50,grey)
                else:
                    button("<--",300,450,50,50,red,bright_red,self.decreaseSkellyEye)
                
                text(str(self.buttons['Skelly Eye']),350,450,50,50,white)

                if (self.PInven.getPrice('Skelly Eye') * (self.buttons['Skelly Eye'] + 1)) > self.PInven.gold:
                    text("-->",400,450,50,50,grey)
                else:
                    button("-->",400,450,50,50,red, bright_red,self.increaseSkellyEye)
                
                text(str(self.PInven.getPrice('Skelly Eye') * self.buttons['Skelly Eye']) + "G",450,450,100,50,green)

                if self.buttons['Skelly Eye'] == 0:
                    text("buy",550,450,50,50,grey)
                else:
                    button("buy",550,450,50,50,red,bright_red,self.buySkellyEye)



                text("Leather",100,500,100,50,green)
                text(str(self.PInven.getPrice('Leather'))+ "G",200,500,100,50,white)
                
                if self.buttons['Leather'] == 0:
                    text("<--",300,500,50,50,grey)
                else:
                    button("<--",300,500,50,50,red,bright_red,self.decreaseLeather)
                
                text(str(self.buttons['Leather']),350,500,50,50,white)

                if (self.PInven.getPrice('Leather') * (self.buttons['Leather'] + 1)) > self.PInven.gold:
                    text("-->",400,500,50,50,grey)
                else:
                    button("-->",400,500,50,50,red, bright_red,self.increaseLeather)
                
                text(str(self.PInven.getPrice('Leather') * self.buttons['Leather']) + "G",450,500,100,50,green)

                if self.buttons['Leather'] == 0:
                    text("buy",550,500,50,50,grey)
                else:
                    button("buy",550,500,50,50,red,bright_red,self.buyLeather)


            elif self.state == 2:
                text("Fang",100,250,100,50,green)
                text(str(self.PInven.getPrice('Fang'))+ "G",200,250,100,50,white)
                
                if self.buttons['Fang'] == 0:
                    text("<--",300,250,50,50,grey)
                else:
                    button("<--",300,250,50,50,red,bright_red,self.decreaseFang)
                
                text(str(self.buttons['Fang']),350,250,50,50,white)

                if (self.PInven.getPrice('Fang') * (self.buttons['Fang'] + 1)) > self.PInven.gold:
                    text("-->",400,250,50,50,grey)
                else:
                    button("-->",400,250,50,50,red, bright_red,self.increaseFang)
                
                text(str(self.PInven.getPrice('Fang') * self.buttons['Fang']) + "G",450,250,100,50,green)

                if self.buttons['Fang'] == 0:
                    text("buy",550,250,50,50,grey)
                else:
                    button("buy",550,250,50,50,red,bright_red,self.buyFang)



                text("H Ring",100,300,100,50,green)
                text(str(self.PInven.getPrice('Ring of Health'))+ "G",200,300,100,50,white)
                
                if self.buttons['Ring of Health'] == 0:
                    text("<--",300,300,50,50,grey)
                else:
                    button("<--",300,300,50,50,red,bright_red,self.decreaseROH)
                
                text(str(self.buttons['Ring of Health']),350,300,50,50,white)

                if (self.PInven.getPrice('Ring of Health') * (self.buttons['Ring of Health'] + 1)) > self.PInven.gold:
                    text("-->",400,300,50,50,grey)
                else:
                    button("-->",400,300,50,50,red, bright_red,self.increaseROH)
                
                text(str(self.PInven.getPrice('Ring of Health') * self.buttons['Ring of Health']) + "G",450,300,100,50,green)

                if self.buttons['Ring of Health'] == 0:
                    text("buy",550,300,50,50,grey)
                else:
                    button("buy",550,300,50,50,red,bright_red,self.buyROH)



                text("Sword",100,350,100,50,green)
                text(str(self.PInven.getPrice('Sword'))+ "G",200,350,100,50,white)
                
                if self.buttons['Sword'] == 0:
                    text("<--",300,350,50,50,grey)
                else:
                    button("<--",300,350,50,50,red,bright_red,self.decreaseSword)
                
                text(str(self.buttons['Sword']),350,350,50,50,white)

                if (self.PInven.getPrice('Sword') * (self.buttons['Sword'] + 1)) > self.PInven.gold:
                    text("-->",400,350,50,50,grey)
                else:
                    button("-->",400,350,50,50,red, bright_red,self.increaseSword)
                
                text(str(self.PInven.getPrice('Sword') * self.buttons['Sword']) + "G",450,350,100,50,green)

                if self.buttons['Sword'] == 0:
                    text("buy",550,350,50,50,grey)
                else:
                    button("buy",550,350,50,50,red,bright_red,self.buySword)



                text("Health Pot",100,350,100,50,green)
                text(str(self.PInven.getPrice('Health Potion'))+ "G",200,350,100,50,white)
                
                if self.buttons['Health Potion'] == 0:
                    text("<--",300,350,50,50,grey)
                else:
                    button("<--",300,350,50,50,red,bright_red,self.decreaseHealthPotion)
                
                text(str(self.buttons['Health Potion']),350,350,50,50,white)

                if (self.PInven.getPrice('Health Potion') * (self.buttons['Health Potion'] + 1)) > self.PInven.gold:
                    text("-->",400,350,50,50,grey)
                else:
                    button("-->",400,350,50,50,red, bright_red,self.increaseHealthPotion)
                
                text(str(self.PInven.getPrice('Health Potion') * self.buttons['Health Potion']) + "G",450,350,100,50,green)

                if self.buttons['Health Potion'] == 0:
                    text("buy",550,350,50,50,grey)
                else:
                    button("buy",550,350,50,50,red,bright_red,self.buyHealthPotion)



                text("Mana Pot",100,400,100,50,green)
                text(str(self.PInven.getPrice('Mana Potion'))+ "G",200,400,100,50,white)
                
                if self.buttons['Mana Potion'] == 0:
                    text("<--",300,400,50,50,grey)
                else:
                    button("<--",300,400,50,50,red,bright_red,self.decreaseManaPotion)
                
                text(str(self.buttons['Mana Potion']),350,400,50,50,white)

                if (self.PInven.getPrice('Mana Potion') * (self.buttons['Mana Potion'] + 1)) > self.PInven.gold:
                    text("-->",400,400,50,50,grey)
                else:
                    button("-->",400,400,50,50,red, bright_red,self.increaseManaPotion)
                
                text(str(self.PInven.getPrice('Mana Potion') * self.buttons['Mana Potion']) + "G",450,400,100,50,green)

                if self.buttons['Mana Potion'] == 0:
                    text("buy",550,400,50,50,grey)
                else:
                    button("buy",550,400,50,50,red,bright_red,self.buyManaPotion)



                text("Skelly Eye",100,450,100,50,green)
                text(str(self.PInven.getPrice('Skelly Eye'))+ "G",200,450,100,50,white)
                
                if self.buttons['Skelly Eye'] == 0:
                    text("<--",300,450,50,50,grey)
                else:
                    button("<--",300,450,50,50,red,bright_red,self.decreaseSkellyEye)
                
                text(str(self.buttons['Skelly Eye']),350,450,50,50,white)

                if (self.PInven.getPrice('Skelly Eye') * (self.buttons['Skelly Eye'] + 1)) > self.PInven.gold:
                    text("-->",400,450,50,50,grey)
                else:
                    button("-->",400,450,50,50,red, bright_red,self.increaseSkellyEye)
                
                text(str(self.PInven.getPrice('Skelly Eye') * self.buttons['Skelly Eye']) + "G",450,450,100,50,green)

                if self.buttons['Skelly Eye'] == 0:
                    text("buy",550,450,50,50,grey)
                else:
                    button("buy",550,450,50,50,red,bright_red,self.buySkellyEye)



                text("Leather",100,500,100,50,green)
                text(str(self.PInven.getPrice('Leather'))+ "G",200,500,100,50,white)
                
                if self.buttons['Leather'] == 0:
                    text("<--",300,500,50,50,grey)
                else:
                    button("<--",300,500,50,50,red,bright_red,self.decreaseLeather)
                
                text(str(self.buttons['Leather']),350,500,50,50,white)

                if (self.PInven.getPrice('Leather') * (self.buttons['Leather'] + 1)) > self.PInven.gold:
                    text("-->",400,500,50,50,grey)
                else:
                    button("-->",400,500,50,50,red, bright_red,self.increaseLeather)
                
                text(str(self.PInven.getPrice('Leather') * self.buttons['Leather']) + "G",450,500,100,50,green)

                if self.buttons['Leather'] == 0:
                    text("buy",550,500,50,50,grey)
                else:
                    button("buy",550,500,50,50,red,bright_red,self.buyLeather)


            elif self.state >= 3:
                text("Fang",100,250,100,50,green)
                text(str(self.PInven.getPrice('Fang'))+ "G",200,250,100,50,white)
                
                if self.buttons['Fang'] == 0:
                    text("<--",300,250,50,50,grey)
                else:
                    button("<--",300,250,50,50,red,bright_red,self.decreaseFang)
                
                text(str(self.buttons['Fang']),350,250,50,50,white)

                if (self.PInven.getPrice('Fang') * (self.buttons['Fang'] + 1)) > self.PInven.gold:
                    text("-->",400,250,50,50,grey)
                else:
                    button("-->",400,250,50,50,red, bright_red,self.increaseFang)
                
                text(str(self.PInven.getPrice('Fang') * self.buttons['Fang']) + "G",450,250,100,50,green)

                if self.buttons['Fang'] == 0:
                    text("buy",550,250,50,50,grey)
                else:
                    button("buy",550,250,50,50,red,bright_red,self.buyFang)



                text("H Ring",100,300,100,50,green)
                text(str(self.PInven.getPrice('Ring of Health'))+ "G",200,300,100,50,white)
                
                if self.buttons['Ring of Health'] == 0:
                    text("<--",300,300,50,50,grey)
                else:
                    button("<--",300,300,50,50,red,bright_red,self.decreaseROH)
                
                text(str(self.buttons['Ring of Health']),350,300,50,50,white)

                if (self.PInven.getPrice('Ring of Health') * (self.buttons['Ring of Health'] + 1)) > self.PInven.gold:
                    text("-->",400,300,50,50,grey)
                else:
                    button("-->",400,300,50,50,red, bright_red,self.increaseROH)
                
                text(str(self.PInven.getPrice('Ring of Health') * self.buttons['Ring of Health']) + "G",450,300,100,50,green)

                if self.buttons['Ring of Health'] == 0:
                    text("buy",550,300,50,50,grey)
                else:
                    button("buy",550,300,50,50,red,bright_red,self.buyROH)



                text("Sword",100,350,100,50,green)
                text(str(self.PInven.getPrice('Sword'))+ "G",200,350,100,50,white)
                
                if self.buttons['Sword'] == 0:
                    text("<--",300,350,50,50,grey)
                else:
                    button("<--",300,350,50,50,red,bright_red,self.decreaseSword)
                
                text(str(self.buttons['Sword']),350,350,50,50,white)

                if (self.PInven.getPrice('Sword') * (self.buttons['Sword'] + 1)) > self.PInven.gold:
                    text("-->",400,350,50,50,grey)
                else:
                    button("-->",400,350,50,50,red, bright_red,self.increaseSword)
                
                text(str(self.PInven.getPrice('Sword') * self.buttons['Sword']) + "G",450,350,100,50,green)

                if self.buttons['Sword'] == 0:
                    text("buy",550,350,50,50,grey)
                else:
                    button("buy",550,350,50,50,red,bright_red,self.buySword)



                text("Health Pot",100,350,100,50,green)
                text(str(self.PInven.getPrice('Health Potion'))+ "G",200,350,100,50,white)
                
                if self.buttons['Health Potion'] == 0:
                    text("<--",300,350,50,50,grey)
                else:
                    button("<--",300,350,50,50,red,bright_red,self.decreaseHealthPotion)
                
                text(str(self.buttons['Health Potion']),350,350,50,50,white)

                if (self.PInven.getPrice('Health Potion') * (self.buttons['Health Potion'] + 1)) > self.PInven.gold:
                    text("-->",400,350,50,50,grey)
                else:
                    button("-->",400,350,50,50,red, bright_red,self.increaseHealthPotion)
                
                text(str(self.PInven.getPrice('Health Potion') * self.buttons['Health Potion']) + "G",450,350,100,50,green)

                if self.buttons['Health Potion'] == 0:
                    text("buy",550,350,50,50,grey)
                else:
                    button("buy",550,350,50,50,red,bright_red,self.buyHealthPotion)



                text("Mana Pot",100,400,100,50,green)
                text(str(self.PInven.getPrice('Mana Potion'))+ "G",200,400,100,50,white)
                
                if self.buttons['Mana Potion'] == 0:
                    text("<--",300,400,50,50,grey)
                else:
                    button("<--",300,400,50,50,red,bright_red,self.decreaseManaPotion)
                
                text(str(self.buttons['Mana Potion']),350,400,50,50,white)

                if (self.PInven.getPrice('Mana Potion') * (self.buttons['Mana Potion'] + 1)) > self.PInven.gold:
                    text("-->",400,400,50,50,grey)
                else:
                    button("-->",400,400,50,50,red, bright_red,self.increaseManaPotion)
                
                text(str(self.PInven.getPrice('Mana Potion') * self.buttons['Mana Potion']) + "G",450,400,100,50,green)

                if self.buttons['Mana Potion'] == 0:
                    text("buy",550,400,50,50,grey)
                else:
                    button("buy",550,400,50,50,red,bright_red,self.buyManaPotion)



                text("Skelly Eye",100,450,100,50,green)
                text(str(self.PInven.getPrice('Skelly Eye'))+ "G",200,450,100,50,white)
                
                if self.buttons['Skelly Eye'] == 0:
                    text("<--",300,450,50,50,grey)
                else:
                    button("<--",300,450,50,50,red,bright_red,self.decreaseSkellyEye)
                
                text(str(self.buttons['Skelly Eye']),350,450,50,50,white)

                if (self.PInven.getPrice('Skelly Eye') * (self.buttons['Skelly Eye'] + 1)) > self.PInven.gold:
                    text("-->",400,450,50,50,grey)
                else:
                    button("-->",400,450,50,50,red, bright_red,self.increaseSkellyEye)
                
                text(str(self.PInven.getPrice('Skelly Eye') * self.buttons['Skelly Eye']) + "G",450,450,100,50,green)

                if self.buttons['Skelly Eye'] == 0:
                    text("buy",550,450,50,50,grey)
                else:
                    button("buy",550,450,50,50,red,bright_red,self.buySkellyEye)



                text("Leather",100,500,100,50,green)
                text(str(self.PInven.getPrice('Leather'))+ "G",200,500,100,50,white)
                
                if self.buttons['Leather'] == 0:
                    text("<--",300,500,50,50,grey)
                else:
                    button("<--",300,500,50,50,red,bright_red,self.decreaseLeather)
                
                text(str(self.buttons['Leather']),350,500,50,50,white)

                if (self.PInven.getPrice('Leather') * (self.buttons['Leather'] + 1)) > self.PInven.gold:
                    text("-->",400,500,50,50,grey)
                else:
                    button("-->",400,500,50,50,red, bright_red,self.increaseLeather)
                
                text(str(self.PInven.getPrice('Leather') * self.buttons['Leather']) + "G",450,500,100,50,green)

                if self.buttons['Leather'] == 0:
                    text("buy",550,500,50,50,grey)
                else:
                    button("buy",550,500,50,50,red,bright_red,self.buyLeather)
                
            
            button("Back",50,750,100,50,red,bright_red,self.back)

            pygame.display.update()
            clock.tick(15)




    # initial shop--------------------------------------------------------------------

    def shop_intro(self):

        dialog = random.choice(self.introDia)
        

        while self.Run:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 100)
            medText = pygame.font.SysFont("times",30)
            TextSurf, TextRect = text_objects("Shop of Destiny", largeText, white)
            TextRect.center = ((display_width/2),(display_height/10))

            TextMess, TextLoc = text_objects(dialog, medText, white)
            TextLoc.center = ((display_width/2),(display_height/4))
            
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextMess, TextLoc)
            gameDisplay.blit(shopImg, (display_width/2 - 400,display_height/3))
            
            button("Buy",800,250,100,50,green,bright_green,self.buy)
            button("Sell",800,350,100,50,green,bright_green,self.sell)
            button("Back",800,450,100,50,red,bright_red,self.escape)

            if self.shop == False:
                dialog = random.choice(self.introDia)
                self.resetAll()
                self.shop = True

            pygame.display.update()
            clock.tick(15)
        self.blackout()
        return self.PInven

        







