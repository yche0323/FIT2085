from pokemon_base import PokemonBase
import random


class GlitchMon(PokemonBase):
    def __init__(self, hp: int):
        super().__init__(hp, "None")
        self.hp = hp
        self.level = 1

    def gain_hp(self):
        self.hp += 1
        self.set_hp(self.hp)

    def superpower(self):
        random_gain = random.randint(1, 3)

        if random_gain == 1:
            self.level += 1
        elif random_gain == 2:
            self.gain_hp()
        else:
            self.level += 1
            self.gain_hp()
