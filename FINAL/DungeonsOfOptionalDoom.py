import pygame
import time
import os
import WorldEngine

pygame.init()
 
display_width = 1200
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
blue = (0,0,200)
bright_blue = (0,0,255)
intro = True
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
    w = WorldEngine.World(True)
    w.world_intro()


def run2():
    w = WorldEngine.World(False)
    w.world_intro()

def escape():
    global intro
    intro = False

def game_intro():

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                break
                
        gameDisplay.fill(white)
        gameDisplay.blit(BackGround.image, BackGround.rect)
        largeText = pygame.font.SysFont("times", 60)
        medText = pygame.font.SysFont("times",30)
        title = "Dungeons of Optional Doom"
        text = largeText.render(title, True, white)
        gameDisplay.blit(text, ((display_width/6),(display_height/10)))  
        
        button("New Game",200,250,100,50,green,bright_green,run)
        button("Load",200,350,100,50,red,bright_red,run2)
        button("Quit",200,450,100,50,blue,bright_blue,escape)

        pygame.display.update()
        clock.tick(15)


game_intro()
quit()
