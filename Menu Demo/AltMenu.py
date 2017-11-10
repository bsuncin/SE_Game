import pygame
import time
import os
import Menu

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
 
block_color = (53,115,255)
 
quitgame = pygame.quit
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dungeons of Optional Doom')
clock = pygame.time.Clock()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('doom.jpg', [0,0])

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


def run():
    Menu.game_intro()


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                quit()
                
        gameDisplay.fill(white)
        gameDisplay.blit(BackGround.image, BackGround.rect)
        largeText = pygame.font.SysFont("times", 60)
        medText = pygame.font.SysFont("times",30)
        title = "Dungeons of Optional Doom"
        text = largeText.render(title, True, white)
        gameDisplay.blit(text, ((display_width/6),(display_height/10)))  
        #TextSurf, TextRect = text_objects("Dungeons of Optional Doom", largeText)
        #TextRect.center = ((display_width/2),(display_height/10))

        #TextMess, TextLoc = text_objects(dialog, medText)
        #TextLoc.center = ((display_width/2),(display_height/4))
        
        #gameDisplay.blit(TextSurf, TextRect, white)
        #gameDisplay.blit(TextMess, TextLoc)
        #gameDisplay.blit(shopImg, (display_width/2 - 400,display_height/3))
        
        button("New Game",200,250,100,50,green,bright_green,run)
        button("Load",200,350,100,50,red,bright_red,game_intro)
        button("Quit",200,450,100,50,blue,bright_blue,quitgame)

        pygame.display.update()
        clock.tick(15)
