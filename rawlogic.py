import time
import numpy as np
import sys
import pokedex
import random

def delay(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self,name,types,moves,EVs,health=100):
        self.name = name
        self.types = types
        self.moves = moves
        self.att = EVs['ATTACK']
        self.defn = EVs['DEFENCE']
        self.hp = 20
        self.health = health

    def fight(self,Pokemon2):
        global str1,str2
        print('-------BATTLE-------')
        print(f"\n{self.name}")
        print("TYPE/",self.types)
        print("ATTACK/",self.att)
        print("DEFENCE/",self.defn)
        print("LVL/",round(3*(1+np.mean([self.att,self.defn]))))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/",Pokemon2.types)
        print("ATTACK/",Pokemon2.att)
        print("DEFENCE/",Pokemon2.defn)
        print("LVL/",round(3*(1+np.mean([Pokemon2.att,Pokemon2.defn]))))

        time.sleep(2)

        kind = ['Normal','Fire','Water','Electric','Grass','Ice','Fighting','Poison','Ground','Flying','Psychic','Bug','Rock','Ghost','Dragon','Dark','Steel']
        #Normal
        if self.types == kind[0]:
            if Pokemon2.types in ['Rock','Steel']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
                
            
            elif Pokemon2.types == 'Ghost':
                self.att *= 0
                Pokemon2.att *= 0
                str1 = "\nIt's immune..."
                str2 = "\nIt's immune..."
            
            elif Pokemon2.types == 'Fighting':
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"
            
            else:
                str1 = '\n...'
                str2 = '\n...'
        
        #Fire
        elif self.types == kind[1]:
            if Pokemon2.types in ['Fire']:
                self.att /= 2
                Pokemon2.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Dragon']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Rock','Water']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types == 'Ground':
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Grass','Ice','Bug','Steel']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            else:
                str1 = '\n...'
                str2 = '\n...'

        #Water
        elif self.types == kind[2]:
            if Pokemon2.types in ['Water']:
                self.att /= 2
                Pokemon2.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Dragon']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n'
            
            elif Pokemon2.types in ['Grass']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types == 'Electric':
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Rock','Ground']:
                self.att *= 2
                str1 = "\nIt's super effective!"
                str2 = '\n...'

            elif Pokemon2.types in ['Fire']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Ice','Steel']:
                Pokemon2.att /= 2
                str1 = '\n...'
                str2 = "\nIt's not very effective..."

            else:
                str1 = '\n...'
                str2 = '\n...'
            
        #Electric
        elif self.types == kind[3]:
            if Pokemon2.types in ['Electric']:
                self.att /= 2
                Pokemon2.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Dragon','Grass']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Ground']:
                self.att *= 0
                Pokemon2.att *= 2
                str1 = "\nIt's immune..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Water']:
                self.att *= 2
                str1 = "\nIt's super effective!"
                str2 = '\n...'

            elif Pokemon2.types in ['Flying']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Steel']:
                Pokemon2.att /= 2
                str1 = '\n...'
                str2 = "\nIt's not very effective..."

            else:
                str1 = '\n...'
                str2 = '\n...'

        #Grass
        elif self.types == kind[4]:
            if Pokemon2.types in ['Grass']:
                self.att /= 2
                Pokemon2.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Dragon','Steel']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Fire','Poison','Flying','Bug']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types == 'Ice':
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Rock']:
                self.att *= 2
                str1 = "\nIt's super effective!"
                str2 = '\n...'

            elif Pokemon2.types in ['Water','Ground']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Electric']:
                Pokemon2.att /= 2
                str1 = '\n...'
                str2 = "\nIt's not very effective..."

            else:
                str1 = '\n...'
                str2 = '\n...'

        #Ice
        elif self.types == kind[5]:
            if Pokemon2.types in ['Ice']:
                self.att /= 2
                Pokemon2.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Water']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Fire','Steel']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Fighting','Rock']:
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Grass','Ground','Flying','Dragon']:
                self.att *= 2
                str1 = "\nIt's super effective!"
                str2 = '\n...'

            else:
                str1 = '\n...'
                str2 = '\n...'

        #Fighting
        elif self.types == kind[6]:
            if Pokemon2.types in ['Bug']:
                self.att /= 2
                Pokemon2.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Poison']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Flying','Psychic']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Normal','Ice','Steel']:
                self.att *= 2
                str1 = "\nIt's super effective!"
                str2 = '\n...'

            elif Pokemon2.types in ['Rock','Dark']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types == 'Ghost':
                self.att *= 0
                str1 = "\nIt's immune..."
                str2 = '\n...'

            else:
                str1 = '\n...'
                str2 = '\n...'

        #Poison
        elif self.types == kind[7]:
            if Pokemon2.types in ['Poison']:
                self.att /= 2
                Pokemon2.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Rock','Ghost']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Ground']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types == 'Psychic':
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Grass']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Steel']:
                self.att *= 0
                str1 = "\nIt's immune..."
                str2 = "\n..."
            
            elif Pokemon2.types == 'Fighting':
                Pokemon2.att /= 2
                str1 = '\n...'
                str2 = "\nIt's not very effective..."
            
            else:
                str1 = '\n...'
                str2 = '\n...'

        #Ground
        elif self.types == kind[8]:
            if Pokemon2.types in ['Bug']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Grass']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Water','Ice']:
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Fire','Steel']:
                self.att *= 2
                str1 = "\nIt's super effective!"
                str2 = '\n...'

            elif Pokemon2.types in ['Poison','Rock']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types == 'Electric':
                self.att *= 2
                Pokemon2.att *= 0
                str1 = "\nIt's super effective!"
                str2 = "\nIt's immune..."

            elif Pokemon2.types == 'Flying':
                self.att *= 0
                str1 = "\nIt's immune..."
                str2 = '\n...'

            else:
                str1 = '\n...'
                str2 = '\n...'

        #Flying
        elif self.types == kind[9]:
            if Pokemon2.types in ['Steel']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Electric','Rock']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types == 'Ice':
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Grass','Fighting','Bug']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Ground']:
                Pokemon2.att *= 0
                str1 = '\n...'
                str2 = "\nIt's immune..."

            else:
                str1 = '\n...'
                str2 = '\n...'
        
        #Psychic
        elif self.types == kind[10]:
            if Pokemon2.types in ['Psychic']:
                self.att /= 2
                Pokemon2.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Steel']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'

            elif Pokemon2.types in ['Ghost','Bug']:
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Poison']:
                self.att *= 2
                str1 = "\nIt's super effective!"
                str2 = '\n...'

            elif Pokemon2.types in ['Fighting']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Dark']:
                self.att *= 0
                Pokemon2.att *= 2
                str1 = "\nIt's immune..."
                str2 = "\nIt's super effective!"

            else:
                str1 = '\n...'
                str2 = '\n...'

        #Bug
        elif self.types == kind[11]:
            if Pokemon2.types in ['Fighting']:
                self.att /= 2
                Pokemon2.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Ghost','Steel']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Fire','Flying']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types == 'Rock':
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Psychic','Dark']:
                self.att *= 2
                str1 = "\nIt's super effective!"
                str2 = '\n...'

            elif Pokemon2.types in ['Grass']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Ground']:
                Pokemon2.att /= 2
                str1 = '\n...'
                str2 = "\nIt's not very effective..."

            else:
                str1 = '\n...'
                str2 = '\n...'
        
        #Rock
        elif self.types == kind[12]:
            if Pokemon2.types in ['Fighting','Ground','Steel']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Water','Grass']:
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Bug','Ice']:
                self.att *= 2
                str1 = "\nIt's super effective!"
                str2 = '\n...'

            elif Pokemon2.types in ['Fire','Flying']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Normal','Poison']:
                Pokemon2.att /= 2
                str1 = '\n...'
                str2 = "\nIt's not very effective..."

            else:
                str1 = '\n...'
                str2 = '\n...'
        
        #Ghost
        elif self.types == kind[13]:
            if Pokemon2.types in ['Steel']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Dark']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types == 'Ghost':
                self.att *= 2
                Pokemon2.att *= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Psychic']:
                self.att *= 2
                str1 = "\nIt's super effective!"
                str2 = '\n...'

            elif Pokemon2.types in ['Normal']:
                self.att *= 0
                Pokemon2.att *= 0
                str1 = "\nIt's immune..."
                str2 = "\nIt's immune..."

            elif Pokemon2.types == 'Fighting':
                Pokemon2.att *= 0
                str1 = '\n...'
                str2 = "\nIt's immune..."

            elif Pokemon2.types in ['Poison','Bug']:
                Pokemon2.att /= 2
                str1 = '\n...'
                str2 = "\nIt's not very effective..."

            else:
                str1 = '\n...'
                str2 = '\n...'
        
        #Dragon
        elif self.types == kind[14]:
            if Pokemon2.types in ['Dragon']:
                self.att *= 2
                Pokemon2.att *= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Steel']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'


            elif Pokemon2.types == 'Ice':
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"


            elif Pokemon2.types in ['Fire','Water','Electric','Grass']:
                Pokemon2.att /= 2
                str1 = '\n...'
                str2 = "\nIt's not very effective..."

            else:
                str1 = '\n...'
                str2 = '\n...'
        
        #Dark
        elif self.types == kind[15]:
            if Pokemon2.types in ['Dark']:
                self.att /= 2
                Pokemon2.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Steel']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Fighting']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types == 'Bug':
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Ghost']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Psychic']:
                self.att *= 2
                Pokemon2.att *= 0
                str1 = "\nIt's super effective!"
                str2 = "\nIt's immune..."

            else:
                str1 = '\n...'
                str2 = '\n...'
        
        #Steel
        elif self.types == kind[16]:
            if Pokemon2.types in ['Steel']:
                self.att /= 2
                Pokemon2.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Electric','Water']:
                self.att /= 2
                str1 = "\nIt's not very effective..."
                str2 = '\n...'
            
            elif Pokemon2.types in ['Fire']:
                self.att /= 2
                Pokemon2.att *= 2
                str1 = "\nIt's not very effective..."
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Fighting','Ground']:
                Pokemon2.att *= 2
                str1 = '\n...'
                str2 = "\nIt's super effective!"

            elif Pokemon2.types in ['Ice','Rock']:
                self.att *= 2
                Pokemon2.att /= 2
                str1 = "\nIt's super effective!"
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types in ['Normal','Grass','Flying','Psychic','Bug','Ghost','Dragon','Dark']:
                Pokemon2.att /= 2
                str1 = '\n...'
                str2 = "\nIt's not very effective..."

            elif Pokemon2.types == 'Poison':
                Pokemon2.att *= 0
                str1 = '\n...'
                str2 = "\nIt's immune..."

            else:
                str1 = '\n...'
                str2 = '\n...'
        
        
def oneplayer(self,Pokemon2):
    global str1,str2
    while (self.hp > 0) and (Pokemon2.hp > 0):
        print(f"\n{self.name}\t\tHP\t{self.health}\n")
        print(f"{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n")

        #User's Turn
        print(f"Go {self.name}!")

        for i,k in enumerate(self.moves):
            print(f"{i+1}.",k)
        
        mov = int(input("Pick a move: "))
        while mov not in [1,2,3,4]:
            mov = int(input("Pick a valid move number: "))
        delay(f"{self.name} used {self.moves[mov-1]}!")

        time.sleep(1)

        delay(str1)

        Pokemon2.hp -= self.att//2
        Pokemon2.health = -100

        for j in range(int(Pokemon2.hp+0.1*Pokemon2.defn)):
            Pokemon2.health += 10

        time.sleep(1)
        
        if self.health>=0:
            print(f"\n{self.name}\t\tHP\t{self.health}\n")
        else:
            print(f"\n{self.name}\t\tHP\t0\n")
            print(f"\n{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n")
            delay(self.name+' has fainted ...')
            break
        if Pokemon2.health>=0:
            print(f"\n{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n")
        else:
            print(f"\n{self.name}\t\tHP\t{self.health}\n")
            print(f"\n{Pokemon2.name}\t\tHP\t0\n")
            delay(Pokemon2.name+' has fainted ...')
            break

        time.sleep(0.5)




        #Pokemon 2's Turn
        print(f"Go {Pokemon2.name}!")

        for i,k in enumerate(Pokemon2.moves):
            print(f"{i+1}.",k)
        
        mov = random.randint(1,4)
        while mov not in [1,2,3,4]:
            mov = int(input("Pick a valid move number: "))
        delay(f"{Pokemon2.name} used {Pokemon2.moves[mov-1]}!")

        time.sleep(1)

        delay(str2)

        self.hp -= Pokemon2.att//2
        self.health = -100

        for j in range(int(self.hp+0.1*self.defn)):
            self.health += 10

        time.sleep(1)
        
        if self.health>=0:
            print(f"\n{self.name}\t\tHP\t{self.health}\n")
        else:
            print(f"\n{self.name}\t\tHP\t0\n")
            print(f"\n{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n")
            delay(self.name+' has fainted ...')
            break
        if Pokemon2.health>=0:
            print(f"\n{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n")
        else:
            print(f"\n{self.name}\t\tHP\t{self.health}\n")
            print(f"\n{Pokemon2.name}\t\tHP\t0\n")
            delay(Pokemon2.name+' has fainted ...')
            break

        time.sleep(0.5)

        
    money = np.random.choice(10000)
    delay(f"\nOpponent paid you {money}!\n")
    
def twoplayer(self,Pokemon2):
    global str1,str2
    while (self.hp > 0) and (Pokemon2.hp > 0):
        print(f"\n{self.name}\t\tHP\t{self.health}\n")
        print(f"{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n")

        #User's Turn
        print(f"Go {self.name}!")

        for i,k in enumerate(self.moves):
            print(f"{i+1}.",k)
        
        mov = int(input("Pick a move: "))
        while mov not in [1,2,3,4]:
            mov = int(input("Pick a valid move number: "))
        delay(f"{self.name} used {self.moves[mov-1]}!")

        time.sleep(1)

        delay(str1)

        Pokemon2.hp -= self.att//2
        Pokemon2.health = -100

        for j in range(int(Pokemon2.hp+0.1*Pokemon2.defn)):
            Pokemon2.health += 10

        time.sleep(1)
        
        if self.health>=0:
            print(f"\n{self.name}\t\tHP\t{self.health}\n")
        else:
            print(f"\n{self.name}\t\tHP\t0\n")
            print(f"\n{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n")
            delay(self.name+' has fainted ...')
            break
        if Pokemon2.health>=0:
            print(f"\n{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n")
        else:
            print(f"\n{self.name}\t\tHP\t{self.health}\n")
            print(f"\n{Pokemon2.name}\t\tHP\t0\n")
            delay(Pokemon2.name+' has fainted ...')
            break

        time.sleep(0.5)




        #Pokemon 2's Turn
        print(f"Go {Pokemon2.name}!")

        for i,k in enumerate(Pokemon2.moves):
            print(f"{i+1}.",k)
        
        mov = int(input("Pick a move: "))
        while mov not in [1,2,3,4]:
            mov = int(input("Pick a valid move number: "))
        delay(f"{Pokemon2.name} used {Pokemon2.moves[mov-1]}!")

        time.sleep(1)

        delay(str2)

        self.hp -= Pokemon2.att//2
        self.health = -100

        for j in range(int(self.hp+0.1*self.defn)):
            self.health += 10

        time.sleep(1)
        
        if self.health>=0:
            print(f"\n{self.name}\t\tHP\t{self.health}\n")
        else:
            print(f"\n{self.name}\t\tHP\t0\n")
            print(f"\n{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n")
            delay(self.name+' has fainted ...')
            break
        if Pokemon2.health>=0:
            print(f"\n{Pokemon2.name}\t\tHP\t{Pokemon2.health}\n")
        else:
            print(f"\n{self.name}\t\tHP\t{self.health}\n")
            print(f"\n{Pokemon2.name}\t\tHP\t0\n")
            delay(Pokemon2.name+' has fainted ...')
            break

        time.sleep(0.5)

        
    money = np.random.choice(10000)
    delay(f"\nOpponent paid you {money}!\n")



if __name__ == '__main__':
    Charizard = Pokemon('Charizard','Fire',['Flamethrower','Fly','Blast Burn','Fire Punch'],{'ATTACK':12,'DEFENCE':18})
    Blastoise = Pokemon('Blastoise','Water',['Water Pulse','Surf','Hydro Pump','Bubble Beam'],{'ATTACK':10,'DEFENCE':10})
    Venusaur = Pokemon('Venusaur','Grass',['Vine Whip','Razor Leaf','Magical Leaf','Stomp'],{'ATTACK':8,'DEFENCE':12})

    l = [Charizard,Blastoise,Venusaur]
    p1 = np.random.choice(l)
    p2 = np.random.choice(l)
    while p1 == p2:
        p1 = np.random.choice(l)
    p1.fight(p2)
    
while True:
    x=input('One player or 2 player mode? 3 to exit')
    if x=='1':
        oneplayer(p1,p2)
        break
    elif x=='2':
        twoplayer(p1,p2)
        break
    elif x=='3':
        break
    else:
        print('invalid input')
        