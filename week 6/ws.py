""" Pets, Kids and Toys implementation.
"""
from abc import ABC, abstractmethod
import math


class PlayableAtCapacity(Exception):
    """ Exception raised when a Playable is at capacity,
    i.e. the maximum number of players has been reached."""

    def __init__(self):
        Exception.__init__(self)


class PlayerIsNotCurrentlyPlaying(Exception):
    """ Exception raised when a Player is incorrectly
    assumed to be already playing."""

    def __init__(self):
        Exception.__init__(self)


class Playable(ABC):
    """ Describes something that can be played with and can have
    a maximum number of players. """

    def __init__(self, name, maxplayers=math.inf):
        self.name = name
        self.maxplayers = maxplayers
        self.players = []

    def __str__(self) -> str:
        return self.name

    def has_free_player_spot(self) -> bool:
        """
        Returns True iff a player can join.
        """
        return len(self.players) < self.maxplayers

    def _add_player(self, player: "Player") -> None:
        """
        Adds a player to the playable.
        :pre: player is not None.
        :pre: player is not playing with this playable.
        :raises PlayableAtCapacity: if the playable already has the max number of players
        """
        assert player is not None                   # player is not None
        assert player.playing_with is not self      # player is not playing with this playable

        if self.has_free_player_spot():             # if a player can join
            self.players.append(player)             # adds a player to the playable
        else:                                       # if the playable already has the max number of players
            raise PlayableAtCapacity                # raise PlayableAtCapacity

    def _remove_player(self, player: "Player") -> None:
        """
        Given a player playing with the playable,
        removes that player.
        :pre: player is not None.
        :pre: player is currently playing with this playable.
        """
        assert player is not None               # pre: player is not None
        assert player.playing_with is self      # pre: player is currently playing with this playable
        self.players.remove(player)             # remove that player


class Player(ABC):
    """ A player can play or stop playing.
    """

    def __init__(self, name):
        self.name = name
        self.playing_with = None

    def __str__(self):
        return self.name

    def play(self, playable: Playable) -> bool:
        """ Returns True if and only if the player is
        playing with playable when the function returns.
        If the player is already playing with the playable,
        then nothing happens.
        Otherwise, the player stops playing with another playable, if any.
        :pre: playable is not None
        """

        if self.playing_with is not None:       # If the player is not None
            if self.playing_with is playable:   # If the player is already playing with the playable
                return True                     # return True
            else:                               # Otherwise,
                self.stop_playing()             # the player stops playing with another playable

        try:
            playable._add_player(self)          # try adding the player to the playable
            self.playing_with = playable        # if playable has free slots, then player is playing with playable
            print("{} is now playing with {}".format(self, playable))
            return True                         # return True
        except PlayableAtCapacity as e:         # if playable does not have free slots, then raise PlayableAtCapacity
            print("{} cannot play with {}".format(self, playable))
            return False                        # return False

    def stop_playing(self) -> None:
        """
        Makes the player stop playing.
        :raise PlayerIsNotCurrentlyPlaying: if the player is currently not playing
        """
        assert self.playing_with is not None, PlayerIsNotCurrentlyPlaying

        self.playing_with._remove_player(self)
        print("{} has stopped playing with {}".format(self, self.playing_with))


class Toy(Playable):
    """ A Toy """

    def __init__(self, name: str, maxplayers) -> None:
        Playable.__init__(self, name, maxplayers)


class Kid(Player):
    """ A Kid """

    def __init__(self, name: str) -> None:
        Player.__init__(self, name)


class Pet(Player, Playable):
    """ A Pet """

    def __init__(self, name) -> None:
        Player.__init__(self, name)
        Playable.__init__(self,name)


diamond = Pet("Diamond")
syscall = Pet("Syscall")

taylor = Kid("Taylor")
connect4 = Toy("connect4", 2)

print("1")
taylor.play(diamond)
print("2")
taylor.play(diamond)
print("3")
taylor.play(syscall)

print("4")
diamond.play(connect4)
print("5")
taylor.play(connect4)
print("6")
syscall.play(connect4)
print("7")
taylor.stop_playing()
print("8")
syscall.stop_playing()