import pygame
import time
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
display_width=800
display_height=600

img = pygame.image.load("snakeHead.png")
appleimg=pygame.image.load("õun.png")

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Ussimännu")

icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

appleThickness=30
block_size=20
FPS=15

direction="right"

clock=pygame.time.Clock()

smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("comicsansms",80)

def pause():
     paused=True
     message_to_screen("paused", green,-100,size="large")
     message_to_screen("C to continue or Q to quit",black,0)
     pygame.display.update()
     while paused:
         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 pygame.quit
                 quit()
             if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_c:
                     paused=False
                 elif event.key==pygame.K_q:
                     pygame.quit()
                     quit()
         #gameDisplay.fill(white)
         clock.tick(5)


def score(score):
    text = smallfont.render("Score: "+str(score),True,black)
    gameDisplay.blit(text,[0,0])

def game_intro():
    intro=True
    while intro:
        gameDisplay.fill(white)
        message_to_screen("Ussimännu",
                          green,-100,"large")
        message_to_screen("Hello, my name is Torbedo el Nataro Von Shcuke!",
                          black, 100)
        message_to_screen("You never Win!",black,0)
        message_to_screen("C to play!",black,200)
        message_to_screen("P to pause",black,250)
        
        pygame.display.update()
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
def snake(block_size,snakelist):
    if direction=="right":
        head = pygame.transform.rotate(img, 270)
    if direction=="left":
        head = pygame.transform.rotate(img, 90)
    if direction=="up":
        head = img
    if direction=="down":
        head = pygame.transform.rotate(img, 180)
    
    gameDisplay.blit(head,(snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,black,[XnY[0], XnY[1], block_size, block_size])

def text_objects(text,color,size):
    if size == "small":   
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":   
        textSurface = medfont.render(text,True,color)
    elif size == "large":   
        textSurface = largefont.render(text,True,color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)
    
def gameLoop():
    global direction
    gameExit=False
    gameOver=False
    
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change=10
    lead_y_change=0
    
    snakeList=[]
    snakeLenght=1
    
    randAppleX=random.randrange(0,display_width-block_size,appleThickness)
    randAppleY=random.randrange(0,display_height-block_size,appleThickness)

    while not gameExit:
        if gameOver == True:
            message_to_screen("Game over", red,-50, size="large")
            message_to_screen("Press C to play again or Q to quit",
                              green,50,size="medium")
            pygame.display.update()
        while gameOver==True:
            direction="right"
            #gameDisplay.fill(white)
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                    if event.key==pygame.K_c:
                        gameLoop()
            if event.type==pygame.QUIT:
                gameExit=True
                gameOver=False
            
            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction="left"
                    lead_x_change = -block_size
                    lead_y_change=0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change=block_size
                    lead_y_change=0
                    direction="right"
                elif event.key == pygame.K_UP:
                    lead_y_change =-block_size
                    lead_x_change=0
                    direction="up"
                elif event.key == pygame.K_DOWN:
                    lead_y_change =block_size
                    lead_x_change=0
                    direction="down"
                elif event.key==pygame.K_p:
                    pause()
                
                
                
        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            gameOver=True
                    
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        
# #         if lead_x >= randAppleX and lead_x <= randAppleX+appleThickness:
# #             if leadY>= randAppleY and lead_Y <= randappleY+appleThickness:
# #                 randAppleX=random.randrange(0,display_width-block_size,appleThickness)
# #                 randAppleY=random.randrange(0,display_height-block_size,appleThickness)
# #                 snakeLenght+=1
        if lead_x + block_size > randAppleX and lead_x < randAppleX + appleThickness:
            if lead_y + block_size > randAppleY and lead_y < randAppleY + appleThickness:
                randAppleX=random.randrange(0,display_width-appleThickness,appleThickness)
                randAppleY=random.randrange(0,display_height-appleThickness,appleThickness)
                snakeLenght+=1
                
            
        gameDisplay.fill(white)
        ##pygame.draw.rect(gameDisplay,red,[randAppleX, randAppleY, appleThickness,appleThickness])
        gameDisplay.blit(appleimg,[randAppleX, randAppleY])
        
        
        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList)>snakeLenght:
            del snakeList[0]
        
        for eachSegment in snakeList[:-1]:
            if eachSegment==snakeHead:
                gameOver=True
        
        snake(block_size,snakeList)
        score(snakeLenght-1)
        
        pygame.display.update()
        
        clock.tick(FPS)
                
    pygame.quit()
    quit()
game_intro()
gameLoop()
        
