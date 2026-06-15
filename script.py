from email.mime import text
from fileinput import close

import  pygame
import sys
from pygame import color
from pygame import font
from pygame.constants import QUIT
from pygame.examples.music_drop_fade import screen
import random


x= pygame.init()
window= pygame.display.set_mode((600, 600))
pygame.display.set_caption("My first game")



def scoreshow(score,color,window,size):
   font=pygame.font.Font(None,25)
   text=font.render(score,True,color)
   window.blit(text,(5,5))
   pygame.display.update()

def scoreshoww(score,color,window,size):
   font=pygame.font.Font(None,25)
   text=font.render(score,True,color)
   window.blit(text,(150,300))
   pygame.display.update()


def snakeplot(snklist,window,color,size):
    for x,y in snklist:
        pygame.draw.rect(window,color,(x,y,size,size))


#game variables



def foodgen(window,color,x,y,WIDTH,HEIGHT):
    pygame.draw.rect(window,color,(x,y,WIDTH,HEIGHT))
close = False

def gameloop():

    #game variables

    velocity_x = 5
    velocity_y = 5
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    gameover = False
    x = 255
    y = 255
    fps = 30
    width = 20
    height = 20
    food_x: int = random.randint(20, 550)
    food_y = random.randint(20, 550)
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
    score = 0
    snklist = []
    snklen = 1
    close = False

    with open("hiscore.txt","r") as f:
        hiscore=f.read()

    # gameloop



    while not close:
        if gameover:

            window.fill(WHITE)
            i=scoreshoww("Your Have scored: "+str(score)+" Press Enter to restart", RED, window, 20)
            pygame.display.update(i)
            for event in pygame.event.get():


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameover = False
                        close=False
                        score = 0
                        return




                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()











        for event in pygame.event.get():








            if not gameover:
                  if event.type==pygame.KEYDOWN:

                        if event.key == pygame.K_SPACE:
                           score = int(score) + 50


                        if event.key==pygame.K_RIGHT:
                          velocity_x=5
                          velocity_y=0

                        if event.key == pygame.K_LEFT:

                           velocity_x=-5
                           velocity_y=0

                        if event.key == pygame.K_DOWN:
                           velocity_y=5
                           velocity_x=0

                        if event.key == pygame.K_UP:
                            velocity_y = -5
                            velocity_x = 0

                  if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()



























        if x < 0 or x > 600 or y < 0 or y > 600:
            gameover = True


        if snklist:
            if head in snklist[:-1]:
                gameover = True

        if abs(food_x-x)<10 and abs(food_y-y)<10:
            food_x = random.randint(20, 550)
            food_y = random.randint(20, 550)
            score+=10
            snklen+=5



        if len(snklist) > snklen:
            del snklist[0]



        if int(hiscore)<score:
            hiscore=score
            with open("hiscore.txt","w") as f:
                f.write(str(hiscore))





        head = []
        head.append(x)
        head.append(y)
        snklist.append(head)

        pygame.display.update()
        clock.tick(fps)

        window.fill(BLUE)
        x = x + velocity_x
        y = y + velocity_y

        scoreshow("Score: " + str(score)+" Hiscore:" +str(hiscore), RED, window, 5)
        snakeplot(snklist, window, WHITE, 20)

        if x<0 or x>600 or y<0 or y>600:
            gameover=True










        foodgen(window,RED,food_x,food_y,width,height)








while True:
    gameloop()
