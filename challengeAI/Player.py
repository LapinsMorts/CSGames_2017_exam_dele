#!/usr/bin/python3
# -*- coding: utf-8 -*-

from GameManager import GameManager
import sys


class Player:

    def __init__(self, game_M, id_num):
        self._game_manager = game_M
        self._player_id = id_num

    def place_boats(self):
        # place les bateaux automatiquement et au hasard
        self._game_manager.place_boats(self._player_id)

    def play(self):
        is_bad_coords = True
        y_coord = 0
        x_coord = 0
        while is_bad_coords:
            try:
                y_coord = input("Entrer la coordonnée Y (de 0 à 9) : ")
                x_coord = input("Entrer la coordonnée X (de 0 à 9) : ")
                is_bad_coords = not (self.check_bounds(x_coord) and
                                     self.check_bounds(y_coord))
            except (TypeError, SyntaxError, NameError, RuntimeError):
                is_bad_coords = True
            except KeyboardInterrupt:
                print("\nKTHXBYE")
                sys.exit(0)
            if is_bad_coords:
                print("Mauvaises coordonnées! ")

        self._game_manager.shoot(self._player_id, y_coord, x_coord)

    def check_bounds(self, num):
        return num >= 0 and num <= 9
