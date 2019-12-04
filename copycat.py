from player import Player

class Copycat(Player):

    def __init__(self):
        super(Copycat, self).__init__()

    # if round 0 : lastmove = -1
    def play(self, lastmove):
        if lastmove == -1:
            self.coins = self.coins - 1
            return 1
        else:
            if lastmove == 1:
                self.coins -= 1
            return lastmove