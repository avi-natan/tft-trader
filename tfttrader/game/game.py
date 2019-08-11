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
                player_array[i].worker.start()
            else:
                player_array[i] = player.Player(self, "player_{}".format(i), rightmost.Rightmost())
                player_array[i].worker.start()
        return player_array

    def start(self):
        print("\n{}".format(self.pool.quantities))
        for p in self.players:
            print(p.to_string())

    def run(self):
        i = 1
        while i <= 30:
            self.planning_session(i)
            self.battle_session(i)
            i += 1

        print("end of while loop")
        for p in self.players:
            p.should_end = True
            p.event.set()

    def planning_session(self, session_number):
        print("================== Planning session number: {} start ===================".format(session_number))
        for p in self.players:
            self.pool.recall_old_personal_shop(p.get_personal_shop())

        for p in self.players:
            p.update_gold()
            p.update_exp()
            p.set_personal_shop(self.pool.get_shop_for_level(p.get_level()))
            print("Shop for player:     {}, level {}\n{}\n".format(p.name, p.get_level(), p.get_personal_shop()))

        for p in self.players:
            p.event.set()

        all_ready = False
        while not all_ready:
            rdy = True
            for p in self.players:
                rdy &= not p.event.isSet()
            all_ready = rdy

        print("=================== Planning session number: {} end ====================".format(session_number))
        print("\n\n")

    def battle_session(self, session_number):
        print("+++++++++++++++++++ Battle session number: {} start ++++++++++++++++++++".format(session_number))
        battle_pairs = np.array(list(map(lambda p: p.name, self.players)))
        np.random.shuffle(battle_pairs)
        battle_pairs = battle_pairs.reshape((4, 2))
        print("Battle pairs:\n{}".format(battle_pairs))
        print("++++++++++++++++++++ Battle session number: {} end +++++++++++++++++++++".format(session_number))
        print("\n\n")

    def generate_personal_shop(self, p):
        shop = self.pool.get_shop_for_level(p.get_level())
        return shop
