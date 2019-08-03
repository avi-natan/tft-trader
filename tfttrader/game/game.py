import numpy as np

from tfttrader.game import pool, player
from tfttrader.strategies import leftmost, rightmost


class Game:
    def __init__(self):
        self.pool = pool.Pool()
        self.players = self.init_players()

    def init_players(self):
        player_array = np.empty(8, dtype=player.Player)
        for i in range(0, 8):
            if i % 2 == 0:
                player_array[i] = player.Player(self, "player_{}".format(i), leftmost.Leftmost())
            else:
                player_array[i] = player.Player(self, "player_{}".format(i), rightmost.Rightmost())
        return player_array

    def start(self):
        print(self.pool.quantities)
        for p in self.players:
            print(p.to_string())
