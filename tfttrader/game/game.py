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

    def run(self):
        i = 1
        while i <= 30:
            print("Iteration number:    {}".format(i))
            for p in self.players:
                print("Shop for player:     {}".format(p.name))
                for j in range(0, 5):
                    # TODO: put a fine-super-crazy-fine algorithm to randomize champions from the pool
                    # champpos = random.randrange(0, self.pool.total)
                    # cp = champpos
                    # ci = 0
                    # champ_name = ""
                    # while cp > 0:
                    #     if self.pool.quantities[ci] < cp:
                    #         cp -= self.pool.quantities[ci]
                    #     else:
                    #         champ_name = self.pool.quantities[ci]
                    print("         position {}: {}".format(j, self.pool.quantities[0][0]), end="")
                print("\n")
            print("\n\n")
            i += 1
