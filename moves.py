class Moves:
    def __init__(self, move, element, basePower, pokemonType):
        self.move = move
        self.element =  element
        self.basePower = basePower
        self.pokemonType = pokemonType
        if (self.element == self.pokemonType):
            self.STAB = 1.5
        else:
            self.STAB = 1.0


class Tackle(Moves):
    def __init__(self, pokemonType):
        super().__init__("Tackle", "Normal", 50, pokemonType)

class Scratch(Moves):
    def __init__(self, pokemonType):
        super().__init__("Scratch", "Normal", 40, pokemonType)

class Vinewhip(Moves):
    def __init__(self, pokemonType):
        super().__init__("Vine Whip", "Grass", 45, pokemonType)

class Ember(Moves):
    def __init__(self, pokemonType):
        super().__init__("Ember", "Fire", 40, pokemonType)

class WaterGun(Moves):
    def __init__(self, pokemonType):
        super().__init__("Water Gun", "Water", 40, pokemonType)