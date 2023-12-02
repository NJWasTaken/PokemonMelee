import csv

class Pokemon:
    def __init__(self, name, types, moves, EVs, health=100):
        self.name = name
        self.types = types
        self.att = int(EVs['ATTACK']) if 'ATTACK' in EVs else 0  # Convert to int with a default value
        self.defn = int(EVs['DEFENCE']) if 'DEFENCE' in EVs else 0  # Convert to int with a default value
        self.hp = 20
        self.health = health

types = ['Fire', 'Water', 'Grass', 'Electric', 'Flying', 'Psychic', 'Fighting', 'Rock', 'Poison', 'Bug', 'Ground', 'Ice', 'Normal', 'Dragon', 'Ghost', 'Dark', 'Steel', 'Fairy']
Fire_type=['Flamethrower','Blast Burn','Overheat','Incinerate']
Water_type=['Water Gun','Hydro Pump','Surf','Bubble Beam']
Grass_type=['Vine Whip', 'Grass Knot', 'Wood Hammer', 'Mega Drain']
Electric_type=['Thunder', 'Zap Cannon', 'Spark','Charge Beam']
Flying_type=['Gust', 'Wing Attack', 'Fly', 'Peck']
Psychic_type=['Psybeam', 'Confusion', 'Psychic','Zen Headbutt']
Fighting_type=['Karate Chop', 'Double Kick', 'Jump Kick', 'Rolling Kick']
Rock_type=['Rock Throw', 'Rock Slide', 'Rock Blast', 'Power Gem']
Poison_type=['Poison Sting', 'Acid', 'Poison Fang', 'Toxic']
Bug_type=['Fury Cutter', 'Megahorn','Bug Bite','X-Scissor']
Ground_type=['Earthquake', 'Dig', 'Mud-Slap','Bulldoze']
Ice_type=['Ice Punch', 'Ice Beam', 'Blizzard', 'Aurora Beam']
Normal_type=['Pound', 'Double Slap', 'Comet Punch', 'Mega Punch']
Dragon_type=['Dragon Rage', 'Outrage', 'Dragon Breath', 'Dragon Claw']
Ghost_type=['Night Shade', 'Shadow Ball','Astonish', 'Shadow Punch']
Dark_type=['Feint Attack', 'Crunch','Sucker Punch', 'Dark Pulse']
Steel_type=['Iron Tail', 'Metal Claw', 'Meteor Mash','Iron Head']
Fairy_type=['Play Rough', 'Fairy Wind', 'Moonblast', 'Geomancy']
Attacks_list=[Fire_type, Water_type, Grass_type, Electric_type ,Flying_type, Psychic_type, Fighting_type, Rock_type, Poison_type, Bug_type, Ground_type, Ice_type, Normal_type, Dragon_type, Ghost_type, Dark_type, Steel_type, Fairy_type]
Attacks_dict={}


# with open('move-data.csv', mode='r') as file1:
#     csvFile1 = csv.reader(file1)
#     next(csvFile1)
#     for line in csvFile1:
#         if line[2]=='Fire':
#             Fire_type.append(line[1])
#         if line[2]=='Water':
#             Water_type.append(line[1])
#         if line[2]=='Grass':
#             Grass_type.append(line[1])
#         if line[2]=='Electric':
#             Electric_type.append(line[1])
#         if line[2]=='Flying':
#             Flying_type.append(line[1])
#         if line[2]=='Psychic':
#             Psychic_type.append(line[1])
#         if line[2]=='Fighting':
#             Fighting_type.append(line[1])
#         if line[2]=='Rock':
#             Rock_type.append(line[1])
#         if line[2]=='Poison':
#             Poison_type.append(line[1])
#         if line[2]=='Bug':
#             Bug_type.append(line[1])
#         if line[2]=='Ground':
#             Ground_type.append(line[1])
#         if line[2]=='Ice':
#             Ice_type.append(line[1])
#         if line[2]=='Normal':
#             Normal_type.append(line[1])
#         if line[2]=='Dragon':
#             Dragon_type.append(line[1])
#         if line[2]=='Ghost':
#             Ghost_type.append(line[1])
#         if line[2]=='Dark':
#             Dark_type.append(line[1])
#         if line[2]=='Steel':
#             Steel_type.append(line[1])
#         if line[2]=='Fairy':
#             Fairy_type.append(line[1])
# #print(Attacks_list)
for i,j in list(zip(types,Attacks_list)):
    Attacks_dict[i]=j

Pokemon_dict = {}
with open('Pokedata(1).csv', mode='r') as file2:
    csvFile2 = csv.reader(file2)
    for line in csvFile2:
        #print(line)
        if len(line) >= 7:  # Check if the line has enough elements
            name = str(line[1])
            types = str(line[2])
            attack = int(line[5]) if line[5] else 0  # Convert to int with a default value
            defence = int(line[6]) if line[6] else 0  # Convert to int with a default value
            move = Attacks_dict[types]

            Pokemon_dict[name] = Pokemon(name, types, move,{'ATTACK': attack, 'DEFENCE': defence})
        else:
            print(f"Skipping line {line} as it doesn't have enough elements.")

#for name, pokemon in Pokemon_dict.items():
#print(name, pokemon)