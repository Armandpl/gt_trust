from player import Player

class Cooperate(Player):

    def __init__(self, name):
        super(Cooperate, self).__init__(name)

    def play(self, lastmove):
        self.coins = self.coins - 1
        return 1