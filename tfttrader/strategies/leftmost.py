from tfttrader.strategies.strategy import Strategy


class Leftmost(Strategy):
    def __init__(self):
        self.name = "Leftmost"

    def plan(self, player):
        while not player.should_end:
            print("\nThread {}: planning - READY".format(player.name))
            event_is_set = player.event.wait()
            if player.should_end:
                break
            print("\nThread {}: planning - RUNNING".format(player.name))
            print("\nThread {}: planning - END".format(player.name))
            player.event.clear()

