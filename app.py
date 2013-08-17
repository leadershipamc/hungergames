from __future__ import division, print_function
from Game import Game
from bots import *
from Player import Player

# Bare minimum test game. See README.md for details.

if __name__ == '__main__':
    players = [Player()]
    for i in range(10):
        BoundedHunter(0.05*i,1)
        players.append(Alternator())
        players.append(MaxRepHunter())
        players.append(Freeloader())
        players.append(Pushover())
        players.append(FairHunter())
        players.append(AverageHunter())
    game = Game(players)
    game.play_game()
