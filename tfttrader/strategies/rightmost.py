from tfttrader.strategies.strategy import Strategy


class Rightmost(Strategy):
    def __init__(self):
        self.name = "Rightmost"

    def pick(self, player):
        print("picking rightmost")
