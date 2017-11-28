import pygame
import time
import os
import menu
import Player as P

pygame.init()
 
display_width = 1200
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
blue = (0,0,200)
bright_blue = (0,0,255)
orange = (255,100,0)
bright_orange = (255,150,0)
amber = (255,191,0)
bright_amber = (255,210,0)
silver = (192,192,192)
bright_silver = (211,211,211)
grey = (128,128,128)

block_color = (53,115,255)
 
quitgame = pygame.quit
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dungeons of Optional Doom')
clock = pygame.time.Clock()

def text_objects(text, font, color):
    textSurface = font.render(text, True, black)
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
    textSurf, textRect = text_objects(msg, smallText, white)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('equip.png', [0,0])

class Equipment:
    def __init__(self, PInven, PEquip):
        self.PInven = PInven
        self.PEquip = PEquip
        
        self.weapon1 = 'none'
        if self.PEquip.righthand[0]==True:
            self.weapon1 = self.PEquip.righthand[1]
            
        self.weapon2 = 'none'
        if self.PEquip.lefthand[0]==True:
            self.weapon2 = self.PEquip.lefthand[1]
            
        self.ring1 = 'none'
        if self.PEquip.firstfinger[0]==True:
            self.ring1 = self.PEquip.firstfinger[1]
            
        self.ring2 = 'none'
        if self.PEquip.secondfinger[0]==True:
            self.ring1 = self.PEquip.secondfinger[1]
            
        self.armor = 'none'
        if self.PEquip.armor[0]==True:
            self.ring1 = self.PEquip.armor[1]
            
        self.Run = True
        self.equip = True
        self.currEquipArmor = self.PEquip.armor[1]
        self.currEquipRing1 = self.PEquip.firstfinger[1]
        self.currEquipRing2 = self.PEquip.secondfinger[1]
        self.currEquipWeapon1 = self.PEquip.righthand[1]
        self.currEquipWeapon2 = self.PEquip.lefthand[1]

# Button Controllers------------------------------------------------------------
            
    def equipPlatemail(self):
        if self.PEquip.armor[0] == False:
            self.PEquip.equipArmor('Platemail')
            self.currEquipArmor = self.PEquip.armor[1]
            
    def equipLeather(self):
        if self.PEquip.armor[0] == False:
            self.PEquip.equipArmor('Leather')
            self.currEquipArmor = self.PEquip.armor[1]

    def equipChainmail(self):
        if self.PEquip.armor[0] == False:
            self.PEquip.equipArmor('Chainmail')
            self.currEquipArmor = self.PEquip.armor[1]
            
    def equipTatteredRobes(self):
        if self.PEquip.armor[0] == False:
            self.PEquip.equipArmor('Tattered Robes')
            self.currEquipArmor = self.PEquip.armor[1]

    def equipSword1(self):
        if self.PEquip.righthand[0] == False:
            self.PEquip.equipRighthand('Sword')
            self.currEquipWeapon1 = self.PEquip.righthand[1]

    def equipSword2(self):
        if self.PEquip.lefthand[0] == False:
            self.PEquip.equipLefthand('Sword')
            self.currEquipWeapon2 = self.PEquip.lefthand[1]

    def equipDagger1(self):
        if self.PEquip.righthand[0] == False:
            self.PEquip.equipRighthand('Dagger')
            self.currEquipWeapon1 = self.PEquip.righthand[1]

    def equipDagger2(self):
        if self.PEquip.lefthand[0] == False:
            self.PEquip.equipLefthand('Dagger')
            self.currEquipWeapon2 = self.PEquip.lefthand[1]

    def equipClub1(self):
        if self.PEquip.righthand[0] == False:
            self.PEquip.equipRighthand('Club')
            self.currEquipWeapon1 = self.PEquip.righthand[1]

    def equipClub2(self):
        if self.PEquip.lefthand[0] == False:
            self.PEquip.equipLefthand('Club')
            self.currEquipWeapon2 = self.PEquip.lefthand[1]

    def equipBrokenStick1(self):
        if self.PEquip.righthand[0] == False:
            self.PEquip.equipRighthand('Broken Stick')
            self.currEquipWeapon1 = self.PEquip.righthand[1]

    def equipBrokenStick2(self):
        if self.PEquip.lefthand[0] == False:
            self.PEquip.equipLefthand('Broken Stick')
            self.currEquipWeapon2 = self.PEquip.lefthand[1]

    def equipRingH1(self):
        if self.PEquip.firstfinger[0] == False:
            self.PEquip.equipFirstfinger('Ring of Health')
            self.currEquipRing1 = self.PEquip.firstfinger[1]

    def equipRingH2(self):
        if self.PEquip.secondfinger[0] == False:
            self.PEquip.equipSecondfinger('Ring of Health')
            self.currEquipRing2 = self.PEquip.secondfinger[1]

    def equipRingM1(self):
        if self.PEquip.firstfinger[0] == False:
            self.PEquip.equipFirstfinger('Ring of Mana')
            self.currEquipRing1 = self.PEquip.firstfinger[1]

    def equipRingM2(self):
        if self.PEquip.secondfinger[0] == False:
            self.PEquip.equipSecondfinger('Ring of Mana')
            self.currEquipRing2 = self.PEquip.secondfinger[1]

    def unequiparmor(self, item):
        if self.PEquip.armor[0] == False:
            pass
        else:
            self.PEquip.removeArmor(item)

    def unequiprighthand(self, item):
        if self.PEquip.righthand[0] == False:
            pass
        else:
            self.PEquip.removeRighthand(item)

    def unequiplefthand(self, item):
        if self.PEquip.lefthand[0] == False:
            pass
        else:
            self.PEquip.removeLefthand(item)

    def unequipfirstfinger(self, item):
        if self.PEquip.firstfinger[0] == False:
            pass
        else:
            self.PEquip.removeFirstfinger(item)

    def unequipsecondfinger(self, item):
        if self.PEquip.secondfinger[0] == False:
            pass
        else:
            self.PEquip.removeSecondfinger(item)

        
# Back Controllers-----------------------------------------------------------------------------------
    def back(self):
        self.equip = False

    def escape(self):
        self.Run = False

    def blackout(self):
        counter = 0
        
        while counter != 3:
            
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
            gameDisplay.fill(black)


            pygame.display.update()
            clock.tick(15)
            counter += 1

# Armor equip screen--------------------------------------------------------------------

    def armorequip(self):

        while self.equip:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break

            gameDisplay.fill(white)
            BackGround = Background('armor.png', [0,0])
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 60)
            medText = pygame.font.SysFont("times",30)      

            if self.PInven.checkAmount('Platemail') > 0 and (
                self.currEquipArmor != "Platemail"):
                button("Platemail",150,250,150,50,amber,bright_amber,self.equipPlatemail)
            else:
                text("Platemail",150,250,150,50,grey)

            
            if self.PInven.checkAmount('Leather') > 0 and (
                self.currEquipArmor != "Leather"):
                button("Leather",150,450,150,50,amber,bright_amber,self.equipLeather)
            else:
                text("Leather",150,450,150,50,grey)

            if self.PInven.checkAmount('Chainmail') > 0 and (
                self.currEquipArmor != "Chainmail"):
                button("Chainmail",900,450,150,50,amber,bright_amber,self.equipChainmail)
            else:
                text("Chainmail",900,450,150,50,grey)

            if self.PInven.checkAmount('Tattered Robes') > 0 and (
                self.currEquipArmor != "Tattered Robes"):
                button("Tattered Robes",900,250,150,50,amber,bright_amber,self.equipTatteredRobes)
            else:
                text("Tattered Robes",900,250,150,50,grey)

            if self.currEquipArmor == None:
                text("No Armor", 500,100,200,50,grey)
            else:
                button(str(self.currEquipArmor),500,100,200,50,amber,bright_amber,self.unequiparmor(self.currEquipArmor))

            button("Back", 1100,2,100,50,red,bright_red,self.back)
            
            pygame.display.update()
            clock.tick(15)
            
        self.blackout()

# Weapon1 equip screen------------------------------------------------------------

    def weapon1equip(self):

        while self.equip:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break

            gameDisplay.fill(white)
            BackGround = Background('sword.png', [0,0])
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 60)
            medText = pygame.font.SysFont("times",30)

            if self.PInven.checkAmount('Sword') > 0 and (
                self.currEquipWeapon1 != "Sword"):
                button("Sword",100,175,150,50,silver,bright_silver,self.equipSword1)
            else:
                text("Sword",100,175,150,50,grey)

            
            if self.PInven.checkAmount('Dagger') > 0 and (
                self.currEquipWeapon1 != "Dagger"):
                button("Dagger",75,500,150,50,silver,bright_silver,self.equipDagger1)
            else:
                text("Dagger",75,500,150,50,grey)

            if self.PInven.checkAmount('Club') > 0 and (
                self.currEquipWeapon1 != "Club"):
                button("Club",1000,500,150,50,silver,bright_silver,self.equipClub1)
            else:
                text("Club",1000,500,150,50,grey)

            if self.PInven.checkAmount('Broken Stick') > 0 and (
                self.currEquipWeapon1 != "Broken Stick"):
                button("Broken Stick",925,175,150,50,silver,bright_silver,self.equipBrokenStick1)
            else:
                text("Broken Stick",925,175,150,50,grey)

            if self.currEquipWeapon1 == None:
                text("No Weapon In Right", 500,100,200,50,grey)
            else:
                button(str(self.currEquipWeapon1),500,100,200,50,silver,bright_silver,self.unequiprighthand(self.currEquipWeapon1))

            button("Back", 1100,2,100,50,red,bright_red,self.back)
            
            pygame.display.update()
            clock.tick(15)
            
        self.blackout()

# Weapon2 equip screen------------------------------------------------------------

    def weapon2equip(self):

        while self.equip:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break

            gameDisplay.fill(white)
            BackGround = Background('sword.png', [0,0])
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 60)
            medText = pygame.font.SysFont("times",30)
           
            if self.PInven.checkAmount('Sword') > 0 and (
                self.currEquipWeapon2 != "Sword"):
                button("Sword",100,175,150,50,silver,bright_silver,self.equipSword2)
            else:
                text("Sword",100,175,150,50,grey)

            
            if self.PInven.checkAmount('Dagger') > 0 and (
                self.currEquipWeapon2 != "Dagger"):
                button("Dagger",75,500,150,50,silver,bright_silver,self.equipDagger2)
            else:
                text("Dagger",75,500,150,50,grey)

            if self.PInven.checkAmount('Club') > 0 and (
                self.currEquipWeapon2 != "Club"):
                button("Club",1000,500,150,50,silver,bright_silver,self.equipClub2)
            else:
                text("Club",1000,500,150,50,grey)

            if self.PInven.checkAmount('Broken Stick') > 0 and (
                self.currEquipWeapon2 != "Broken Stick"):
                button("Broken Stick",925,175,150,50,silver,bright_silver,self.equipBrokenStick2)
            else:
                text("Broken Stick",925,175,150,50,grey)

            if self.currEquipWeapon2 == None:
                text("No Weapon", 500,100,200,50,grey)
            else:
                button(str(self.currEquipWeapon2),500,100,200,50,silver,bright_silver,self.unequiplefthand(self.currEquipWeapon2))

            button("Back", 1100,2,100,50,red,bright_red,self.back)
            
            pygame.display.update()
            clock.tick(15)
            
        self.blackout()
            
# Ring1 equip screen------------------------------------------------------------

    def ring1equip(self):

        while self.equip:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break

            gameDisplay.fill(white)
            BackGround = Background('Ring.png', [0,0])
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 60)
            medText = pygame.font.SysFont("times",30)

            if self.PInven.checkAmount('Ring of Health') > 0 and (
                self.currEquipRing1 != "Ring of Health"):
                button("Ring of Health",100,300,150,50,blue,bright_blue,self.equipRingH1)
            else:
                text("Ring of Health",100,300,150,50,grey)


            if self.PInven.checkAmount('Ring of Mana') > 0 and (
                self.currEquipRing1 != "Ring of Mana"):
                button("Ring of Mana",925,300,150,50,blue,bright_blue,self.equipRingM1)
            else:
                text("Ring of Mana",925,300,150,50,grey)

            if self.currEquipRing1 == None:
                text("No Ring", 500,315,200,50,grey)
            else:
                button(str(self.currEquipRing1),500,315,200,50,blue,bright_blue,self.unequipfirstfinger(self.currEquipRing1))

            button("Back", 1100,2,100,50,red,bright_red,self.back)
            
            pygame.display.update()
            clock.tick(15)
            
        self.blackout()

# Ring2 equip screen------------------------------------------------------------

    def ring2equip(self):

        while self.equip:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break

            gameDisplay.fill(white)
            BackGround = Background('Ring.png', [0,0])
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 60)
            medText = pygame.font.SysFont("times",30)
            
            if self.PInven.checkAmount('Ring of Health') > 0 and (
                self.currEquipRing2 != "Ring of Health"):
                button("Ring of Health",100,300,150,50,blue,bright_blue,self.equipRingH2)
            else:
                text("Ring of Health",100,300,150,50,grey)


            if self.PInven.checkAmount('Ring of Mana') > 0 and (
                self.currEquipRing2 != "Ring of Mana"):
                button("Ring of Mana",925,300,150,50,blue,bright_blue,self.equipRingM2)
            else:
                text("Ring of Mana",925,300,150,50,grey)

            if self.currEquipRing2 == None:
                text("No Ring", 500,315,200,50,grey)
            else:
                button(str(self.currEquipRing2),500,315,200,50,blue,bright_blue,self.unequipsecondfinger(self.currEquipRing2))

            button("Back", 1100,2,100,50,red,bright_red,self.back)
            
            pygame.display.update()
            clock.tick(15)
            
        self.blackout()

    def Equip(self):
    
        while self.Run:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
           
            BackGround = Background('equip.png', [0,0])
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 60)
            medText = pygame.font.SysFont("times",30)
        
            button("Armor",600,175,100,50,amber,bright_amber,self.armorequip) 
            button("Ring 1",300,250,100,50,blue,bright_blue,self.ring1equip)
            button("Ring 2",850,250,100,50,blue,bright_blue,self.ring2equip)
            button("Weapon 1",300,350,100,50,silver,bright_silver,self.weapon1equip)
            button("Weapon 2",850,350,100,50,silver,bright_silver,self.weapon2equip)
            button("Exit",1030,500,100,50,red,bright_red,self.escape)

            
            
            pygame.display.update()
            clock.tick(15)
        self.blackout()
        return self.currEquipArmor and self.currEquipWeapon1 and self.currEquipWeapon2 and self.currEquipRing1 and self.currEquipRing2
        

