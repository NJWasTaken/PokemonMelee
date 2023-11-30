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
Fire_type=[]
Water_type=[]
Grass_type=[]
Electric_type=[]
Flying_type=[]
Psychic_type=[]
Fighting_type=[]
Rock_type=[]
Poison_type=[]
Bug_type=[]
Ground_type=[]
Ice_type=[]
Normal_type=[]
Dragon_type=[]
Ghost_type=[]
Dark_type=[]
Steel_type=[]
Fairy_type=[]
Attacks_list=[Fire_type, Water_type, Grass_type, Electric_type ,Flying_type, Psychic_type, Fighting_type, Rock_type, Poison_type, Bug_type, Ground_type, Ice_type, Normal_type, Dragon_type, Ghost_type, Dark_type, Steel_type, Fairy_type]
Attacks_dict={}
for i,j in zip(types,Attacks_list):
    Attacks_dict[i]=j

with open('move-data.csv', mode='r') as file1:
    csvFile1 = csv.reader(file1)
    next(csvFile1)
    for line in csvFile1:
        if line[2]=='Fire':
            Fire_type.append(line[1])
        if line[2]=='Water':
            Water_type.append(line[1])
        if line[2]=='Grass':
            Grass_type.append(line[1])
        if line[2]=='Electric':
            Electric_type.append(line[1])
        if line[2]=='Flying':
            Flying_type.append(line[1])
        if line[2]=='Psychic':
            Psychic_type.append(line[1])
        if line[2]=='Fighting':
            Fighting_type.append(line[1])
        if line[2]=='Rock':
            Rock_type.append(line[1])
        if line[2]=='Poison':
            Poison_type.append(line[1])
        if line[2]=='Bug':
            Bug_type.append(line[1])
        if line[2]=='Ground':
            Ground_type.append(line[1])
        if line[2]=='Ice':
            Ice_type.append(line[1])
        if line[2]=='Normal':
            Normal_type.append(line[1])
        if line[2]=='Dragon':
            Dragon_type.append(line[1])
        if line[2]=='Ghost':
            Ghost_type.append(line[1])
        if line[2]=='Dark':
            Dark_type.append(line[1])
        if line[2]=='Steel':
            Steel_type.append(line[1])
        if line[2]=='Fairy':
            Fairy_type.append(line[1])
#print(Attacks_list)

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
            #print(f"Skipping line {line} as it doesn't have enough elements.")

#for name, pokemon in Pokemon_dict.items():
    #print(name, pokemon)

