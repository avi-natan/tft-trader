from tfttrader.game import board


starting_hp = 100
starting_exp = 0
exp_gain = 4
starting_level = 1
starting_gold = 1


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = starting_hp
        self.exp = starting_exp
        self.level = starting_level
        self.gold = starting_gold
        self.max_field_champs = self.level
        self.board = board.Board()
        self.personal_shop = None
        self.trading_strategy = None

    def to_string(self):
        string_rep = """Name:   {}
Hp:     {}
Exp:    {}
Level:  {}
Gold:   {}
Max field champs:   {}\n""".format(self.name, self.hp, self.exp, self.level, self.gold, self.max_field_champs)
        string_rep += "Board:   " + self.board.to_string()
        string_rep += "Trading strategy:    {}\n\n".format(self.trading_strategy)

        return string_rep
