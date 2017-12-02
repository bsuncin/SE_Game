import pygame
import time
import random



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
blue = (0, 0, 200)
orange = (255,165,0)
purple = (128,0,128)
yellow = (255,255,0)
 
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

#-------------------------------------------------------------------------------
        
class Mastermind:

    def __init__(self):
        self.colors = [red, green, blue, orange, purple, yellow]
        self.code = []
        
        for x in range(4):
            choice = random.choice(self.colors)
            self.code.append(choice)
            self.colors.remove(choice)

        self.ans1 = white
        self.ans2 = white
        self.ans3 = white
        self.ans4 = white

        self.answers = [self.ans1, self.ans2, self.ans3, self.ans4]
        self.previous = []
        self.previousAnswers = []

        self.numCorrect = 0
        self.numIncorrect = 0
        self.turns = 10
        self.run = True
        self.Win = False


        self.guess1pos1 = white
        self.guess2pos1 = white
        self.guess3pos1 = white
        self.guess4pos1 = white
        self.guess5pos1 = white
        self.guess6pos1 = white
        self.guess7pos1 = white
        self.guess8pos1 = white
        self.guess9pos1 = white
        self.guess10pos1 = white
            
        self.guess1pos2 = white
        self.guess2pos2 = white
        self.guess3pos2 = white
        self.guess4pos2 = white
        self.guess5pos2 = white
        self.guess6pos2 = white
        self.guess7pos2 = white
        self.guess8pos2 = white
        self.guess9pos2 = white
        self.guess10pos2 = white

        self.guess1pos3 = white
        self.guess2pos3 = white
        self.guess3pos3 = white
        self.guess4pos3 = white
        self.guess5pos3 = white
        self.guess6pos3 = white
        self.guess7pos3 = white
        self.guess8pos3 = white
        self.guess9pos3 = white
        self.guess10pos3 = white

        self.guess1pos4 = white
        self.guess2pos4 = white
        self.guess3pos4 = white
        self.guess4pos4 = white
        self.guess5pos4 = white
        self.guess6pos4 = white
        self.guess7pos4 = white
        self.guess8pos4 = white
        self.guess9pos4 = white
        self.guess10pos4 = white

        self.guess1corr = 0
        self.guess2corr = 0
        self.guess3corr = 0
        self.guess4corr = 0
        self.guess5corr = 0
        self.guess6corr = 0
        self.guess7corr = 0
        self.guess8corr = 0
        self.guess9corr = 0
        self.guess10corr = 0

        self.guess1wro = 0
        self.guess2wro = 0
        self.guess3wro = 0
        self.guess4wro = 0
        self.guess5wro = 0
        self.guess6wro = 0
        self.guess7wro = 0
        self.guess8wro = 0
        self.guess9wro = 0
        self.guess10wro = 0
        
        

    def red1(self):
        self.ans1 = red

    def red2(self):
        self.ans2 = red

    def red3(self):
        self.ans3 = red

    def red4(self):
        self.ans4 = red

    def blue1(self):
        self.ans1 = blue

    def blue2(self):
        self.ans2 = blue

    def blue3(self):
        self.ans3 = blue

    def blue4(self):
        self.ans4 = blue

    def green1(self):
        self.ans1 = green

    def green2(self):
        self.ans2 = green

    def green3(self):
        self.ans3 = green

    def green4(self):
        self.ans4 = green

    def orange1(self):
        self.ans1 = orange

    def orange2(self):
        self.ans2 = orange

    def orange3(self):
        self.ans3 = orange

    def orange4(self):
        self.ans4 = orange

    def purple1(self):
        self.ans1 = purple

    def purple2(self):
        self.ans2 = purple

    def purple3(self):
        self.ans3 = purple

    def purple4(self):
        self.ans4 = purple

    def yellow1(self):
        self.ans1 = yellow

    def yellow2(self):
        self.ans2 = yellow

    def yellow3(self):
        self.ans3 = yellow

    def yellow4(self):
        self.ans4 = yellow

    def reset(self):
        self.ans1 = white
        self.ans2 = white
        self.ans3 = white
        self.ans4 = white

    def escape(self):
        self.run = False
        

    def guess(self):
        self.numCorrect = 0
        self.numIncorrect = 0
        self.turns -= 1
        
        if self.ans1 == self.code[0]:
            self.numCorrect += 1
        if self.ans2 == self.code[1]:
            self.numCorrect += 1
        if self.ans3 == self.code[2]:
            self.numCorrect += 1
        if self.ans4 == self.code[3]:
            self.numCorrect += 1

        if self.ans1 not in self.code:
            self.numIncorrect += 1
        if self.ans2 not in self.code:
            self.numIncorrect += 1
        if self.ans3 not in self.code:
            self.numIncorrect += 1
        if self.ans4 not in self.code:
            self.numIncorrect += 1
        
        
        if self.turns == 0:
            self.guess10corr = self.numCorrect
            self.guess10pos1 = self.ans1
            self.guess10pos2 = self.ans2
            self.guess10pos3 = self.ans3
            self.guess10pos4 = self.ans4
            self.guess10wro = 4 - self.numIncorrect - self.numCorrect
            
        elif self.turns == 9:
            self.guess1corr = self.numCorrect
            self.guess1pos1 = self.ans1
            self.guess1pos2 = self.ans2
            self.guess1pos3 = self.ans3
            self.guess1pos4 = self.ans4
            self.guess1wro = 4 - self.numIncorrect - self.numCorrect
            
        elif self.turns == 8:
            self.guess2corr = self.numCorrect
            self.guess2pos1 = self.ans1
            self.guess2pos2 = self.ans2
            self.guess2pos3 = self.ans3
            self.guess2pos4 = self.ans4
            self.guess2wro = 4 - self.numIncorrect - self.numCorrect
   
        elif self.turns == 7:
            self.guess3corr = self.numCorrect
            self.guess3pos1 = self.ans1
            self.guess3pos2 = self.ans2
            self.guess3pos3 = self.ans3
            self.guess3pos4 = self.ans4
            self.guess3wro = 4 - self.numIncorrect - self.numCorrect
          
        elif self.turns == 6:
            self.guess4corr = self.numCorrect
            self.guess4pos1 = self.ans1
            self.guess4pos2 = self.ans2
            self.guess4pos3 = self.ans3
            self.guess4pos4 = self.ans4
            self.guess4wro = 4 - self.numIncorrect - self.numCorrect
            
        elif self.turns == 5:
            self.guess5corr = self.numCorrect
            self.guess5pos1 = self.ans1
            self.guess5pos2 = self.ans2
            self.guess5pos3 = self.ans3
            self.guess5pos4 = self.ans4
            self.guess5wro = 4 - self.numIncorrect - self.numCorrect
            
        elif self.turns == 4:
            self.guess6corr = self.numCorrect
            self.guess6pos1 = self.ans1
            self.guess6pos2 = self.ans2
            self.guess6pos3 = self.ans3
            self.guess6pos4 = self.ans4
            self.guess6wro = 4 - self.numIncorrect - self.numCorrect
            
        elif self.turns == 3:
            self.guess7corr = self.numCorrect
            self.guess7pos1 = self.ans1
            self.guess7pos2 = self.ans2
            self.guess7pos3 = self.ans3
            self.guess7pos4 = self.ans4
            self.guess7wro = 4 - self.numIncorrect - self.numCorrect

        elif self.turns == 2:
            self.guess8corr = self.numCorrect
            self.guess8pos1 = self.ans1
            self.guess8pos2 = self.ans2
            self.guess8pos3 = self.ans3
            self.guess8pos4 = self.ans4
            self.guess8wro = 4 - self.numIncorrect - self.numCorrect
            
        elif self.turns == 1:
            self.guess9corr = self.numCorrect
            self.guess9pos1 = self.ans1
            self.guess9pos2 = self.ans2
            self.guess9pos3 = self.ans3
            self.guess9pos4 = self.ans4
            self.guess9wro = 4 - self.numIncorrect - self.numCorrect

        if self.numCorrect == 4:
            self.Win = True
        self.reset()

    def back(self):
        self.backtrack = False
            

    def goodGuess(self):
        if self.ans1 != white and self.ans2 != white and self.ans3 != white and self.ans4 != white:
            self.guess()

    def EndGameWin(self):
        counter = 0
        self.run = False
        while counter < 30:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            TextSurf, TextRect = text_objects("Mastermind", largeText, black)
            TextRect.center = ((display_width/2),(display_height/10))
            gameDisplay.blit(TextSurf, TextRect)

            TextSurf, TextRect = text_objects("You Win!", largeText, black)
            TextRect.center = ((600),(400))
            gameDisplay.blit(TextSurf, TextRect)
            

            pygame.display.update()
            clock.tick(15)
            counter += 1

    def EndGameLose(self):
        counter = 0
        self.run = False
        while counter < 30:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(red)
            TextSurf, TextRect = text_objects("Mastermind", largeText, black)
            TextRect.center = ((display_width/2),(display_height/10))
            gameDisplay.blit(TextSurf, TextRect)

            TextSurf, TextRect = text_objects("You Lose!", largeText, black)
            TextRect.center = ((600),(400))
            gameDisplay.blit(TextSurf, TextRect)
            
            pygame.display.update()
            clock.tick(15)
            counter += 1
    def game(self):
            
        while self.run:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    break
                    
            gameDisplay.fill(white)
            TextSurf, TextRect = text_objects("Mastermind", largeText, black)
            TextRect.center = ((display_width/2),(display_height/10))
            gameDisplay.blit(TextSurf, TextRect)
            
            text("",600,250,60,60,black)
            text("",605,255,50,50,self.ans1)
            text("",660,250,60,60,black)
            text("",665,255,50,50,self.ans2)
            text("",720,250,60,60,black)
            text("",725,255,50,50,self.ans3)
            text("",780,250,60,60,black)
            text("",785,255,50,50,self.ans4)
            button("",605,325,50,50,red,red,self.red1)
            button("",665,325,50,50,red,red,self.red2)
            button("",725,325,50,50,red,red,self.red3)
            button("",785,325,50,50,red,red,self.red4)
            button("",605,385,50,50,blue,blue,self.blue1)
            button("",665,385,50,50,blue,blue,self.blue2)
            button("",725,385,50,50,blue,blue,self.blue3)
            button("",785,385,50,50,blue,blue,self.blue4)
            button("",605,445,50,50,green,green,self.green1)
            button("",665,445,50,50,green,green,self.green2)
            button("",725,445,50,50,green,green,self.green3)
            button("",785,445,50,50,green,green,self.green4)
            button("",605,505,50,50,orange,orange,self.orange1)
            button("",665,505,50,50,orange,orange,self.orange2)
            button("",725,505,50,50,orange,orange,self.orange3)
            button("",785,505,50,50,orange,orange,self.orange4)
            button("",605,565,50,50,purple,purple,self.purple1)
            button("",665,565,50,50,purple,purple,self.purple2)
            button("",725,565,50,50,purple,purple,self.purple3)
            button("",785,565,50,50,purple,purple,self.purple4)
            button("",605,625,50,50,yellow,yellow,self.yellow1)
            button("",665,625,50,50,yellow,yellow,self.yellow2)
            button("",725,625,50,50,yellow,yellow,self.yellow3)
            button("",785,625,50,50,yellow,yellow,self.yellow4)
            button("Guess",670,685,100,50,green,bright_green,self.goodGuess)
            text("#Correct",600,150,100,50,green)

            text('1',0,200,50,50,white)
            text('2',0,250,50,50,white)
            text('3',0,300,50,50,white)
            text('4',0,350,50,50,white)
            text('5',0,400,50,50,white)
            text('6',0,450,50,50,white)
            text('7',0,500,50,50,white)
            text('8',0,550,50,50,white)
            text('9',0,600,50,50,white)
            text('10',0,650,50,50,white)
            
            text('',50,200,50,50,self.guess1pos1)
            text('',50,250,50,50,self.guess2pos1)
            text('',50,300,50,50,self.guess3pos1)
            text('',50,350,50,50,self.guess4pos1)
            text('',50,400,50,50,self.guess5pos1)
            text('',50,450,50,50,self.guess6pos1)
            text('',50,500,50,50,self.guess7pos1)
            text('',50,550,50,50,self.guess8pos1)
            text('',50,600,50,50,self.guess9pos1)
            text('',50,650,50,50,self.guess10pos1)
            
            text('',100,200,50,50,self.guess1pos2)
            text('',100,250,50,50,self.guess2pos2)
            text('',100,300,50,50,self.guess3pos2)
            text('',100,350,50,50,self.guess4pos2)
            text('',100,400,50,50,self.guess5pos2)
            text('',100,450,50,50,self.guess6pos2)
            text('',100,500,50,50,self.guess7pos2)
            text('',100,550,50,50,self.guess8pos2)
            text('',100,600,50,50,self.guess9pos2)
            text('',100,650,50,50,self.guess10pos2)

            text('',150,200,50,50,self.guess1pos3)
            text('',150,250,50,50,self.guess2pos3)
            text('',150,300,50,50,self.guess3pos3)
            text('',150,350,50,50,self.guess4pos3)
            text('',150,400,50,50,self.guess5pos3)
            text('',150,450,50,50,self.guess6pos3)
            text('',150,500,50,50,self.guess7pos3)
            text('',150,550,50,50,self.guess8pos3)
            text('',150,600,50,50,self.guess9pos3)
            text('',150,650,50,50,self.guess10pos3)

            text('',200,200,50,50,self.guess1pos4)
            text('',200,250,50,50,self.guess2pos4)
            text('',200,300,50,50,self.guess3pos4)
            text('',200,350,50,50,self.guess4pos4)
            text('',200,400,50,50,self.guess5pos4)
            text('',200,450,50,50,self.guess6pos4)
            text('',200,500,50,50,self.guess7pos4)
            text('',200,550,50,50,self.guess8pos4)
            text('',200,600,50,50,self.guess9pos4)
            text('',200,650,50,50,self.guess10pos4)

            text(str(self.guess1corr),250,200,50,50,white)
            text(str(self.guess2corr),250,250,50,50,white)
            text(str(self.guess3corr),250,300,50,50,white)
            text(str(self.guess4corr),250,350,50,50,white)
            text(str(self.guess5corr),250,400,50,50,white)
            text(str(self.guess6corr),250,450,50,50,white)
            text(str(self.guess7corr),250,500,50,50,white)
            text(str(self.guess8corr),250,550,50,50,white)
            text(str(self.guess9corr),250,600,50,50,white)
            text(str(self.guess10corr),250,650,50,50,white)

            text(str(self.guess1wro),300,200,50,50,white)
            text(str(self.guess2wro),300,250,50,50,white)
            text(str(self.guess3wro),300,300,50,50,white)
            text(str(self.guess4wro),300,350,50,50,white)
            text(str(self.guess5wro),300,400,50,50,white)
            text(str(self.guess6wro),300,450,50,50,white)
            text(str(self.guess7wro),300,500,50,50,white)
            text(str(self.guess8wro),300,550,50,50,white)
            text(str(self.guess9wro),300,600,50,50,white)
            text(str(self.guess10wro),300,650,50,50,white)
            

    
            text(str(self.numCorrect),700,150,50,50,green)
            button("Exit",1070,685,100,50,red,bright_red,self.escape)
            if self.Win == True:
                self.EndGameWin()

            if self.turns == 0 and self.Win == False:
                self.EndGameLose()
                

            
            pygame.display.update()
            clock.tick(15)
        return self.Win

#ma = Mastermind()
#ma.game()
