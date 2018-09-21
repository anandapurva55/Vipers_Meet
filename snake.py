import pygame
import time
import random
import cx_Freeze


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0,128,0)
brown = (120,58,58)
purple = (128, 0 ,128)
grey = (125,125,125)
dred = (139,0,0)
aquamarine = (127,255,212)
display_width = 800
display_height = 600

gameScreen = pygame.display.set_mode((display_width, display_height))


gameClose = False


clock = pygame.time.Clock()

block_size = 20
FPS = 15

direction = 'right'

pygame.display.set_caption("Vipers Meet")
icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

img = pygame.image.load('snake1.jpg')
apple = pygame.image.load("apple.png")

def text_objects(text,color , size):
     if size == 'small':
         textSurface  = smallfont.render(text , True ,color)
     elif size == 'medium':
         textSurface = mediumfont.render(text , True , color)

     elif size == 'large':
         textSurface = largefont.render(text ,True ,color )



     return textSurface , textSurface.get_rect()


def message_to_screen(msg, color, y_displace = 0 , size = "small"):

    textSurf , textRect = text_objects(msg,color,size)


    textRect.center = (display_width/2) , (display_height/2) + y_displace
    gameScreen.blit(textSurf , textRect)

font = pygame.font.SysFont(None , 25)
smallfont = pygame.font.SysFont("Comicsansms", 25)
mediumfont = pygame.font.SysFont("Comicsansms", 40)
largefont = pygame.font.SysFont("Comicsansms", 80)



def gameintro():
    intro = True
    while True:

        gameScreen.fill(grey)
        message_to_screen("Vipers Meet",black, -200 , size = "large")
        message_to_screen("Rule:-",dred,-120,"medium")
        message_to_screen("You should eat apple to earn points",black ,-80) #small is by default
        message_to_screen("If you run into yourself or on the edges,you die",black,-50,"small")
        message_to_screen("About the developer:",red,0,"medium")
        message_to_screen("Apurva Anand: a lonely seeker of truth swimming in this material pool",black,40,)
        message_to_screen("Press S to play game and Q to quit",black,180)
        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    intro = False
                    gameloop()
                if event.type == pygame.K_q:
                    pygame.quit()

def score(score) :
    text = smallfont.render("Score : "+str(score) , True,black)
    gameScreen.blit(text,[0,0])

def our_snake(block_size , snakeList):

    if direction == 'right':
        head = pygame.transform.rotate(img ,270 )
    if direction == 'left':
        head = pygame.transform.rotate(img , 90)

    if direction == 'up':
        head = img

    if direction == 'down':
        head = pygame.transform.rotate(img, 180)
    gameScreen.blit(head , (snakeList[-1][0] , snakeList[-1][1]))

    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameScreen,brown,[XnY[0],XnY[1],block_size,block_size])


def gameloop():
    global m
    FPS = 5
    global direction
    global head
    gameClose = False
    gameOver = False
    snakeList = []
    snakeLength = 1

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 10
    lead_y_change = 0

    randAppleX = round(random.randrange(0 , display_width - 20)/10.0)*10.0
    randAppleY = round(random.randrange(0 , display_height-27)/10.0)*10.0


    while not gameClose:

        while gameOver == True:
            gameScreen.fill(dred)
            if m == 0:
                message_to_screen("Final Score is 0 !", aquamarine, -50, "medium")
            else:
                message_to_screen("Final Score is "+str(m)+" !",aquamarine,-50,"medium")
            message_to_screen("Game Over",black,-200 , size = "large")
            message_to_screen("Press S to play again or Q to quit" , black,50,size = "medium")



            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameClose = True

                    if event.key == pygame.K_s:

                        gameloop()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction ='left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction ='up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
               gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameScreen.fill(white)

        AppleThickness=  30
        #pygame.draw.rect(gameScreen,red,(randAppleX,randAppleY,27,20))
        gameScreen.blit(apple,(randAppleX,randAppleY,20,20))
        #pygame.draw.rect(gameScreen, green, (lead_x, lead_y, 10,10))
        #pygame.display.update()

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]


        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        our_snake(block_size, snakeList)

        score(10*snakeLength-10)
        m = 10*snakeLength-10

        pygame.display.update()



        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                randAppleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                snakeLength += 1
                FPS = FPS + 2
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                randAppleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                snakeLength += 1
                FPS = FPS + 2

        clock.tick(FPS)


    pygame.quit()
    quit()

gameintro()
gameloop()


