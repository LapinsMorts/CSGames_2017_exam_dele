#!/usr/bin/python3
# -*- coding: utf-8 -*-

from GameManager import GameManager
from AI import AI
from Player import Player

print("""
#Bienvenue à Navire De Guerre, là où tout est meilleur en CLI!
#
#     Vous devez couler les navires adverses avant que les vôtres le soient.
#
#    Vous êtes Joueur1, votre AI est Joueur2.
#
#    GLHF!
#""")

# Generate the maps, done in the GameManager constructor
# print("Generating maps...")
game_manager = GameManager()

# Pour la correction, Player sera remplace par un autre AI qui affrontera
# l'autre. Tous les joueurs doivent avoir le game_manager pour pouvoir placer
# les bateaux et tirer. Les joueurs sont reconnus avec leur ID. Tu utilises le
# mauvais ID: tu t'attaques toi-meme. T'as juste a pas y toucher.

# for testing purposes, you can set the two players as AIs
# first_player = Player(game_manager, 1)
first_player = AI(game_manager, 0)
second_player = AI(game_manager, 1)

first_player.place_boats()
second_player.place_boats()

# Main game loop
# Les deux joueurs jouent a tour de role jusqu'a ce qu'au moins un des deux
# aie detruit tous les bateaux de l'autre
while not (game_manager.is_game_finished()):
    game_manager.print_grids()
    print("Joueur 1 : ")
    first_player.play()
    print("Joueur 2 : ")
    second_player.play()

game_manager.print_grids()
game_manager.print_winner()
