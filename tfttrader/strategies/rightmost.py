import time

from tfttrader.strategies.strategy import Strategy


class Rightmost(Strategy):
    def __init__(self):
        self.name = "Rightmost"

    def plan(self, player):
        while not player.should_end:
            print("\nThread {}: planning - READY".format(player.name))
            event_is_set = player.event.wait()
            if player.should_end:
                break
            print("\nThread {}: planning - RUNNING".format(player.name))
            while not player.should_stop_planning:
                time.sleep(4)
                print("\n{}\n".format(player.name))
            print("\nThread {}: planning - END".format(player.name))
            player.should_stop_planning = False
            player.event.clear()