#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This module contains the Player class, that represents a player"""

import sys


class Player(object):
    """ The class implements the actions a player will have to do to
    play the game"""

    def __init__(self, game_m, id_num):
        """ Initialise function"""
        self._game_manager = game_m
        self._player_id = id_num

    def place_boats(self):
        """ Places the boats rapidly and randomly"""
        self._game_manager.place_boats(self._player_id)

    def play(self):
        """ The function that lets the player play it's turn"""
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
                print "\nKTHXBYE"
                sys.exit(0)
            if is_bad_coords:
                print "Mauvaises coordonnées! "

        self._game_manager.shoot(self._player_id, y_coord, x_coord)

    @classmethod
    def check_bounds(cls, num):
        """ checks if the given number is between the 0-9 bounds"""
        return num >= 0 and num <= 9
