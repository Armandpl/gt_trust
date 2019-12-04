from player import Player

class Cheat(Player):

    def __init__(self):
        super(Cheat, self).__init__()

    def play(self, lastmove):
        return 0