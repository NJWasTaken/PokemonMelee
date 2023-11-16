#Imports
import pygame
import random
import pandas as pd
from pygame.locals import *
import os


#Making sure the program reads the file paths correctly 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Obtaining Pokemon names from the csv
df = pd.read_csv("PokemonData.csv")
df["Path"]=df["Name"]+".png"

#Selecting a random Player Pokemon
r = random.randint(0,150)
pk = df.Path[r]
ptype = df.Types[r]

#Selecting a random Opponent Pokemon
r2 = random.randint(1,151)
oppath=str(r2)+'.png'
optype = df.Types[r2-1]


#Defining chance for the opponent Pokemon to be shiny (rare)
schance = random.randint(1,100)

#Initializing canvas and mixer
pygame.init()
pygame.mixer.init()

#Setting canvas size
width=1050;
height=700
screen = pygame.display.set_mode( (width, height) )

#Loading Player Pokemon images
pkmg = pygame.image.load(os.path.join('assets','player','img_back',pk)).convert()
pkmg = pygame.transform.scale(pkmg,(200,200))

#Loading Opponent Pokemon images
if schance == 42:
    pkmg2 = pygame.image.load(os.path.join('assets','opp','shiny',oppath)).convert_alpha()
else:
    pkmg2 = pygame.image.load(os.path.join('assets','opp','img_front',oppath)).convert_alpha()
pkmg2 = pygame.transform.scale(pkmg2,(200,200))

#Set game speed
fpsClock = pygame.time.Clock()

#Setting variables for the positions of the two Pokemon
pimageX= 190;
pimageY= 360; 
cimageX=580;
cimageY=220;

#Setting variables for game states
# pname = ''
# opname = ''
running = True
hasatt=1
hasstag=1
st=False
pattack=False
path = 'mainmenu'
audio = 'home'
mainscreen = 'startup'
l=[]
lvol=[]

#Volume 
sppath = 'speaker'
vol = 0.5

#Sounds
sel_sound = pygame.mixer.Sound(os.path.join('assets','audio','select.mp3'))

#Buttons
start_b = pygame.image.load(os.path.join('assets','gui','begin.png')).convert_alpha()
start_b = pygame.transform.scale(start_b,(275,100))
options_b = pygame.image.load(os.path.join('assets','gui','options.png')).convert_alpha()
options_b = pygame.transform.scale(options_b,(275,100))
exit_b = pygame.image.load(os.path.join('assets','gui','exit.png')).convert_alpha()
exit_b = pygame.transform.scale(exit_b,(275,100))


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
    bg_img = pygame.image.load(os.path.join('assets','art',mainscreen+'.jpg')).convert()
    bg_img = pygame.transform.scale(bg_img,(width,height))
    gui = pygame.image.load(os.path.join('assets','gui',path+'.png')).convert()
    gui = pygame.transform.scale(gui,(1050, 187))
    speaker = pygame.image.load(os.path.join('assets','audio',sppath+'.png')).convert_alpha()
    speaker = pygame.transform.scale(speaker,(100,100))
    
    #Setting up game music
    if audio not in l:
        l.clear()
        pygame.mixer.music.load(os.path.join('assets','audio',audio+'.mp3'))
        pygame.mixer.music.play(-1)
        l.append(audio) 
    pygame.mixer.music.set_volume(vol)

    screen.fill((0,0,0)) #Base Layer    
    screen.blit(bg_img,[0,0]) #Background Image
    screen.blit(speaker,[900,50]) #Volume
    
    #Homescreen
    if mainscreen == 'startup':
        screen.blit(exit_b,[400,600])
        screen.blit(start_b,[400,300])
        screen.blit(options_b,[400,400])

    #Player attack event
    if pattack == True:
        if st == False:
            pimageX,pimageY,hasatt,st=attan(pimageX,pimageY,hasatt,st)
        else:
            cimageX,cimageY,hasstag,pattack=stagger(cimageX,cimageY,hasstag,pattack)
    
    #Pokemon sprites
    if mainscreen == 'bgimg':
        screen.blit(pkmg2 , [cimageX,cimageY])
        screen.blit(pkmg , [pimageX, pimageY])

    #User events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            #print('x:',x,',y:',y)
            #Homepage
            if mainscreen == 'startup':
                if x in range(405, 645) and y in range(610, 695):
                    pygame.mixer.Sound.play(sel_sound)
                    running = False
                if x in range(405, 645) and y in range(310,390):
                    pygame.mixer.Sound.play(sel_sound)
                    mainscreen = 'bgimg'
                    audio = 'theme'
                    path = 'mainmenu'

            #Volume
            if x in range(900,960) and y in range(70,130):
                if vol == 0:
                    sppath = 'speaker'
                    vol = 0.5
                elif vol == 0.5:
                    pygame.mixer.Sound.play(sel_sound)
                    sppath = 'speakernt'
                    vol = 0

            #Fight
            if path == 'mainmenu' and (x in range(516,778) and y in range(525,610)):
                path = 'fight'
            
            if path == 'fight' and ((x in range(55,400) and y in range(555,606)) or (x in range(415,690) and y in range(555,606)) or (x in range(55,400) and y in range(615,665)) or (x in range(415,690) and y in range(615,665))):
                pygame.mixer.Sound.play(sel_sound)
                pattack = True
                st = False
                hasatt = 1
                hasstag = 1

            #Run
            if path == 'mainmenu' and (x in range(780,1040) and y in range(590,693)):
                path = 'run'

            if path == 'run':
                if (x in range(518,778) and y in range(565,650)):
                    pygame.mixer.Sound.play(sel_sound)
                    mainscreen = 'startup'
                    audio = 'home'
                if (x in range(780,1040) and y in range(565,650)):
                    pygame.mixer.Sound.play(sel_sound)
                    path = 'mainmenu'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if path == 'fight':
                    path = 'mainmenu'
    
    if mainscreen == 'bgimg':
        screen.blit(gui,[0,513])

    pygame.display.update()
    fpsClock.tick(200)
pygame.quit()