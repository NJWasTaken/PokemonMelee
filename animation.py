#Imports
import pygame
import random
import pandas as pd
from pygame.locals import *
import os
import threading

tevent = threading.Event()

#Making sure the program reads the file paths correctly
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Obtaining Pokemon names from the csv
df = pd.read_csv("PokemonData.csv")
df["Path"]=df["Name"]+".png"

#Selecting a random Player Pokemon
r = random.randint(0,150)
pk = df.Path[r]

#Selecting a random Opponent Pokemon
r2 = random.randint(1,151)
oppath=str(r2)+'.png'

#Defining chance for the opponent Pokemon to be shiny (rare)
schance = random.randint(1,100)

#Creating canvas
pygame.init()

#Setting canvas size
width=1050;
height=700
screen = pygame.display.set_mode( (width, height) )

#Loading Player Pokemon images
pkmg = pygame.image.load(f"assets\\player\\img_back\\{pk}").convert()
pkmg = pygame.transform.scale(pkmg,(200,200))

#Loading Opponent Pokemon images
if schance == 42:
    pkmg2 = pygame.image.load(f"assets\\opp\\shiny\\{oppath}").convert_alpha()
else:
    pkmg2 = pygame.image.load(f"assets\\opp\\img_front\\{oppath}").convert_alpha()
pkmg2 = pygame.transform.scale(pkmg2,(200,200))

#Set game speed
fpsClock = pygame.time.Clock()

#Setting variables for the positions of the two Pokemon
pimageX= 190;
pimageY= 360; 
cimageX=580;
cimageY=220;

#Loading in background image
bg_img = pygame.image.load("assets\\art\\bgimg.jpg").convert()
bg_img = pygame.transform.scale(bg_img,(width,height))

#Setting variables for game states
running = True
hasatt=1
hasstag=1
st=False
pattack=False
path = 'mainmenu'

#Player Pokemon attack animation
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

#Opponent Pokemon stagger animation
def stagger(x,y,c,p):
    if x >= 610:
        c=0

    if x<610 and c!=0:
        x += 1 ;
        y -= 0.5

    if c==0 and x>580:
        x-=1;
        y+=0.5
    
    if c==0 and x<=580:
        p = False
    return (x,y,c,p)

#Main Loop
while (running):
    gui = pygame.image.load(f"assets\gui\{path}.png").convert()
    gui = pygame.transform.scale(gui,(1050, 187))

    screen.fill((0,0,0)) #Base Layer
    screen.blit(bg_img,[0,0]) #Background Image
    
    #Player attack event
    if pattack == True:
        if st == False:
            pimageX,pimageY,hasatt,st=attan(pimageX,pimageY,hasatt,st)
        else:
            cimageX,cimageY,hasstag,pattack=stagger(cimageX,cimageY,hasstag,pattack)
    screen.blit(pkmg2 , [cimageX,cimageY])
    screen.blit(pkmg , [pimageX, pimageY])

    #User events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            #Fight
            if path == 'mainmenu' and (x in range(516,778) and y in range(525,610)):
                pattack = True
                st = False
                hasatt = 1
                hasstag = 1

            #Run
            if path == 'mainmenu' and (x in range(780,1040) and y in range(611,693)):
                path = 'run'

            if path == 'run':
                if (x in range(518,778) and y in range(565,650)):
                    running = False
                if (x in range(780,1040) and y in range(565,650)):
                    path = 'mainmenu'
                
    screen.blit(gui,[0,513])
    pygame.display.update()
    fpsClock.tick(200)
pygame.quit()
