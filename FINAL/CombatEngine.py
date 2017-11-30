import pygame
import time
import random
import Enemy
import Player
import CombatEngine
import Items
import queue


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

BackGround = Background('B1.png', [0,0])

#--------------------------------------------------------------------------------------------

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = Enemy.enemies[enemy]
        self.EHP = self.enemy.hp
        self.enemypic = pygame.image.load(enemy + ".png")
        self.enemypic = pygame.transform.scale(self.enemypic, (200, 200))
        self.plarmor = 5
        if self.player.armor[0] == True:
            self.plarmor += Items.items[self.player.armor[1]].defence
        self.run = True
        self.plAlive = True
        self.playerW1 = 0
        if self.player.firsthand[0] == True:
            self.playerW1 = Items.items[self.player.firsthand[1]].damage
        self.playerW2 = 0
        if self.player.secondhand[0] == True:
            self.playerW2 = Items.items[self.player.secondhand[1]].damage

        self.rawDam = self.playerW1 + self.playerW2 + self.player.strength
        self.enemyAlive = True



#--------------------------------------------------------------------------------------------
    def blackout(self):
        counter = 0
        
        while counter != 30:
            
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
            gameDisplay.fill(black)

            if counter >= 5:
                medText = pygame.font.SysFont("times",30)
                TextSurf, TextRect = text_objects("You got away safely", medText, white)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)

            pygame.display.update()
            clock.tick(15)
            counter += 1

    def death(self):
        counter = 0
        
        while counter != 45:
            
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
            gameDisplay.fill(red)

            if counter >= 5:
                medText = pygame.font.SysFont("times",30)
                TextSurf, TextRect = text_objects("You Died", medText, black)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)

            pygame.display.update()
            clock.tick(15)
            counter += 1


    def escape(self):
        if self.player.agility > self.enemy.agl:
            self.run = False
            self.blackout()

        else:
            if random.choice([1,2,3,4,5,6,7,8,9,10]) > 5:
                self.run = False
                self.blackout()
            else:
                self.enemyTurn()

    def win(self):
        drops = []
        for drop in self.enemy.drops:
            counter = drop[1]
            for x in range(counter):
                drops.append(drop[0])

        drop = random.choice(drops)
        self.player.inventory.addItem(drop, 1)
        self.player.inventory.gold += self.enemy.gold
        self.run = False
            


    def enemyTurn(self):
        self.player.health -= self.calcEnemyDamage()

    def defend(self):
        self.player.health -= int(self.calcEnemyDamage() * .5)
        if self.player.health <= 0:
            self.plAlive = False
        
    def fight(self):
        self.enemy.hp -= self.rawDam
        self.enemyTurn()

    def skill(self):
        if self.player.mana >= 20:
            if self.player.health < (self.player.maxHealth-50):
               self.player.health+=50
               self.player.mana-=20
            else:
                self.player.health=self.player.maxHealth
                self.player.mana-=20
        self.enemyTurn()
    
    # Returns how much damage an enemy will do to the player
    def calcEnemyDamage(self):
        return int(self.enemy.attack * ((100 - self.plarmor)/100))

#Combat-------------------------------------------------------------------------

    def combat_intro(self):

        while self.run and self.plAlive:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 100)
            medText = pygame.font.SysFont("times",30)

            
            gameDisplay.blit(self.enemypic, (600,200))


            text("Cur HP",200,100,100,50,white)
            text("Enemy HP",200,150,100,50,white)
            button("Heal Spell",100,700,100,50,green,bright_green,self.skill)
            text(str(self.player.health),300,100,100,50,white )
            text(str(self.enemy.hp),300,150,100,50,white)
            text(str(self.player.mana),100,650,100,50,white)
            button("Fight",300,700,100,50,green,bright_green,self.fight)
            button("Defend",500,700,100,50,green,bright_green,self.defend)  
            button("Run",700,700,100,50,red,bright_red,self.escape)
            

            pygame.display.update()
            clock.tick(15)

            if self.player.health <= 0:
                self.plAlive = False

            if self.enemy.hp <=0:
                self.enemyAlive = False
                self.win()

            if self.plAlive == False:
                self.death()
                
        self.enemy.hp = self.EHP
        return self.plAlive, self.player 
