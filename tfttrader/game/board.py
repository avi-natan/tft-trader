# passive object
import numpy as np
import math

STARTING_HP = 100
STARTING_EXP = 0
EXP_GAIN = 4
STARTING_LEVEL = 1
STARTING_GOLD = 1
STARTING_STREAK_COUNT = 0  # negative for losing streaks

STREAKS_GOLD = [0, 0, 1, 1, 2, 2, 3]


class Board:
    def __init__(self, board_name):
        self.board_name = board_name
        self.hp = STARTING_HP
        self.exp = STARTING_EXP
        self.level = STARTING_LEVEL
        self.gold = STARTING_GOLD
        self.streak_count = STARTING_STREAK_COUNT
        self.champ_traits = np.array([])
        self.items = np.array([])
        self.personal_shop = np.array([None, None, None, None, None])
        self.bench = np.array([None, None, None, None, None, None, None, None, None])
        self.field = np.array([[None, None, None, None, None, None, None],
                               [None, None, None, None, None, None, None],
                               [None, None, None, None, None, None, None]])

    def get_board_name(self):
        return self.board_name

    def get_hp(self):
        return self.hp

    def get_level(self):
        return self.level

    def get_gold(self):
        return self.gold

    def get_personal_shop(self):
        return self.personal_shop

    def update_hp(self, amount):
        self.hp += amount
        self.hp = max(self.hp, 0)

    def update_exp(self, amount=2):
        #  below are cumulative experience for each level
        self.exp += amount
        if self.exp >= 184:
            self.level = 9
        elif self.exp >= 114:
            self.level = 8
        elif self.exp >= 68:
            self.level = 7
        elif self.exp >= 38:
            self.level = 6
        elif self.exp >= 20:
            self.level = 5
        elif self.exp >= 10:
            self.level = 4
        elif self.exp >= 4:
            self.level = 3
        elif self.exp >= 2:
            self.level = 2

    def update_gold(self):
        s_c = abs(self.streak_count)
        new_gold = self.gold + min(5, self.level)
        new_gold += min(math.floor(self.gold / 10), 5)
        new_gold += (3 if s_c >= 7 else STREAKS_GOLD[s_c])
        self.gold = new_gold

    def update_personal_shop(self, shop):
        self.personal_shop = shop

    def to_string(self):
        string_rep = """Board Name:   {}
Hp:     {}
Exp:    {}
Level:  {}
Gold:   {}
Streak count:   {}
Champ traits:   {}
Items:          {}
Personal Shop: {}
Bench: {}
Field:
{}\n\n""".format(self.board_name, self.hp, self.exp, self.level, self.gold, self.streak_count,
                 self.champ_traits, self.items, self.personal_shop, self.bench, self.field)

        return string_rep
