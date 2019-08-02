import numpy as np

from tfttrader.game import pool, player


def init_players():
    player_array = np.empty(8, dtype=player.Player)
    for i in range(0, 8):
        player_array[i] = player.Player("player_{}".format(i))
    return player_array


class Game:
    def __init__(self):
        self.pool = pool.Pool()
        self.players = init_players()

    def start(self):
        print(self.pool.quantities)
        for p in self.players:
            print(p.to_string())
