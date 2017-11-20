import pygame
import time
import random
import AltMenu
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


# Back Controllers-----------------------------------------------------------------------------------
    def back(self):
        self.shop = False

    def escape(self):
        self.Run = False



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
                self.shop = True

            pygame.display.update()
            clock.tick(15)

        return self.PInven
