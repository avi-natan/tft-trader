# passive object
import numpy as np

STARTING_HP = 100
STARTING_EXP = 0
EXP_GAIN = 4
STARTING_LEVEL = 1
STARTING_GOLD = 1


class Board:
    def __init__(self, board_name):
        self.board_name = board_name
        self.hp = STARTING_HP
        self.exp = STARTING_EXP
        self.level = STARTING_LEVEL
        self.gold = STARTING_GOLD
        self.max_field_champs = self.level
        self.personal_shop = np.array([None, None, None, None, None])
        self.bench = np.array([None, None, None, None, None, None, None, None, None])
        self.field = np.array([[None, None, None, None, None, None, None],
                               [None, None, None, None, None, None, None],
                               [None, None, None, None, None, None, None]])

    def to_string(self):
        string_rep = """Board Name:   {}
Hp:     {}
Exp:    {}
Level:  {}
Gold:   {}
Max field champs:   {}
Personal Shop: {}
Bench: {}
Field:
{}\n\n""".format(self.board_name, self.hp, self.exp, self.level, self.gold, self.max_field_champs,
                 self.personal_shop, self.bench, self.field)

        return string_rep
