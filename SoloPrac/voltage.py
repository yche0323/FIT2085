import math

# time to gain one LP (in minute)
time_minute = 1.5


def func(a: float, cost: int, comp_minute: float) -> int:
    # to test if recursion will go infinite
    # time - time to gain one round(game) worth of LP
    time = cost * time_minute
    if comp_minute > time:
        raise Exception("gaining one round(game) worth of LP takes lesser time than completing one round of game")

    # a - the maximum number of LP
    # cost - the cost of the mission
    # comp_minute - time to complete one mission (in minute)
    if a < cost:
        return 0
    else:
        no_game = a / cost
        remainder = a % cost
        time_taken = comp_minute * no_game
        gain = time_taken/time_minute
        return math.floor(func(gain + remainder, cost, comp_minute) + no_game)


# Dumpling Mission
print("Dumpling Mission: " + str(func(80, 6, 1 + 13/20)))

# Material Mission
print("Material Mission: " + str(func(74, 6, 1 + 7/20)))
