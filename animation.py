import pygame
import random
import pandas as pd
from pygame.locals import *
df = pd.read_csv("PokemonData.csv")
df["Path"]=df["Name"]+".png"

df1 = df.loc[:9,["Path"]]
r = random.randint(0,8)

pygame.init()
width=1050;
height=600
pk = df1.Path[r]
screen = pygame.display.set_mode( ( width, height) )
pkmg = pygame.image.load(f"img_back\\{pk}").convert()
pkmg2 = pygame.image.load(f"img_back\\charmeleon.png").convert()
pkmg = pygame.transform.scale(pkmg,(200,200))
fpsClock = pygame.time.Clock()
imageX= 190; # x coordnate of image
imageY= 220; # y coordinate of image
#imageX=560;
#imageY=100;
running = True
black = ( 0 , 0 , 0)
bg_img = pygame.image.load(r'bgimg.jpg').convert()
bg_img = pygame.transform.scale(bg_img,(width,height))

a=1
def attan(x,y,c):
    if x >= 420:
        c=0

    if y<420 and c!=0:
        x += 1 ;
    y = (((x-415)**2)/300)+140 ;
    
    if c==0 and x>190:
        x-=1;
    
    if c==0 and x<=190:
        pass
    return (x,y,c)
while (running): # main game loop
    screen.fill((0,0,0))
    screen.blit(bg_img,[0,0])
    imageX,imageY,a=attan(imageX,imageY,a)
    screen.blit(pkmg , [imageX, imageY]) # paint to screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
    pygame.display.update()
    fpsClock.tick(270)
#loop over, quite pygame
pygame.quit()
