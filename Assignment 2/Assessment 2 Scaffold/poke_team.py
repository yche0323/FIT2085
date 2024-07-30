# Author: team 3
# Date last updated: 30/04/2022
# Allows the user to set their pokemon team


from pokemon import Charmander
from pokemon import Bulbasaur
from pokemon import Squirtle
from pokemon import MissingNo

from queue_adt import CircularQueue
from stack_adt import ArrayStack
from array_sorted_list import ArraySortedList


class PokeTeam:
    def __init__(self, name: str):
        """
        Name: __init__
        Purpose: initialises self variables
        Complexity:
            Best: O(1)
            Worst: O(1)
        """

        if type(name) != str:
            raise ValueError("name must be a string")

        self.battle_mode = 0  # default battle-mode
        self.team = None  # ADT
        self.trainer_name = name
        self.maximum = 6

    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        """
        Name: choose_team
        Purpose: gets the user's team from input and checks for validity
        Complexity:
            Best: O(1)
            Worst: O(n)
        """

        if type(battle_mode) != int:
            raise ValueError("battle mode must be an integer")

        if type(criterion) != str:
            raise ValueError("criterion must be a string")

        # check if battle_mode is either 0,1, or 2
        if 2 < battle_mode < 0:
            raise Exception("Battle-mode must be either 0, 1 or 2")
        else:
            self.battle_mode = battle_mode

        if battle_mode == 0:
            self.team = ArrayStack(self.maximum)
        elif battle_mode == 1:
            self.team = CircularQueue(self.maximum)
        else:
            self.team = ArraySortedList(self.maximum)

        try:
            user_input = input("""
                        Howdy Trainer! Choose your team as C B S
                        where C is the number of Charmanders
                              B is the number of Bulbasaurs
                              S is the number of Squirtles
                              M is the number of MissingNo
                                """)
            user_input = user_input.split()  # splitting user input into four strings
            num_charmanders = int(user_input[0])
            num_bulbasaurs = int(user_input[1])
            num_squirtles = int(user_input[2])
            num_missingno = int(user_input[3])
            if (num_charmanders + num_bulbasaurs + num_squirtles + num_missingno) > 6: # Having 6 Pokemons is maximum
                raise Exception("Your team cannot have more than 6 pokemons!")
            elif num_missingno > 1: # Having one MissingNo is maximum
                raise Exception("Your team cannot have more than one MissingNo!")
        except Exception as e:
            raise ValueError(e)
        else:
            self.assign_team(num_charmanders, num_bulbasaurs, num_squirtles, num_missingno)
            # Calling insertion sort
            if battle_mode == 2:
                self.sort(criterion)

    def assign_team(self, charm: int, bulb: int, squir: int, missno: int) -> None:
        """
        Name:assign_team
        Purpose: assigns the user's team to adt depending on battle mode
        Complexity:
            Best:
            Worst:
        """

        if type(charm) != int:
            raise ValueError("charm must be an integer")

        if type(bulb) != int:
            raise ValueError("bulb must be an integer")

        if type(squir) != int:
            raise ValueError("squir must be an integer")

        if type(missno) != int:
            raise ValueError("missno must be an integer")

        if self.battle_mode == 0:
            for i in range(missno):
                self.team.push(MissingNo())

            for i in range(squir):
                self.team.push(Squirtle())

            for j in range(bulb):
                self.team.push(Bulbasaur())

            for i in range(charm):
                self.team.push(Charmander())

        elif self.battle_mode == 1:
            for i in range(charm):
                self.team.append(Charmander())

            for j in range(bulb):
                self.team.append(Bulbasaur())

            for i in range(squir):
                self.team.append(Squirtle())

            for i in range(missno):
                self.team.append(MissingNo())

        else:
            for i in range(charm):
                self.team.__setitem__(i, Charmander())

            for i in range(charm, bulb + charm):
                self.team.__setitem__(i, Bulbasaur())

            for i in range(charm + bulb, squir + bulb + charm):
                self.team.__setitem__(i, Squirtle())

            for i in range(squir + bulb + charm, squir + bulb + charm + missno):
                self.team.__setitem__(i, MissingNo())

    def sort(self, criterion: str) -> None:
        if criterion == "Level":
            for i in range(1, len(self.team)):
                temp = self.team[i].get_level()
                j = i - 1
                while j >= 0 and self.team[j].get_level() < temp:
                    self.team[j + 1] = self.team[j]
                    j -= 1

                self.team[j + 1] = temp

        elif criterion == "HP":
            for i in range(1, len(self.team)):
                temp = self.team[i].get_hp()
                j = i - 1
                while j >= 0 and self.team[j].get_hp() < temp:
                    self.team[j + 1] = self.team[j]
                    j -= 1

                self.team[j + 1] = temp

        elif criterion == "Attack":
            for i in range(1, len(self.team)):
                temp = self.team[i].get_attack()
                j = i - 1
                while j >= 0 and self.team[j].get_attack() < temp:
                    self.team[j + 1] = self.team[j]
                    j -= 1

                self.team[j + 1] = temp

        elif criterion == "Defence":
            for i in range(1, len(self.team)):
                temp = self.team[i].get_def()
                j = i - 1
                while j >= 0 and self.team[j].get_def() < temp:
                    self.team[j + 1] = self.team[j]
                    j -= 1

                self.team[j + 1] = temp

        elif criterion == "Speed":
            for i in range(1, len(self.team)):
                temp = self.team[i].get_speed()
                j = i - 1
                while j >= 0 and self.team[j].get_speed() < temp:
                    self.team[j + 1] = self.team[j]
                    j -= 1

                self.team[j + 1] = temp
