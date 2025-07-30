import random

class Pokemon:
    def __init__(self, name, species, element, weakness, resistance, moveSet):
        self.name = name
        self.species = species
        self.element = element
        self.weakness = weakness
        self.resistance = resistance
        self.moveSet = moveSet

        #randomly generated properties
        self.health = random.randint(115, 150)
        self.attack = random.randint(80, 115)
        self.defense = random.randint(80,115)
        self.speed = random.randint(80, 115)

    
    def calculateDamage(self, move, attack, opponent):
        STAB = move.STAB
        if (move.element in self.weakness):
            typeEffect = 2.0
            print(f"{opponent} used {move.move}... it's super effective!")
        elif (move.element in self.resistance):
            typeEffect = 0.5
            print(f"{opponent} used {move.move}... it was not very effective...")
        else:
            typeEffect = 1.0
            print(f"{opponent} used {move.move}...")

        randomMod = random.uniform(0.85, 1.0)
        crit = random.randint(1,2)
        attackMod = STAB * typeEffect * crit * randomMod
        defense = self.defense

        damage = (((0.44) * (attack/defense) * move.basePower + 2) * attackMod)
        self.health = self.health - damage

        if self.health < 0:
            self.health = 0

#-------------------------------------------------------------------------------#

class Bulbasaur(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Bulbasaur", "Grass", "Fire", ["Grass", "Water"], ["Tackle", "VineWhip"])

class Charmander(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Charmander", "Fire", "Water", ["Fire", "Grass"], ["Scratch", "Ember"])

class Squirtle(Pokemon):
    def __init__(self, name):
        super().__init__(name, "Squirtle", "Water", "Grass", ["Water", "Fire"], ["Tackle", "WaterGun"])
