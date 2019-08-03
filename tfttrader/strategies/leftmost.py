from tfttrader.strategies.strategy import Strategy


class Leftmost(Strategy):
    def __init__(self):
        self.name = "Leftmost"

    def pick(self, player):
        print("picking leftmost")
