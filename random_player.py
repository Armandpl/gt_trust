from player import Player
from random import randint

class RandomPlayer(Player):

    def __init__(self, name):
        super(RandomPlayer, self).__init__(name)

    def play(self, lastmove):
        if randint(0,1) == 0:
            return 0
        else:
            self.coins = self.coins - 1
            return 1