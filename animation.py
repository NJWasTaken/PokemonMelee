#Imports
import pygame
import random
import pandas as pd
from pygame.locals import *
import os
import tkinter as tk
from tkinter import *
from tkinter import simpledialog, ttk, messagebox
import functools
import pokedex
from pyvidplayer2 import Video

#Making sure the program reads the file paths correctly 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Obtaining Pokemon names from the csv
df = pd.read_csv("PokemonData.csv")
df["Path"]=df["Name"]+".png"

#Importing the pokedex list from pokedex.py
pokelist = pokedex.pokelist()
#Selecting a random Player Pokemon
r = random.randint(0,150)
pk = df.Path[r]
player_pk = df.Name[r]
ptype = pokelist[r]

#Selecting a random Opponent Pokemon
r2 = random.randint(1,151)
oppath=str(r2)+'.png'
opponent_pk = df.Name[r2-1]
optype = pokelist[r2-1]

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

#Loading battle start animation images and game title
red = pygame.image.load(os.path.join('assets','art','red.jpeg')).convert()
red = pygame.transform.scale(red,(width,height//2))
blue = pygame.image.load(os.path.join('assets','art','blue.jpeg')).convert()
blue = pygame.transform.scale(blue,(width,height//2))
vs_img = pygame.image.load(os.path.join('assets','art','vs.png')).convert_alpha()
vs_img = pygame.transform.scale(vs_img,(256,256))
title = pygame.image.load(os.path.join('assets','art','title.png')).convert_alpha()
title = pygame.transform.scale(title,(550,290))
#Set game speed
fpsClock = pygame.time.Clock()

#Setting up tkinter
root = tk.Tk()
root.iconbitmap(os.path.join('assets','art','icon.ico'))
root.withdraw()

#Setting variables for the positions of the two Pokemon
pimageX= 190;
pimageY= 360; 
cimageX=580;
cimageY=220;

#Setting variables for game states
op = False
pname = 'Red'
opname = 'Blue'
font = pygame.font.Font(None, 32)
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
e = False
r_emoji = str(random.randint(0,9))
r_x =random.randint(0,950) 
r_y =random.randint(0,413)
vs_x1 = -425
vs_x2 = 425
vs_centre = False
anim_start = False
singleplayer = True
video = 0

#Volume 
sppath = 'speaker'
vol = 0.5

#Options
optionmenu = pygame.image.load(os.path.join('assets','gui','optionmenu.png')).convert_alpha()
optionmenu = pygame.transform.scale(optionmenu,(664,313))

#Sounds
sel_sound = pygame.mixer.Sound(os.path.join('assets','audio','select.mp3'))
vid = Video(os.path.join('assets','art','easter_egg.mp4'))

#Buttons
start_b = pygame.image.load(os.path.join('assets','gui','begin.png')).convert_alpha()
start_b = pygame.transform.scale(start_b,(275,100))
options_b = pygame.image.load(os.path.join('assets','gui','options.png')).convert_alpha()
options_b = pygame.transform.scale(options_b,(275,100))
exit_b = pygame.image.load(os.path.join('assets','gui','exit.png')).convert_alpha()
exit_b = pygame.transform.scale(exit_b,(275,100))

#VS Animation
def vs(x1,x2,k):
    if k == False:
        x1+=5
        x2-=5
        if x1 == x2:
            k = True
    if k == True:
        x1+=10
        x2-=10

    return x1,x2,k

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
    
    emoji = pygame.image.load(os.path.join('assets','art',r_emoji+'.png')).convert_alpha()
    emoji = pygame.transform.scale(emoji,(100,100))
    

    #Setting up game music
    if audio not in l:
        l.clear()
        pygame.mixer.music.load(os.path.join('assets','audio',audio+'.mp3'))
        pygame.mixer.music.play(-1)
        l.append(audio) 
    pygame.mixer.music.set_volume(vol)

    screen.fill((0,0,0)) #Base Layer    
    if video != 1:
        screen.blit(bg_img,[0,0]) #Background Image

    if mainscreen != 'black' and video != 1:
        screen.blit(speaker,[900,50]) #Volume
    
    #Homescreen
    if mainscreen == 'startup' and video != 1:
        screen.blit(exit_b,[400,600])
        screen.blit(start_b,[400,350])
        screen.blit(options_b,[400,450])
        screen.blit(title,[240,30])

    if mainscreen == 'black':
        screen.blit(red,[vs_x1, 0])
        screen.blit(blue,[vs_x2,350])

    if op == True and video != 1:
        screen.blit(optionmenu,[200,200])

    if video == 1:
        vid.draw(screen, (0,0),force_draw=False)
        vol = 0


    #VS Animation
    if mainscreen == 'black':
        vs_x1,vs_x2,vs_centre = vs(vs_x1,vs_x2,vs_centre)
        if vs_centre == True:
            screen.blit(vs_img,[400,250])
        if vs_x1 >= 1050:
            mainscreen = 'bgimg'
            path = 'mainmenu'
            vs_centre = False

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
                    if op == False:
                        pygame.mixer.Sound.play(sel_sound)
                        running = False
                if x in range(405, 645) and y in range(360,440):
                    if op == False:
                        pygame.mixer.Sound.play(sel_sound)
                        mainscreen = 'black'
                        audio = 'theme'
                        anim_start = True
            
                if x in range(405, 645) and y in range(461, 535):
                    pygame.mixer.Sound.play(sel_sound)
                    op = True
                
            if op == True:
                if x in range(720,845) and y in range(450,495):
                    pygame.mixer.Sound.play(sel_sound)
                    op = False
                if x in range(235,835) and y in range(245,325):
                    pygame.mixer.Sound.play(sel_sound)
                    pname = simpledialog.askstring(title="Player Name",prompt="What's your name?")
                    if pname == None or pname == ''or functools.reduce(lambda x,y: x+y,list(set(list(pname)))) == ' ':
                        pname = 'Red'
                if x in range(235,835) and y in range(345,425):
                    pygame.mixer.Sound.play(sel_sound)
                    opname = simpledialog.askstring(title="Opponent Name",prompt="What's the opponent's name?")
                    if opname == None or opname == '' or functools.reduce(lambda x,y: x+y,list(set(list(opname)))) == ' ':
                        opname = 'Blue'
                if x in range(200,230) and y in range(200,230):
                    pygame.mixer.Sound.play(sel_sound)
                    video +=1

                if x in range(235,400) and y in range(430,500): #Reset button (Needs to reset health)
                    pygame.mixer.Sound.play(sel_sound)
                    r = random.randint(0,150)
                    pk = df.Path[r]
                    player_pk = df.Name[r]
                    ptype = pokelist[r]

                    r2 = random.randint(1,151)
                    oppath=str(r2)+'.png'
                    opponent_pk = df.Name[r2-1]
                    optype = pokelist[r2-1]

                    schance = random.randint(1,100)
                    pkmg = pygame.image.load(os.path.join('assets','player','img_back',pk)).convert()
                    pkmg = pygame.transform.scale(pkmg,(200,200))

                    if schance == 42:
                        pkmg2 = pygame.image.load(os.path.join('assets','opp','shiny',oppath)).convert_alpha()
                    else:
                        pkmg2 = pygame.image.load(os.path.join('assets','opp','img_front',oppath)).convert_alpha()
                        pkmg2 = pygame.transform.scale(pkmg2,(200,200))

            #Volume
            if x in range(900,960) and y in range(70,130) and mainscreen != 'black':
                if e == False:
                    if vol == 0:
                        sppath = 'speaker'
                        vol = 0.5
                    elif vol == 0.5:
                        pygame.mixer.Sound.play(sel_sound)
                        sppath = 'speakernt'
                        vol = 0

            #Fight
            if path == 'mainmenu' and (x in range(516,778) and y in range(525,610)):
                if e == False:
                    path = 'fight/fight'+pokelist[r].name
            
            if path == f'fight/fight'+pokelist[r].name and ((x in range(55,400) and y in range(555,606)) or (x in range(415,690) and y in range(555,606)) or (x in range(55,400) and y in range(615,665)) or (x in range(415,690) and y in range(615,665))):
                pygame.mixer.Sound.play(sel_sound)
                pattack = True
                st = False
                hasatt = 1
                hasstag = 1

            #Run
            if path == 'mainmenu' and (x in range(780,1040) and y in range(590,693)):
                if e == False:
                    path = 'run'
                    vs_x1 = -1050
                    vs_x2 = 1050
            if path == 'run':
                if (x in range(518,778) and y in range(565,650)):
                    pygame.mixer.Sound.play(sel_sound)
                    mainscreen = 'startup'
                    audio = 'home'
                if (x in range(780,1040) and y in range(565,650)):
                    pygame.mixer.Sound.play(sel_sound)
                    path = 'mainmenu'
            
            #Emote
            if path == 'mainmenu' and (x in range(785,1035) and y in range(525,610)):
                e = True
                r_emoji = str(random.randint(0,9))
                path = 'emojis'
                pygame.mixer.Sound.play(sel_sound)

            if e == True:
                if x in range(r_x,r_x+100) and y in range(r_y,r_y+100):
                    e = False
                    r_emoji = str(random.randint(0,9)) 
                    path = 'mainmenu'
                    r_x =random.randint(0,950) 
                    r_y =random.randint(0,600)
                    pygame.mixer.Sound.play(sel_sound)

            #Scan
            if path == 'mainmenu' and (x in range(516,778) and y in range(590,693)):
                pygame.mixer.Sound.play(sel_sound)
                messagebox.showinfo("Battle Stats",f"Player: {pname} \nPlayer Pokemon: {player_pk.capitalize()} \n\nOpponent: {opname} \nOpponent Pokemon: {opponent_pk.capitalize()}")
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if path == 'fight/fight'+pokelist[r].name:
                    path = 'mainmenu'

                if path == 'emojis':
                    e = False
                    r_emoji = str(random.randint(0,9)) 
                    path = 'mainmenu'
                    r_x =random.randint(0,950) 
                    r_y =random.randint(0,600)
                    pygame.mixer.Sound.play(sel_sound)
                
                if mainscreen == 'black':
                    vs_x1 += 2000
                    vs_x2 -= 2000
                
                if video == 1:
                    video += 1
                    vol = 0.5

    #Battle Bg
    if mainscreen == 'bgimg':
        screen.blit(gui,[0,513])
    #Emotes
    if e == True:
        screen.blit(emoji , [r_x,r_y])
    
    pygame.display.update()
    fpsClock.tick(200)
pygame.quit()
