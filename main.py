from cheat import Cheat
from cooperate import Cooperate
from copycat import Copycat
import itertools

generation = 10
rounds = 5

reward = 3

cheaters = 5
naive = 15
copycat = 10

players = []

for i in range(copycat):
    players.append(Copycat())

for i in range(cheaters):
    players.append(Cheat())

for i in range(naive):
    players.append(Cooperate())

# for each generation
for g in range(generation):
    print("Generation ",g)
    # print how much of each agent type is alive
    cheat = 0
    coop = 0
    copy = 0
    for p in range(len(players)):
        if type(players[p]) == type(Cheat()):
            cheat +=1
        elif type(players[p]) == type(Cooperate()):
            coop += 1
        elif type(players[p]) == type(Copycat()):
            copy += 1

    print("Cheaters : \t", cheat)
    print("Cooperators : \t", coop)
    print("Copycat : \t", copy)

    print("\n")

    # we have each player play 5 rounds against each others
    for p1, p2 in itertools.combinations(players, 2):

        last_move_p1 = -1
        last_move_p2 = -1
        for r in range(5):

            last_move_p1 = p1.play(last_move_p2)
            last_move_p2 = p2.play(last_move_p1)

            if (last_move_p1 + last_move_p2) == 2:
                p1.coins += reward
                p2.coins += reward
            elif last_move_p1 == 0 and last_move_p2 == 1:
                p1.coins += reward
            elif last_move_p1 == 1 and last_move_p2 == 0:
                p2.coins += reward

    players.sort(key=lambda x: x.coins, reverse=True)

    # reproduce the five top
    # kill the five last
    for w in range(5):
        if type(players[w]) == type(Cheat()):
            players[len(players)-w-1] = Cheat()
        elif type(players[w]) == type(Cooperate()):
            players[len(players)-w-1] = Cooperate()
        elif type(players[w]) == type(Copycat()):
            players[len(players)-w-1] = Copycat()

    # reset coins
    for p in range(len(players)):
        players[p].coins = 0