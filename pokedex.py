#each class retains the __init__ unless overridden with a local __init__
#init contains strength, weakness and null eventhough they exist as class variables locally as each pokemon can be assigned diff variables at discretion if required

types = ['Fire', 'Water', 'Grass', 'Electric', 'Flying', 'Psychic', 'Fighting', 'Rock', 'Poison', 'Bug', 'Ground', 'Ice', 'Normal', 'Dragon', 'Ghost', 'Dark', 'Steel', 'Fairy']

#parent class
class poketype:
    null = [x for x in types and x not in strength+weakness]
  def __init__(self, name, strength, weakness, null):
    self.name = name
    self.strength = strength
    self.weakness = weakness
    self.null = null

#child classes

class Fire(poketype):
  strength = ['Bug', 'Grass', 'Ice', 'Steel']
  weakness = ['Ground', 'Rock', 'Water']

class Water(poketype):
  strength = ['Fire', 'Ground', 'Rock']
  weakness = ['Electric', 'Grass']

class Grass(poketype):
  strength = ['Ground', 'Rock', 'Water']
  weakness = ['Bug', 'Fire', 'Flying', 'Ice', 'Poison']

class Electric(poketype):
  strength = ['Flying', 'Water']
  weakness = ['Ground']

class Flying(poketype):
  strength = ['Bug', 'Fighting', 'Grass']
  weakness = ['Electric', 'Ice', 'Rock']

class Psychic(poketype):
  strength = ['Fighting', 'Poison']
  weakness = ['Bug', 'Dark', 'Ghost']

class Fighting(poketype):
  strength = ['Dark', 'Ice', 'Normal', 'Rock', 'Steel']
  weakness = ['Fairy', 'Flying', 'Psychic']=

class Rock(poketype):
  strength = ['Bug', 'Fire', 'Flying', 'Ice']
  weakness = ['Fighting', 'Grass', 'Ground', 'Steel', 'Water']

class Poison(poketype):
  strength = ['Fairy', 'Grass']
  weakness = ['Ground', 'Psychic']

class Bug(poketype):
  strength = ['Grass', 'Dark', 'Psychic']
  weakness = ['Fire', 'Flying', 'Rock']

class Ground(poketype):
  strength = ['Electric', 'Fire', 'Poison', 'Rock', 'Steel']
  weakness = ['Grass', 'Ice', Wate]

class Ice(poketype):
  strength = ['Dragon', 'Flying', 'Grass', 'Ground']
  weakness = ['Fighting', 'Fire', 'Rock', 'Steel']

class Normal(poketype):
  strength = []
  weakness = ['Fighting']

class Dragon(poketype):
  strength = ['Dragon']
  weakness = ['Dragon', 'Fairy', 'Ice']

class Ghost(poketype):
  strength = ['Ghost', 'Psychic']
  weakness = ['Dark', 'Ghost']

class Dark(poketype):
  strength = ['Ghost', 'Psychic']
  weakness = ['Bug', 'Fairy', 'Fighting']

class Steel(poketype):
  strength = ['Fairy', 'Ice', 'Rock']
  weakness = ['Fighting', 'Fire', 'Ground']

class Fairy(poketype):
  strength = ['Fighting', 'Dark', 'Dragon']
  weakness = ['Poison', 'Steel']
