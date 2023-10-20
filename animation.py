import pygame
import random
import pandas as pd
from pygame.locals import *
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("PokemonData.csv")
df["Path"]=df["Name"]+".png"

r = random.randint(0,151)
schance = random.randint(1,100)
r2 = random.randint(1,151)
oppath=str(r2)+'.png'
pygame.init()

width=1050;
height=700

pk = df.Path[r]

screen = pygame.display.set_mode( (width, height) )

pkmg = pygame.image.load(f"assets\\player\\img_back\\{pk}").convert()
pkmg = pygame.transform.scale(pkmg,(200,200))

if schance == 42:
    pkmg2 = pygame.image.load(f"assets\\opp\\shiny\\{oppath}").convert_alpha()
else:
    pkmg2 = pygame.image.load(f"assets\\opp\\img_front\\{oppath}").convert_alpha()
pkmg2 = pygame.transform.scale(pkmg2,(200,200))

fpsClock = pygame.time.Clock()

pimageX= 190;
pimageY= 350; 
cimageX=580;
cimageY=220;

running = True

bg_img = pygame.image.load("assets\\art\\bgimg.jpg").convert()
bg_img = pygame.transform.scale(bg_img,(width,height))
gui = pygame.image.load("assets\gui\mainmenu.png").convert()
gui = pygame.transform.scale(gui,(1050, 187))
a=1
b=1
st=False

def attan(x,y,c,s):
    if x >= 240:
        c=0

    if x<240 and c!=0:
        x += 1 ;
        y -= 0.2

    if c==0 and x>190:
        x-=1;
        y+=0.2
    
    if c==0 and x<=190:
        s = True
    return (x,y,c,s)


def stagger(x,y,c):
    if x >= 610:
        c=0

    if x<610 and c!=0:
        x += 1 ;
        y -= 0.5

    if c==0 and x>580:
        x-=1;
        y+=0.5
    
    if c==0 and x<=580:
        pass
    return (x,y,c)


while (running): 
    screen.fill((0,0,0))
    screen.blit(bg_img,[0,0])
    
    if st == False:
        pimageX,pimageY,a,st=attan(pimageX,pimageY,a,st)
    else:
        cimageX,cimageY,b=stagger(cimageX,cimageY,b)
    screen.blit(pkmg2 , [cimageX,cimageY])
    screen.blit(pkmg , [pimageX, pimageY])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x in range(516,1051):
                pass
    screen.blit(gui,[0,510])
    pygame.display.update()
    fpsClock.tick(300)
pygame.quit()
