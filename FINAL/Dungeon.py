import pygame
import time
import random
import Enemy
import Player
import CombatEngine as CE
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

BackGround = Background('B3.png', [0,0])



# Object controller-------------------------------------------------------------

class Dungeon:

    def __init__(self, player, state):
        self.player = player
        self.floor1 = ['Skeleton', 'Zombie', 'Fang', 'none', 'poop', 'stick', 'Dagger', 'none', 'none', 'none', 'none', 'none']
        self.floor2 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor3 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor4 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor5 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor6 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor7 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor8 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor9 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor10 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor11 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor12 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor13 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor14 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor15 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor16 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor17 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor18 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor19 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor20 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor21 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor22 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor23 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.floor24 = ['Skeleton', 'Zombie', 'Gold Nug', 'Fang', 'none', 'poop', 'stick', 'Dagger']
        self.boss = ['TheCage']
        self.floors = [self.floor1, self.floor2, self.floor3, self.floor4, self.floor5,
                       self.floor6, self.floor7, self.floor8, self.floor9, self.floor10,
                       self.floor11, self.floor12, self.floor13, self.floor14, self.floor15,
                       self.floor16, self.floor17, self.floor18, self.floor19, self.floor20,
                       self.floor21, self.floor22, self.floor23, self.floor24, self.boss]

        self.state = state
        self.run = True
        self.events = random.randrange(10,20)
        self.currFloor = state * 5
        
        if self.currFloor > 20:
            self.currFloor = 20

        self.intro = ['You walk into a dank smelly place, much like yourself.',
                      'Darkness engulfs you as you enter the dungeon.',
                      'Are you scared?',
                      'Just keep moving forward.'
                      ]
        self.pressOn = ['Do you continue on?',
                        'Do you keep exploring or run away?',
                        'Press on young explorer',
                        'So close yet so far away']
        
        self.item = None
        self.enemy = None
        self.event = None
        self.eventController = True
        self.alive = True
        



#Dungeon Controllers ------------------------------------------------------------------------
    def nextFloor(self):
        self.currFloor += 1

    def eventControl(self):
        self.eventController = False

    def escape(self):
        self.run = False

    def combat(self):
        cb = CE.Combat(self.player, self.enemy)
        self.alive, self.player = cb.combat_intro()
        self.eventController = False

    def blackout(self):
        counter = 0
        
        while counter != 30:
            
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
            gameDisplay.fill(black)

            pygame.display.update()
            clock.tick(15)
            counter += 1
    

    def search(self):
        event = random.choice(self.floors[self.currFloor])

        if event == 'poop':
            self.eventPoop()

        elif event == 'none':
            self.eventNone()

        elif event == 'stick':
            self.eventStick()
            
        elif event in Items.items:
            self.item = event
            self.event = 'Item'

        else:
            self.event = 'fight'
            self.enemy = event
            self.eventCombat()

    def eventPoop(self):
        
        dialog = 'You find some poop on the ground. Interesting'
        
        while self.eventController:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            TextSurf, TextRect = text_objects("Spoooky Dungeon", medText, white)
            TextRect.center = ((display_width/2),(display_height/10))

            TextMess, TextLoc = text_objects(dialog, medText, white)
            TextLoc.center = ((display_width/2),(display_height/4))
            
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextMess, TextLoc)
            
            button('Continue',500,250,100,50,green,bright_green,self.eventControl)
            pygame.display.update()
            clock.tick(15)

            
    def eventNone(self):
        
        dialog = 'You find nothing. A little disappointed you press on.'
        
        while self.eventController:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            TextSurf, TextRect = text_objects("Spoooky Dungeon", largeText, white)
            TextRect.center = ((display_width/2),(display_height/10))

            TextMess, TextLoc = text_objects(dialog, medText, white)
            TextLoc.center = ((display_width/2),(display_height/4))
            
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextMess, TextLoc)

            
            button('Continue',500,250,100,50,green,bright_green,self.eventControl)
            pygame.display.update()
            clock.tick(15)

            
    def eventStick(self):
        
        dialog = 'You find an impressive stick on the ground.'
        dialog2 = 'When you go to pick it up it jumped up and walked away.'
        dialog3 = 'A little dissapointed you walk away.'
        
        while self.eventController:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 100)
            medText = pygame.font.SysFont("times",30)
            TextSurf, TextRect = text_objects("Spoooky Dungeon", largeText, white)
            TextRect.center = ((display_width/2),(display_height/10))
            gameDisplay.blit(TextSurf, TextRect)
            
            TextMess, TextLoc = text_objects(dialog, medText, white)
            TextLoc.center = ((600),(200))
            gameDisplay.blit(TextMess, TextLoc)

            TextMess, TextLoc = text_objects(dialog2, medText, white)
            TextLoc.center = ((600),(250))
            gameDisplay.blit(TextMess, TextLoc)

            TextMess, TextLoc = text_objects(dialog3, medText, white)
            TextLoc.center = ((600),(300))
            gameDisplay.blit(TextMess, TextLoc)
            
            button('Continue',600,600,100,50,green,bright_green,self.eventControl)
            pygame.display.update()
            clock.tick(15)


    def eventCombat(self):
        dialog = 'Will you fight or run?'
        
        while self.eventController:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 100)
            medText = pygame.font.SysFont("times",30)
            TextSurf, TextRect = text_objects("Spoooky Dungeon", largeText, white)
            TextRect.center = ((display_width/2),(display_height/10))

            TextMess, TextLoc = text_objects(dialog, medText, white)
            TextLoc.center = ((display_width/2),(display_height/4))
            
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextMess, TextLoc)
            
            button('Fight',500,250,100,50,green,bright_green,self.combat)
            button('Run Away',500,350,100,50,green,bright_green,self.eventControl)
            pygame.display.update()
            clock.tick(15)
    

# initial Dungeon--------------------------------------------------------------------

    def Dungeon_intro(self):

        dialog = random.choice(self.intro)
        

        while self.run and self.alive:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 100)
            medText = pygame.font.SysFont("times",30)
            TextSurf, TextRect = text_objects("Spoooky Dungeon", largeText, white)
            TextRect.center = ((display_width/2),(display_height/10))

            TextMess, TextLoc = text_objects(dialog, medText, white)
            TextLoc.center = ((display_width/2),(display_height/4))
            
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextMess, TextLoc)
            
            button('Search',800,250,100,50,green,bright_green,self.search)
            
            button('Escape',800,450,100,50,red,bright_red,self.escape)

            if self.eventController == False:
                dialog = random.choice(self.pressOn)
                self.eventController = True

            pygame.display.update()
            clock.tick(15)

        return self.alive, self.player, self.state

        








