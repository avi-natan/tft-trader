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
            self.planning_session(i)
            self.battle_session(i)
            i += 1

    def planning_session(self, session_number):
        print("Planning session number:    {}".format(session_number))
        for p in self.players:
            self.pool.recall_old_personal_shop(p.get_personal_shop())

        for p in self.players:
            p.update_gold()
            p.update_exp()
            p.update_personal_shop(self.pool.get_shop_for_level(p.get_level()))
            print("Shop for player:     {}, level {}".format(p.name, p.get_level()))
            print("{}".format(p.get_personal_shop()), end="")
            print("\n")
        print("\n\n")

    def battle_session(self, session_number):
        print("Battle session number:    {}".format(session_number))
        battle_pairs = np.array(list(map(lambda p: p.name, self.players)))
        np.random.shuffle(battle_pairs)
        battle_pairs = battle_pairs.reshape((4, 2))
        print("Battle pairs:\n{}".format(battle_pairs))
        print("\n\n")

    def generate_personal_shop(self, p):
        shop = self.pool.get_shop_for_level(p.get_level())
        return shop
