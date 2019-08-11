from tfttrader.strategies.strategy import Strategy


class Rightmost(Strategy):
    def __init__(self):
        self.name = "Rightmost"

    def plan(self, player):
        while not player.should_end:
            print("\tTHREAD {}: WAITING FOR EVENT".format(player.name))
            event_is_set = player.event.wait()
            if player.should_end:
                break
            print("\tTHREAD {}: PLANNING IN THE CURRENT SESSION".format(player.name))
            player.event.clear()