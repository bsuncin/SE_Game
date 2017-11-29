import pygame
import time
import random
import Player
import Dungeon
import Inn
import ShopNPCGreg as Shop


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

largeText = pygame.font.SysFont("times", 100)
medText = pygame.font.SysFont("times",30)
 
quitgame = pygame.quit
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dungeons of Optional Doom')
clock = pygame.time.Clock()

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

BackGround = Background('WorldMap.png', [0,0])
Throne = Background('ThroneRoom.png', [0,0])

pepe = pygame.image.load('kingPepeCry.png')
pepe = pygame.transform.scale(pepe, (400, 400))

#-----------------------------------------------------------------------------

class World:

    def __init__(self, intro):
        self.worldstate = 0
        self.shopstate = 0
        self.innstate = 0
        self.dungeonstate = 0
        self.run = True
        self.player = Player.Player()
        self.introScene = intro
        self.king = False
        self.kingback = True
        self.kingcounter = 0

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

    def intro(self):
        counter = 0
        count2 = 0
        
        while counter != 1000:
            
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
            gameDisplay.fill(black)

            if counter >= 10 and counter < 200:
                TextSurf, TextRect = text_objects("Once upon a time in a land not quite far away but really", medText, white)
                TextRect.center = ((600),(350))
                gameDisplay.blit(TextSurf, TextRect)
                
                TextSurf, TextRect = text_objects("somewhat not incredibly close, so pretty much in an indiclosed area in the", medText, white)
                TextRect.center = ((600),(400))
                gameDisplay.blit(TextSurf, TextRect)

                TextSurf, TextRect = text_objects("middle of far and close there was a great evil that fell on the kingdom of Antisoc.", medText, white)
                TextRect.center = ((600),(450))
                gameDisplay.blit(TextSurf, TextRect)

            elif counter > 200 and counter < 400:
                TextSurf, TextRect = text_objects("Antisoc was once a kingdom where memes were plentiful and chicken tendies ", medText, white)
                TextRect.center = ((600),(350))
                gameDisplay.blit(TextSurf, TextRect)
                
                TextSurf, TextRect = text_objects("abundant, but it has now fallen into the darkness that is crappy reposts and Kale Salads.", medText, white)
                TextRect.center = ((600),(400))
                gameDisplay.blit(TextSurf, TextRect)

            elif counter > 400 and counter < 600:
                TextSurf, TextRect = text_objects("This evil darkness was brought upon the land by one reason the disappearance", medText, white)
                TextRect.center = ((600),(350))
                gameDisplay.blit(TextSurf, TextRect)
                
                TextSurf, TextRect = text_objects("of the Queen \"Queen Slay\" whose husband, The King, threw off the", medText, white)
                TextRect.center = ((600),(400))
                gameDisplay.blit(TextSurf, TextRect)

                TextSurf, TextRect = text_objects("balance of the land with his sorrow.", medText, white)
                TextRect.center = ((600),(450))
                gameDisplay.blit(TextSurf, TextRect)

            elif counter > 600 and counter < 800:
                TextSurf, TextRect = text_objects("Many have tried and many have failed, only the Mightest adventurer can help", medText, white)
                TextRect.center = ((600),(350))
                gameDisplay.blit(TextSurf, TextRect)
                
                TextSurf, TextRect = text_objects("save the Queen and bring balance back to the kingdom.", medText, white)
                TextRect.center = ((600),(400))
                gameDisplay.blit(TextSurf, TextRect)

            elif counter > 800:
                if count2 < 100:
                    TextSurf, TextRect = text_objects("Dungeons of Optional Doom", pygame.font.SysFont("times", count2), white)
                    TextRect.center = ((600),(400))
                    gameDisplay.blit(TextSurf, TextRect)
                    count2 += 1

                else:
                    gameDisplay.blit(BackGround.image, BackGround.rect)
                    TextSurf, TextRect = text_objects("Dungeons of Optional Doom", pygame.font.SysFont("times", count2), white)
                    TextRect.center = ((600),(400))
                    gameDisplay.blit(TextSurf, TextRect)
                    
                

            pygame.display.update()
            clock.tick(15)
            counter += 1
    

    def escape(self):
        self.run = False

    def shop(self):
        self.blackout()
        shop = Shop.Shop(self.player.inventory, self.shopstate)
        self.player.inventory = shop.shop_intro()

    def inn(self):
        self.blackout()
        inn = Inn.Inn(self.player.inventory.gold, self.innstate)
        sleep, self.player.inventory.gold = inn.inn_intro()

        if sleep == True:
            self.player.Health = self.player.maxHealth

    def dungeon(self):
        self.blackout()
        dun = Dungeon.Dungeon(self.player, self.dungeonstate)
        self.alive, self.player, self.dungeonstate = dun.Dungeon_intro()

        if self.alive == False:
            self.alive = True
            self.blackout()
            inn = Inn.Inn(self.player.inventory.gold, self.innstate)
            sleep, self.player.inventory.gold = inn.death()
            self.player.Health = self.player.maxHealth

    def arcade(self):
        self.blackout()
        ar = Arcade.Arcade(self.player.inventory.gold)
        #self.player.inventory.gold

    def incKing(self):
        self.kingcounter += 1

    def fall(self):
        counter = 0
        
        while counter != 100:

            if counter < 50:
                gameDisplay.fill(red)
                TextSurf, TextRect = text_objects("You trip on a stick and die", medText, white)
                TextRect.center = ((600),(400))
                gameDisplay.blit(TextSurf, TextRect)
            else:
                gameDisplay.fill(red)
                TextSurf, TextRect = text_objects("Try Again", medText, white)
                TextRect.center = ((600),(400))
                gameDisplay.blit(TextSurf, TextRect)

            pygame.display.update()
            clock.tick(15)
            counter += 1

    def pepe_intro(self):
        self.blackout()
        self.king = True
        while self.kingcounter < 6:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(Throne.image, Throne.rect)
            TextSurf, TextRect = text_objects("Throne Room", largeText, white)
            TextRect.center = ((display_width/2),(display_height/10))
            
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(pepe, (500,100))

            if self.kingcounter == 0:
                TextSurf, TextRect = text_objects("*crying* WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!", medText, white)
                TextRect.center = ((600),(700))
                gameDisplay.blit(TextSurf, TextRect)
                button('next',500, 200, 100, 50, green, bright_green,self.incKing)
            elif self.kingcounter == 1:
                TextSurf, TextRect = text_objects("*sniff* oh hi didnt see you there, you probably already know why I'm", medText, white)
                TextRect.center = ((600),(700))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects("crying from some sort of narration,", medText, white)
                TextRect.center = ((600),(750))
                gameDisplay.blit(TextSurf, TextRect)
                button('next',200, 200, 100, 50, green, bright_green,self.incKing)
            elif self.kingcounter == 2:
                TextSurf, TextRect = text_objects("Well take a seat anyway im going to tell you again, my Queen was abducted", medText, white)
                TextRect.center = ((600),(650))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects("from me when we were strolling around outside the castle and was taken", medText, white)
                TextRect.center = ((600),(700))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects("to THE CAGE!! at the top floor of the DUNGEON OF optional DOOOOMM!!!!", medText, white)
                TextRect.center = ((600),(750))
                gameDisplay.blit(TextSurf, TextRect)
                button('next',800, 400, 100, 50, green, bright_green,self.incKing)

            elif self.kingcounter == 3:
                TextSurf, TextRect = text_objects("I couldnt do anything but sit and watch the hooligans take my ", medText, white)
                TextRect.center = ((600),(700))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects("Queen because of my accursed stubby legs.", medText, white)
                TextRect.center = ((600),(750))
                gameDisplay.blit(TextSurf, TextRect)
                button('next',500, 400, 100, 50, green, bright_green,self.incKing)

            elif self.kingcounter == 4:
                TextSurf, TextRect = text_objects("Please man ya gotta help me get my Queen back shes all I got.", medText, white)
                TextRect.center = ((600),(700))
                gameDisplay.blit(TextSurf, TextRect)
                button('Yes',200, 400, 100, 50, green, bright_green,self.incKing)
                button('No',300, 400, 100, 50, green, bright_green,self.fall)

            elif self.kingcounter == 5:
                TextSurf, TextRect = text_objects("oh.....really, I didnt think I'd get this far, no one has been crazy ", medText, white)
                TextRect.center = ((600),(700))
                gameDisplay.blit(TextSurf, TextRect)
                TextSurf, TextRect = text_objects("enough to say yes to this sucide mission. Now go forth", medText, white)
                TextRect.center = ((600),(750))
                gameDisplay.blit(TextSurf, TextRect)
                
                button('next',300, 400, 100, 50, green, bright_green,self.incKing)
                  
            
            pygame.display.update()
            clock.tick(15)
        self.blackout()

    def kingbackback(self):
        self.kingback = False

    def pepe_last(self):
        self.blackout()
        while self.kingback:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(Throne.image, Throne.rect)
            TextSurf, TextRect = text_objects("Throne Room", largeText, white)
            TextRect.center = ((display_width/2),(display_height/10))
            
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(pepe, (500,100))

            
            TextSurf, TextRect = text_objects("Save my Queen!!!", medText, white)
            TextRect.center = ((600),(650))
            gameDisplay.blit(TextSurf, TextRect)
            button("back",1000,750,100,50,red,bright_red,self.kingbackback)
                  
            
            pygame.display.update()
            clock.tick(15)
        self.blackout()

    def world_intro(self):
        if self.introScene == True:
            self.intro()
            
        while self.run:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            TextSurf, TextRect = text_objects("Island of Antisoc", largeText, white)
            TextRect.center = ((display_width/2),(display_height/10))
            
            gameDisplay.blit(TextSurf, TextRect)

            
            if self.king == False:
                button("Throne",1000,350,100,50,green,bright_green,self.pepe_intro)
                text("Shop",200,400,100,50,grey)
                text("Inn",400,400,100,50,grey)
                text("Dungeon",400,200,100,50,grey)
                text("Arcade",600,400,100,50,grey)
                text("Items",600,700,100,50,grey)
                text("Equip",800,700,100,50,grey)

            else:
                button("Throne",1000,350,100,50,green,bright_green,self.pepe_last)
                button("Shop",200,400,100,50,green,bright_green,self.shop)
                button("Inn",400,400,100,50,green,bright_green,self.inn)
                button("Dungeon",400,200,100,50,green,bright_green,self.dungeon)
                button("Arcade",600,400,100,50,green,bright_green,self.inn)
                button("Items",600,700,100,50,red,bright_red,self.escape)
                button("Equip",800,700,100,50,red,bright_red,self.escape)
                button("Back",1000,700,100,50,red,bright_red,self.escape)

            pygame.display.update()
            clock.tick(15)

