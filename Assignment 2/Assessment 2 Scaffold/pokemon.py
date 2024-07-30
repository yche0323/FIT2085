# Author: team 3
# Date: 30/ 04/ 2022
# This file instantiates PokemonBase to create the three pokemon (Charmander, Bulbauser, Squirtle) and MissingNo

from glitchmon import GlitchMon
from pokemon_base import PokemonBase

import random


class Charmander(PokemonBase):
    def __init__(self) -> None:

        PokemonBase.__init__(self, 7, "fire")
        self.name = "Charmander"
        self.attack = 6 + self.level
        self.defence = 4
        self.speed = 7 + self.level

    def get_name(self) -> str:
        return self.name

    def get_speed(self) -> int:
        return self.speed

    def get_attack(self) -> int:
        return self.attack

    def get_type(self) -> str:
        return self.poke_type

    def get_def(self) -> int:
        return self.defence

    def attacked(self, attacker: PokemonBase) -> None:
        # determine the type effectiveness
        if attacker.get_type() == "grass":
            multiplier = 0.5
        elif attacker.get_type() == "water":
            multiplier = 2
        else:
            multiplier = 1

        # subtract damage from hp
        if attacker.get_attack() > self.defence:
            self.hp -= attacker.get_attack() * multiplier
        else:
            self.hp -= attacker.get_attack() // 2 * multiplier


class Bulbasaur(PokemonBase):
    def __init__(self) -> None:
        PokemonBase.__init__(self, 9, "grass")

        self.name = "Bulbasaur"
        self.attack = 5
        self.defence = 5
        self.speed = 7 + (self.level // 2)

    def get_name(self) -> str:
        return self.name

    def get_speed(self) -> int:
        return self.speed

    def get_attack(self) -> int:
        return self.attack

    def get_type(self) -> str:
        return self.poke_type

    def get_def(self) -> int:
        return self.defence

    def attacked(self, attacker: PokemonBase) -> None:
        if attacker.get_type == "fire":
            multiplier = 2
        elif attacker.get_type == "water":
            multiplier = 0.5
        else:
            multiplier = 1

        # subtract damage from hp
        if attacker.get_attack() > self.defence + 5:
            self.hp -= attacker.get_attack() * multiplier
        else:
            self.hp -= attacker.get_attack() // 2 * multiplier


class Squirtle(PokemonBase):
    def __init__(self) -> None:
        PokemonBase.__init__(self, 8, "water")
        self.name = "Squirtle"
        self.attack = 4 + (self.level // 2)
        self.defence = 6 + self.level
        self.speed = 7

    def get_name(self) -> str:
        return self.name

    def get_speed(self) -> int:
        return self.speed

    def get_attack(self) -> int:
        return self.attack

    def get_type(self) -> str:
        return self.poke_type

    def get_def(self) -> int:
        return self.defence

    def attacked(self, attacker: PokemonBase) -> None:
        if attacker.get_type() == "fire":
            multiplier = 0.5
        elif attacker.get_type() == "grass":
            multiplier = 2
        else:
            multiplier = 1

        # subtract damage from hp
        if attacker.get_attack() > self.defence * 2:
            self.hp -= attacker.get_attack() * multiplier
        else:
            self.hp -= attacker.get_attack() // 2 * multiplier


class MissingNo(GlitchMon):
    def __init__(self) -> None:
        GlitchMon.__init__(self, 8)
        self.name = "missingno"
        self.attack = 5 + self.level
        self.defence = 5 + self.level
        self.speed = 7 + self.level

    def get_name(self) -> str:
        return self.name

    def get_speed(self) -> int:
        return self.speed

    def get_attack(self) -> int:
        return self.attack

    def get_type(self) -> str:
        return self.poke_type

    def get_def(self) -> int:
        return self.defence

    def attacked(self, attacker: PokemonBase) -> None:
        def_chance = 25

        if random.randint(1, 100) < def_chance:
            self.superpower()
