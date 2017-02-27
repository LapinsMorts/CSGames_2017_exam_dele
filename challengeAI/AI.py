#!/usr/bin/python
# -*- coding: utf-8 -*-

""" The AI class. Not really impressive as it is meant to be completed.
 The AI is supposed to play battleship """


class AI(object):
    """ The AI class is a Battleship AI to play the game. It basically places
     it's boats in the place_boats method and then implements the play
     function to play a turn"""

    def __init__(self, game_M, id_num):
        """ Initialisation function"""
        self._game_manager = game_M
        self._player_id = id_num
        self._i_coord = 0
        self._j_coord = 0

    def place_boats(self):
        """ Places the boats automaticly and randomly"""
        self._game_manager.place_boats(self._player_id)

    def play(self):
        """ Let's the AI play a turn"""
        if self._i_coord > 9:
            self._i_coord = 0
            self._j_coord += 1
        if self._j_coord > 9:
            self._j_coord = 0

        self._game_manager.shoot(self._player_id, self._j_coord, self._i_coord)
        self._i_coord += 1
