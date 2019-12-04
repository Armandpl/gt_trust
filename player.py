class Player:

    def __init__(self):
        self.coins = 0

    # gets opponent last move
    # returns 0 for cheat, 1 for cooperate
    def play(self, lastMove):
        raise NotImplementedError