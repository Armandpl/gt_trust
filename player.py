class Player:

    def __init__(self, name):
        self.coins = 0
        self.name = name

    # gets opponent last move
    # returns 0 for cheat, 1 for cooperate
    def play(self, lastMove):
        raise NotImplementedError