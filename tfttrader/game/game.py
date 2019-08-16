import numpy as np

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

    def start(self):
        print(self.pool.quantities)
        for b in self.boards:
            print(b.to_string())
