from cheat import Cheat
from cooperate import Cooperate
from copycat import Copycat
from random_player import RandomPlayer
import itertools
import random

generation = 10
rounds = 5

reward = 2

players = []

# initialize at least 10 players
players.append(Cheat("Veljko"))
players.append(Cheat("Paul"))
players.append(Cheat("Lucas"))
players.append(Cheat("Antoine"))
players.append(Cheat("Ramzy"))
players.append(Cheat("Colin"))
players.append(Cheat("Thomas"))
players.append(Cheat("Mehdi"))
players.append(Cheat("Thomas"))
players.append(Cheat("Florian"))
players.append(Cheat("Louis"))


# for each generation
for g in range(generation):

    random.shuffle(players)

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

    print("End of generation ",g)
    # print how much of each agent type is alive
    for p in range(len(players)):
        if type(players[p]) == type(Cheat('')):
            print("Player ",p,"\t Strategy : Cheat \t Name : ",players[p].name, "\t Coins ",players[p].coins)
        elif type(players[p]) == type(Cooperate('')):
            print("Player ",p,"\t Strategy : Cooperate\t Name : ",players[p].name, "\t Coins ",players[p].coins)
        elif type(players[p]) == type(Copycat('')):
            print("Player ",p,"\t Strategy : Copycat\t Name : ",players[p].name, "\t Coins ",players[p].coins)
        elif type(players[p] == type(RandomPlayer(''))):
            print("Player ",p,"\t Strategy : Random\t Name : ",players[p].name, "\t Coins ",players[p].coins)
    print("\n")

    #print("Cheaters : \t", cheat)
    #print("Cooperators : \t", coop)
    #print("Copycat : \t", copy)

    # reproduce the five top
    # kill the five last
    for w in range(5):
        if type(players[w]) == type(Cheat('')):
            players[len(players)-w-1] = Cheat(players[w].name)
        elif type(players[w]) == type(Cooperate('')):
            players[len(players)-w-1] = Cooperate(players[w].name)
        elif type(players[w]) == type(Copycat('')):
            players[len(players)-w-1] = Copycat(players[w].name)

    # reset coins
    for p in range(len(players)):
        players[p].coins = 0