import pygame
import time
import os
import menu

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
 
block_color = (53,115,255)
 
quitgame = pygame.quit
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Arcade')
clock = pygame.time.Clock()

arcadeImg = pygame.image.load('arcade.jpg')
arcadeImg = pygame.transform.scale(arcadeImg, (200, 200))

class Arcade:
    def __init__(self, gold):
        self.intro = true
        self.gold = gold

        def text_objects(text, font):
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
        textSurf, textRect = text_objects(msg, smallText)
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

                BackGround = Background('arcade.jpg', [0,0])

# Back Controllers-----------------------------------------------------------------------------------
            def back(self):
                self.shop = False

            def escape(self):
                self.Run = False



# initial shop--------------------------------------------------------------------

            def run(self):
                x=2

            def runGame1(self):
                self.gold -= 15
               
            def runGame2(self):
                self.gold -= 15
                
            def runGame3(self):
                self.gold -= 15

            def runGame4(self):
                self.gold -= 15

            def blackout(self):
                counter = 0
        
                while counter != 75:
            
                    for event in pygame.event.get():
                        print(event)
                        if event.type == pygame.QUIT:
                            break
                    gameDisplay.fill(black)

                    if counter >= 15:
                        medText = pygame.font.SysFont("times",30)
                        TextSurf, TextRect = text_objects("You feel well rested!", medText, white)
                        TextRect.center = ((display_width/2),(display_height/2))
                        gameDisplay.blit(TextSurf, TextRect)

                    pygame.display.update()
                    clock.tick(15)
                    counter += 1
                
            def arcade_intro(self):

                while intro:
                    for event in pygame.event.get():
                        print(event)
                        if event.type == pygame.QUIT:
                            break
                
            gameDisplay.fill(white)
            gameDisplay.blit(BackGround.image, BackGround.rect)
            largeText = pygame.font.SysFont("times", 60)
            medText = pygame.font.SysFont("times",30)
            title = "                     Arcade"
            text = largeText.render(title, True, white)
            gameDisplay.blit(text, ((display_width/6),(display_height/42)))
            
            if self.gold >= 15:
                button("Level 1 15G",75,250,100,50,orange,bright_orange,run)
            else:
                text("Level 1 15G",75,250,100,50,grey)
                
            if self.gold >= 15:
                button("Level 2 15G",220,250,100,50,orange,bright_orange,run)
            else:
                text("Level 2 15G",220,250,100,50,grey)
                
            if self.gold >= 15:
                button("Level 3 15G",880,250,100,50,orange,bright_orange,run)
            else:
                text("Level 3 15G",880,250,100,50,grey)
                
            if self.gold >= 15:
                button("Level 4 15G",1030,250,100,50,orange,bright_orange,run)
            else:
                text("Level 4 15G",1030,250,100,50,grey)
                
            button("Exit",1030,500,100,50,red,bright_red,self.escape)

            pygame.display.update()
            clock.tick(15)
        self.blackout()
        return self.gold



