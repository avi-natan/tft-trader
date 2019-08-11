import numpy as np
import threading

from tfttrader.game import board


starting_hp = 100
starting_exp = 0
exp_gain = 4
starting_level = 1
starting_gold = 1

PASSIVE_GOLD_GAIN = 5


class Player:
    def __init__(self, game, name, strategy):
        self.game = game
        self.name = name
        self.hp = starting_hp
        self.exp = starting_exp
        self.level = starting_level
        self.gold = starting_gold
        self.max_field_champs = self.level
        self.board = board.Board()
        self.personal_shop = np.array([None, None, None, None, None])
        self.trading_strategy = strategy
        self.event = threading.Event()
        self.worker = threading.Thread(name=self.name + " Thread", target=self.trading_strategy.plan, args=(self,))
        self.should_end = False

    def to_string(self):
        string_rep = """Name:   {}
Hp:     {}
Exp:    {}
Level:  {}
Gold:   {}
Max field champs:   {}\n""".format(self.name, self.hp, self.exp, self.level, self.gold, self.max_field_champs)
        string_rep += "Board:   " + self.board.to_string()
        string_rep += "Shop:    {}".format(self.personal_shop) + "\n"
        string_rep += "Trading strategy:    {}\n\n".format(self.trading_strategy.to_string())

        return string_rep

    def get_level(self):
        return self.level

    def get_personal_shop(self):
        return self.personal_shop

    def update_gold(self):
        self.gold += PASSIVE_GOLD_GAIN

    def update_exp(self, amount=2):
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

    def set_personal_shop(self, shop):
        self.personal_shop = shop
