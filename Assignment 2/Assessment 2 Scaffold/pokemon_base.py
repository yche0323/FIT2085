# Author: team 3 
# Date last updated: 30/04/2022 
# Provides a class base to construct pokemons 

from abc import ABC, abstractmethod


class PokemonBase(ABC):
    # task 1.1
    def __init__(self, hp: int, poke_type: str) -> None:
        """
        Name: __init__
        Purpose: takes hp (int) and poke_type (str) and sets level to 1
        Complexity:
            Best: O(1)
            Worst: O(1)
        """

        if type(hp) != int:
            raise ValueError("hp must be an integer")

        if type(poke_type) != str:
            raise ValueError("poke_type must be a string")

        self.hp = hp
        self.poke_type = poke_type
        self.level = 1

    # task 1.2
    def get_hp(self) -> int:
        """
        Name: get_hp
        Purpose: returns the pokemon's hp
        Complexity:
            Best: O(1)
            Worst: O(1)
        """

        return self.hp

    def set_hp(self, new_hp) -> None:
        """
        Name: set_hp
        Purpose: takes a new level value and sets this integer to the pokemon's hp
        Complexity:
            Best: O(1)
            Worst: O(1)
        """
        if type(new_hp) != int:
            raise ValueError("hp must be an integer")

        if new_hp < 0:
            raise ValueError("hp cannot be less than 0")

        self.hp = new_hp

    def get_level(self) -> int:
        """
        Name: get_level
        Purpose: returns the pokemon's level
        Complexity:
            Best: O(1)
            Worst: O(1)
        """

        return self.level

    def set_level(self, new_level) -> None:
        """
        Name: set_level
        Purpose: takes a new level value and sets this integer to the pokemon's hp
        Complexity:
            Best: O(1)
            Worst: O(1)
        """

        if type(new_level) != int:
            raise ValueError("level must be an integer")

        if new_level < 0:
            raise ValueError("level cannot be less than 0")

        self.level = new_level

    # task 1.3
    @abstractmethod
    def get_name(self) -> str:
        """
        Name: get_name
        Purpose: abstract method that when updated will return the pokemons name (str)
        Complexity:
            Best: O(1)
            Worst: O(1)
        """

        pass

    @abstractmethod
    def get_speed(self) -> int:
        """
        Name: get_speed
        Purpose: abstract method that when updated will return the pokemons speed (int)
        Complexity:
            Best: O(1)
            Worst: O(1)
        """

        pass

    @abstractmethod
    def get_attack(self) -> int:
        """
        Name: get_attack
        Purpose: abstract method that when updated will return the pokemons attack damage (int)
        Complexity:
            Best: O(1)
            Worst: O(1)
        """

        pass

    @abstractmethod
    def get_type(self) -> str:
        """
        Name: get_type
        Purpose: abstract method that when updated will return the pokemons type (str)
        Complexity:
            Best: O(1)
            Worst: O(1)
        """

        pass

    # task 1.4
    @abstractmethod
    def attacked(self, attacker: object) -> None:
        """
        Name: attacked
        Purpose: abstarct method that when updated will alter pokemon's hp
        Complexity:
            Best: O(1)
            Worst: O(1)
        """

        pass

    # task 1.5
    def __str__(self) -> str:
        """
        Name: __str__
        Purpose: returns string for print statement containing the pokemon's information
        Complexity:
            Best: O(1)
            Worst: O(1)
        """

        return f"{self.get_name()}'s HP = {self.get_hp()} and level = {self.get_level()}"
