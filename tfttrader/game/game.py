import numpy as np
import time

from tfttrader.game import pool, board


def init_boards():
    board_array = np.empty(8, dtype=board.Board)
    for i in range(0, 8):
        board_array[i] = board.Board("board_{}".format(i))
    return board_array


class Game:
    def __init__(self):
        self.pool = pool.Pool()
        self.boards = init_boards()
        self.alive_boards = 8

    def start(self):
        print(self.pool.quantities)
        for b in self.boards:
            print(b.to_string())

    def run(self):
        rnd = 1
        while self.alive_boards > 1:
            print("======================= Round {} start: =======================".format(rnd))
            self.planning_phase()
            self.battle_phase()
            print("======================= Round {} end: =======================\n\n".format(rnd))
            rnd += 1
        print("end of game. winner is {}".format(list(filter((lambda b: b.get_hp() != 0), self.boards))[0].get_board_name()))

    def planning_phase(self):
        print("------------------- Planning phase start: --------------------")
        # Recalling the units that were not bought to the pool
        for b in self.boards:
            self.pool.recall_personal_shop(b.get_personal_shop())

        # Updating player state and debug printing the player shop
        for b in self.boards:
            if b.get_hp() != 0:
                b.update_gold()
                b.update_exp()
                b.update_personal_shop(self.pool.get_shop_for_level(b.get_level()))
                print("Shop for player:     {}, level {}, gold {}, hp {}\n{}\n".format(b.board_name, b.get_level(), b.get_gold(), b.get_hp(), b.get_personal_shop()))

        # Waiting 30 seconds to allow player to do their planning
        time.sleep(1)
        print("------------------- Planning phase end: --------------------")

    def battle_phase(self):
        print("+++++++++++++++++++ Battle phase start: ++++++++++++++++++++")
        battle_pairs = np.array(list(map(lambda b: b.board_name, self.boards)))
        np.random.shuffle(battle_pairs)
        battle_pairs = battle_pairs.reshape((4, 2))
        print("Battle pairs:\n{}".format(battle_pairs))
        for pair in battle_pairs:
            b1 = list(filter(lambda b: b.get_board_name() == pair[0], self.boards))[0]
            prev_hp = b1.get_hp()
            b1.update_hp(-5)
            if b1.get_hp() == 0 and prev_hp != 0:
                self.alive_boards -= 1
            if self.alive_boards == 1:
                break
        print("++++++++++++++++++++ Battle phase end: +++++++++++++++++++++")
