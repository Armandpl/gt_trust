from player import Player

class Cheat(Player):

    def __init__(self, name):
        super(Cheat, self).__init__(name)

    def play(self, lastmove):
        return 0