# Author: team 3
# Date last updated: 30/04/2022
# Allows the user to choose the battle mode

from poke_team import PokeTeam


class Battle:

    # Constructor method which creates two empty teams
    def __init__(self, trainer_one_name: str, trainer_two_name: str):
        """
        Name: __init__
        Purpose: declares self variables
        Complexity:
            Best: O(1)
            Worst: O(1)
        """
        if type(trainer_one_name) != str:
            raise ValueError("trainer_one_name must be a string")

        if type(trainer_two_name) != str:
            raise ValueError("trainer_two_name must be a string")

        self.battle_mode = None

        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)

    def set_mode_battle(self) -> str:
        """
        Name: set_mode_battle
        Purpose: A battle mode where a Pokemon from each team fight until it faints,
                 and the battle ends when at least one of the team is empty
        Complexity:
            Best: O(len(n)*Comp)
            Worst: O(len(n)*Comp)
        """
        self.team1.choose_team(0)
        self.team2.choose_team(0)

        # Runs when both team 1 and team 2 are not empty
        while not self.team1.team.is_empty() and not self.team2.team.is_empty():
            # Getting the first Pokemon on each team
            team_1_chosen_poke = self.team1.team.pop()
            team_2_chosen_poke = self.team2.team.pop()

            # if team_1_chosen_poke is faster than team_2_chosen_poke, then team_1_chosen_poke will attack first
            if team_1_chosen_poke.get_speed() > team_2_chosen_poke.get_speed():
                team_2_chosen_poke.attacked(team_1_chosen_poke)
                # if team_2_chosen_poke did not faint after getting attacked, it will retort
                if team_2_chosen_poke.get_hp() > 0:
                    team_1_chosen_poke.attacked(team_2_chosen_poke)
                    # if team_1_chosen_poke faints, team_2_chosen_poke gain an extra level
                    if team_1_chosen_poke.get_hp() <= 0:
                        team_2_chosen_poke.set_level(team_2_chosen_poke.get_level() + 1)
                        self.team2.team.push(team_2_chosen_poke)
                    else:
                        self.team1.team.push(team_1_chosen_poke)
                        self.team1.team.push(team_2_chosen_poke)
                # if team_2_chosen_poke faints, team_1_chosen_poke gain an extra level
                else:
                    team_1_chosen_poke.set_level(team_1_chosen_poke.get_level() + 1)
                    self.team1.team.push(team_1_chosen_poke)
            # if team_2_chosen_poke is faster than team_1_chosen_poke, then team_2_chosen_poke will attack first
            elif team_2_chosen_poke.get_speed() > team_1_chosen_poke.get_speed():
                team_1_chosen_poke.attacked(team_2_chosen_poke)
                # if team_1_chosen_poke did not faint after getting attacked, it will retort
                if team_1_chosen_poke.get_hp() > 0:
                    team_2_chosen_poke.attacked(team_1_chosen_poke)
                    # if team_2_chosen_poke faints, team_1_chosen_poke gain an extra level
                    if team_2_chosen_poke.get_hp() <= 0:
                        team_1_chosen_poke.set_level(team_1_chosen_poke.get_level() + 1)
                        self.team1.team.push(team_1_chosen_poke)
                    else:
                        self.team1.team.push(team_1_chosen_poke)
                        self.team2.team.push(team_2_chosen_poke)
                # if team_1_chosen_poke faints, team_2_chosen_poke gain an extra level
                else:
                    team_2_chosen_poke.set_level(team_2_chosen_poke.get_level() + 1)
                    self.team2.team.push(team_2_chosen_poke)
            # if team_1_chosen_poke has the same speed as team_1_chosen_poke, then both of them attack at the same time
            else:
                team_1_chosen_poke.attacked(team_2_chosen_poke)
                team_2_chosen_poke.attacked(team_1_chosen_poke)
                # if team_1_chosen_poke did not faint
                if team_1_chosen_poke.get_hp() > 0:
                    # if team_2_chosen_poke faints, team_1_chosen_poke gain an extra level
                    if team_2_chosen_poke.get_hp() <= 0:
                        team_1_chosen_poke.set_level(team_1_chosen_poke.get_level() + 1)
                        self.team1.team.push(team_1_chosen_poke)
                    else:
                        self.team1.team.push(team_1_chosen_poke)
                        self.team2.team.push(team_2_chosen_poke)
                # if team_1_chosen_poke faints and team_2_chosen_poke did not faint, team_2_chosen_poke gain an extra level
                else:
                    if team_2_chosen_poke.get_hp() > 0:
                        team_2_chosen_poke.set_level(team_2_chosen_poke.get_level() + 1)
                        self.team2.team.push(team_2_chosen_poke)

        # if team 1 is empty, team 2 wins
        if self.team1.team.is_empty():
            return self.team2.trainer_name + " Wins!"
        # if team 2 is empty, team 1 wins
        elif self.team2.team.is_empty():
            return self.team1.trainer_name + " Wins!"
        # else, draw
        else:
            return "Draw!"

    def rotating_mode_battle(self) -> str:
        """
        Name: __init__
        Purpose: A battle mode where a Pokemon from each team fight for only a round,
                 and get send to the back of the team after each round (if the Pokemon did not faint).
                 The battle ends when at least one of the team is empty.
        Complexity:
            Best: O(len(n)*Comp)
            Worst: O(len(n)*Comp)
        """
        self.team1.choose_team(1)
        self.team2.choose_team(1)

        # Runs when both team 1 and team 2 are not empty
        while not self.team1.team.is_empty() and not self.team2.team.is_empty():
            # Getting the first Pokemon on each team
            team_1_chosen_poke = self.team1.team.serve()
            team_2_chosen_poke = self.team2.team.serve()

            # if team_1_chosen_poke is faster than team_2_chosen_poke, then team_1_chosen_poke will attack first
            if team_1_chosen_poke.get_speed() > team_2_chosen_poke.get_speed():
                team_2_chosen_poke.attacked(team_1_chosen_poke)
                # if team_2_chosen_poke did not faint after getting attacked, it will retort
                if team_2_chosen_poke.get_hp() > 0:
                    team_1_chosen_poke.attacked(team_2_chosen_poke)
                    # if team_1_chosen_poke faints, team_2_chosen_poke gain an extra level
                    if team_1_chosen_poke.get_hp() <= 0:
                        team_2_chosen_poke.set_level(team_2_chosen_poke.get_level() + 1)
                        self.team2.team.append(team_2_chosen_poke)
                    else:
                        self.team1.team.append(team_1_chosen_poke)
                        self.team2.team.append(team_2_chosen_poke)
                # if team_2_chosen_poke faints, team_1_chosen_poke gain an extra level
                else:
                    team_1_chosen_poke.set_level(team_1_chosen_poke.get_level() + 1)
                    self.team1.team.append(team_1_chosen_poke)
            # if team_2_chosen_poke is faster than team_1_chosen_poke, then team_2_chosen_poke will attack first
            elif team_2_chosen_poke.get_speed() > team_1_chosen_poke.get_speed():
                team_1_chosen_poke.attacked(team_2_chosen_poke)
                # if team_1_chosen_poke did not faint after getting attacked, it will retort
                if team_1_chosen_poke.get_hp() > 0:
                    team_2_chosen_poke.attacked(team_1_chosen_poke)
                    # if team_2_chosen_poke faints, team_1_chosen_poke gain an extra level
                    if team_2_chosen_poke.get_hp() <= 0:
                        team_1_chosen_poke.set_level(team_1_chosen_poke.get_level() + 1)
                        self.team1.team.append(team_1_chosen_poke)
                    else:
                        self.team1.team.append(team_1_chosen_poke)
                        self.team2.team.append(team_2_chosen_poke)
                # if team_1_chosen_poke faints, team_2_chosen_poke gain an extra level
                else:
                    team_2_chosen_poke.set_level(team_2_chosen_poke.get_level() + 1)
                    self.team2.team.append(team_2_chosen_poke)
            # if team_1_chosen_poke and team_2_chosen_poke has the same speed, then both of them attack at the same time
            else:
                team_1_chosen_poke.attacked(team_2_chosen_poke)
                team_2_chosen_poke.attacked(team_1_chosen_poke)
                # if team_1_chosen_poke did not faint
                if team_1_chosen_poke.get_hp() > 0:
                    # if team_2_chosen_poke faints, team_1_chosen_poke gain an extra level
                    if team_2_chosen_poke.get_hp() <= 0:
                        team_1_chosen_poke.set_level(team_1_chosen_poke.get_level() + 1)
                        self.team1.team.append(team_1_chosen_poke)
                    else:
                        self.team1.team.append(team_1_chosen_poke)
                        self.team2.team.append(team_2_chosen_poke)
                # if team_1_chosen_poke faints and team_2_chosen_poke did not faint, team_2_chosen_poke gain an extra level
                else:
                    if team_2_chosen_poke.get_hp() > 0:
                        team_2_chosen_poke.set_level(team_2_chosen_poke.get_level() + 1)
                        self.team2.team.append(team_2_chosen_poke)

        # if team 1 is empty, team 2 wins
        if self.team1.team.is_empty():
            return self.team2.trainer_name + " Wins!"
        # if team 2 is empty, team 1 wins
        elif self.team2.team.is_empty():
            return self.team1.trainer_name + " Wins!"
        # else, draw
        else:
            return "Draw!"

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """
        Name: __init__
        Purpose: A battle mode where the trainer get to choose how they want to arrange their team,
                 and the Pokemons will come out one by one and fight for only a round
                 before getting send back to their own team with their corresponding arrangement (if the Pokemon did not faint).
                 The battle ends when at least one of the team is empty
        Complexity:
            Best: O(len(n)*Comp)
            Worst: O(len(n)*Comp)
        """
        self.team1.choose_team(2, criterion_team1)
        self.team2.choose_team(2, criterion_team2)

        # Runs when both team 1 and team 2 are not empty
        while not self.team1.team.is_empty() and not self.team2.team.is_empty():
            # Getting the first Pokemon on each team
            team_1_chosen_poke = self.team1.team.__getitem__(0)
            team_2_chosen_poke = self.team2.team.__getitem__(0)

            # if team_1_chosen_poke is faster than team_2_chosen_poke, then team_1_chosen_poke will attack first
            if team_1_chosen_poke.get_speed() > team_2_chosen_poke.get_speed():
                team_2_chosen_poke.attacked(team_1_chosen_poke)
                # if team_2_chosen_poke did not faint after getting attacked, it will retort
                if team_2_chosen_poke.get_hp() > 0:
                    team_1_chosen_poke.attacked(team_2_chosen_poke)
                    # if team_2_chosen_poke faints, team_1_chosen_poke gain an extra level
                    if team_1_chosen_poke.get_hp() <= 0:
                        team_2_chosen_poke.set_level(team_2_chosen_poke.get_level() + 1)
                        self.team2.team.__setitem__(0, team_2_chosen_poke)
                        self.team1.team._shuffle_left(1)
                    else:
                        self.team1.team.__setitem__(0, team_1_chosen_poke)
                        self.team2.team.__setitem__(0, team_2_chosen_poke)
                # if team_1_chosen_poke faints, team_2_chosen_poke gain an extra level
                else:
                    team_1_chosen_poke.set_level(team_1_chosen_poke.get_level() + 1)
                    self.team1.team.__setitem__(0, team_1_chosen_poke)
                    self.team2.team._shuffle_left(1)
            # if team_2_chosen_poke is faster than team_1_chosen_poke, then team_2_chosen_poke will attack first
            elif team_2_chosen_poke.get_speed() > team_1_chosen_poke.get_speed():
                team_1_chosen_poke.attacked(team_2_chosen_poke)
                # if team_1_chosen_poke did not faint after getting attacked, it will retort
                if team_1_chosen_poke.get_hp() > 0:
                    team_2_chosen_poke.attacked(team_1_chosen_poke)
                    # if team_2_chosen_poke faints, team_1_chosen_poke gain an extra level
                    if team_2_chosen_poke.get_hp() <= 0:
                        team_1_chosen_poke.set_level(team_1_chosen_poke.get_level() + 1)
                        self.team1.team.__setitem__(0, team_1_chosen_poke)
                        self.team2.team._shuffle_left(1)
                    else:
                        self.team1.team.__setitem__(0, team_1_chosen_poke)
                        self.team2.team.__setitem__(0, team_2_chosen_poke)
                # if team_1_chosen_poke faints, team_2_chosen_poke gain an extra level
                else:
                    team_2_chosen_poke.set_level(team_2_chosen_poke.get_level() + 1)
                    self.team2.team.__setitem__(0, team_2_chosen_poke)
                    self.team1.team._shuffle_left(1)
            # if team_1_chosen_poke and team_2_chosen_poke has the same speed, then both of them attack at the same time
            else:
                team_1_chosen_poke.attacked(team_2_chosen_poke)
                team_2_chosen_poke.attacked(team_1_chosen_poke)
                # if team_1_chosen_poke did not faint
                if team_1_chosen_poke.get_hp() > 0:
                    # if team_2_chosen_poke faints, team_1_chosen_poke gain an extra level
                    if team_2_chosen_poke.get_hp() <= 0:
                        team_1_chosen_poke.set_level(team_1_chosen_poke.get_level() + 1)
                        self.team1.team.__setitem__(0, team_1_chosen_poke)
                        self.team2.team._shuffle_left(1)
                    else:
                        self.team1.team.__setitem__(0, team_1_chosen_poke)
                        self.team2.team.__setitem__(0, team_2_chosen_poke)
                # if team_1_chosen_poke faints
                else:
                    self.team1.team._shuffle_left(1)
                    # if team_2_chosen_poke did not faint, team_2_chosen_poke gain an extra level
                    if team_2_chosen_poke.get_hp() > 0:
                        team_2_chosen_poke.set_level(team_2_chosen_poke.get_level() + 1)
                        self.team2.team.__setitem__(0, team_2_chosen_poke)
                    else:
                        self.team2.team._shuffle_left(1)

            self.team1.sort(criterion_team1)
            self.team2.sort(criterion_team2)

        # if team 1 is empty, team 2 wins
        if self.team1.team.is_empty():
            return self.team2.trainer_name + " Wins!"
        # if team 2 is empty, team 1 wins
        elif self.team2.team.is_empty():
            return self.team1.trainer_name + " Wins!"
        # else, draw
        else:
            return "Draw!"
