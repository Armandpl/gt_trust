from player import Player

class Cooperate(Player):

    def __init__(self):
        super(Cooperate, self).__init__()

    def play(self, lastmove):
        self.coins = self.coins - 1
        return 1