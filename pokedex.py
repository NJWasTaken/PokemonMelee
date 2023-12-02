types = ['Fire', 'Water', 'Grass', 'Electric', 'Flying', 'Psychic', 'Fighting', 'Rock', 'Poison', 'Bug', 'Ground', 'Ice', 'Normal', 'Dragon', 'Ghost']

#parent class
class poketype:
    
  def __init__(self, name, strength, weakness, null):
    reg = list(filter(lambda x:x not in strength+weakness+null,types))
    self.name = name
    #These values are with respect to damage done to the opponent
    self.strength = strength #2x damage 
    self.weakness = weakness #1/2x damage 
    self.null = null #0 damage 
    
  def regular(self):
    reg = list(filter(lambda x:x not in self.strength+self.weakness+self.null,types))
    self.reg = reg #1x damage
    return self.reg
  
#child classes

class Normal(poketype):
  name = 'Normal'
  strength = []
  weakness = ['Rock']
  null = ['Ghost']

class Fire(poketype):
  name = 'Fire'
  strength = ['Bug', 'Grass', 'Ice']
  weakness = ['Fire', 'Rock', 'Water', 'Dragon']
  null = []

class Water(poketype):
  name = 'Water'
  strength = ['Fire', 'Ground', 'Rock']
  weakness = ['Water', 'Grass', 'Dragon']
  null = []

class Electric(poketype):
  name = 'Electric'
  strength = ['Flying', 'Water']
  weakness = ['Electric','Grass','Dragon']
  null = ['Ground']

class Grass(poketype):
  name = 'Grass'
  strength = ['Ground', 'Rock', 'Water']
  weakness = ['Bug', 'Fire', 'Flying', 'Dragon', 'Poison', 'Grass']
  null = [] 

class Ice(poketype):
  name = 'Ice'
  strength = ['Dragon', 'Flying', 'Grass', 'Ground']
  weakness = ['Water', 'Ice']
  null = []

class Fighting(poketype):
  name = 'Fighting'
  strength = ['Ice', 'Normal', 'Rock']
  weakness = ['Poison', 'Flying', 'Psychic', 'Bug']
  null = ['Ghost']

class Poison(poketype):
  name = 'Poison'
  strength = ['Bug', 'Grass']
  weakness = ['Poison', 'Ground', 'Rock','Ghost']
  null = []

class Ground(poketype):
  name = 'Ground'
  strength = ['Electric', 'Fire', 'Poison', 'Rock']
  weakness = ['Grass', 'Bug']
  null = ['Flying']

class Flying(poketype):
  name = 'Flying'
  strength = ['Bug', 'Fighting', 'Grass']
  weakness = ['Electric', 'Rock']
  null = []

class Psychic(poketype):
  name = 'Psychic'
  strength = ['Fighting', 'Poison']
  weakness = ['Psychic']
  null = []

class Bug(poketype):
  name = 'Bug'
  strength = ['Grass', 'Poison', 'Psychic']
  weakness = ['Fire', 'Fighting','Flying', 'Ghost']
  null = []

class Rock(poketype):
  name = 'Rock'
  strength = ['Bug', 'Fire', 'Flying', 'Ice']
  weakness = ['Fighting', 'Ground']
  null = []

class Ghost(poketype):
  name = 'Ghost'
  strength = ['Ghost']
  weakness = []
  null = ['Normal','Psychic']

class Dragon(poketype):
  name = 'Dragon'
  strength = ['Dragon']
  weakness = []
  null = []

bulbasaur=Grass
ivysaur=Grass
venusaur=Grass
charmander=Fire
charmeleon=Fire
charizard=Fire
squirtle=Water
wartortle=Water
blastoise=Water
caterpie=Bug
metapod=Bug
butterfree=Bug
weedle=Bug
kakuna=Bug
beedrill=Bug
pidgey=Normal
pidgeotto=Normal
pidgeot=Normal
rattata=Normal
raticate=Normal
spearow=Normal
fearow=Normal
ekans=Poison
arbok=Poison
pikachu=Electric
raichu=Electric
sandshrew=Ground
sandslash=Ground
nidoran_f=Poison
nidorina=Poison
nidoqueen=Poison
nidoran_m=Poison
nidorino=Poison
nidoking=Poison
clefairy=Normal
clefable=Normal
vulpix=Fire
ninetales=Fire
jigglypuff=Normal
wigglytuff=Normal
zubat=Poison
golbat=Poison
oddish=Grass
gloom=Grass
vileplume=Grass
paras=Bug
parasect=Bug
venonat=Bug
venomoth=Bug
diglett=Ground
dugtrio=Ground
meowth=Normal
persian=Normal
psyduck=Water
golduck=Water
mankey=Fighting
primeape=Fighting
growlithe=Fire
arcanine=Fire
poliwag=Water
poliwhirl=Water
poliwrath=Water
abra=Psychic
kadabra=Psychic
alakazam=Psychic
machop=Fighting
machoke=Fighting
machamp=Fighting
bellsprout=Grass
weepinbell=Grass
victreebel=Grass
tentacool=Water
tentacruel=Water
geodude=Rock
graveler=Rock
golem=Rock
ponyta=Fire
rapidash=Fire
slowpoke=Water
slowbro=Water
magnemite=Electric
magneton=Electric
farfetchd=Normal
doduo=Normal
dodrio=Normal
seel=Water
dewgong=Water
grimer=Poison
muk=Poison
shellder=Water
cloyster=Water
gastly=Ghost
haunter=Ghost
gengar=Ghost
onix=Rock
drowzee=Psychic
hypno=Psychic
krabby=Water
kingler=Water
voltorb=Electric
electrode=Electric
exeggcute=Grass
exeggutor=Grass
cubone=Ground
marowak=Ground
hitmonlee=Fighting
hitmonchan=Fighting
lickitung=Normal
koffing=Poison
weezing=Poison
rhyhorn=Ground
rhydon=Ground
chansey=Normal
tangela=Grass
kangaskhan=Normal
horsea=Water
seadra=Water
goldeen=Water
seaking=Water
staryu=Water
starmie=Water
mr_mime=Psychic
scyther=Bug
jynx=Ice
electabuzz=Electric
magmar=Fire
pinsir=Bug
tauros=Normal
magikarp=Water
gyarados=Water
lapras=Water
ditto=Normal
eevee=Normal
vaporeon=Water
jolteon=Electric
flareon=Fire
porygon=Normal
omanyte=Rock
omastar=Rock
kabuto=Rock
kabutops=Rock
aerodactyl=Rock
snorlax=Normal
articuno=Ice
zapdos=Electric
moltres=Fire
dratini=Dragon
dragonair=Dragon
dragonite=Dragon
mewtwo=Psychic
mew=Psychic

def pokelist():
  l = [bulbasaur,ivysaur,venusaur,charmander,charmeleon,charizard,squirtle,wartortle,blastoise,caterpie,metapod,butterfree,weedle,kakuna,beedrill,pidgey,pidgeotto,pidgeot,rattata,raticate,spearow,fearow,ekans,arbok,pikachu,raichu,sandshrew,sandslash,nidoran_f,nidorina,nidoqueen,nidoran_m,nidorino,nidoking,clefairy,clefable,vulpix,ninetales,jigglypuff,wigglytuff,zubat,golbat,oddish,gloom,vileplume,paras,parasect,venonat,venomoth,diglett,dugtrio,meowth,persian,psyduck,golduck,mankey,primeape,growlithe,arcanine,poliwag,poliwhirl,poliwrath,abra,kadabra,alakazam,machop,machoke,machamp,bellsprout,weepinbell,victreebel,tentacool,tentacruel,geodude,graveler,golem,ponyta,rapidash,slowpoke,slowbro,magnemite,magneton,farfetchd,doduo,dodrio,seel,dewgong,grimer,muk,shellder,cloyster,gastly,haunter,gengar,onix,drowzee,hypno,krabby,kingler,voltorb,electrode,exeggcute,exeggutor,cubone,marowak,hitmonlee,hitmonchan,lickitung,koffing,weezing,rhyhorn,rhydon,chansey,tangela,kangaskhan,horsea,seadra,goldeen,seaking,staryu,starmie,mr_mime,scyther,jynx,electabuzz,magmar,pinsir,tauros,magikarp,gyarados,lapras,ditto,eevee,vaporeon,jolteon,flareon,porygon,omanyte,omastar,kabuto,kabutops,aerodactyl,snorlax,articuno,zapdos,moltres,dratini,dragonair,dragonite,mewtwo,mew]
  return l

# l1 = pokelist()
# print(l1[0].name)
# print(l1[0].strength)
# print(l1[0].weakness)
# print(l1[0].null)
# print(l1[0].regular(l1[0]))