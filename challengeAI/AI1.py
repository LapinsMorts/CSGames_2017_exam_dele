#!/usr/bin/python3
# -*- coding: utf-8 -*-

from GameManager import GameManager


class AI1:

    def __init__(self, game_M, id_num):
        self._game_manager = game_M
        self._player_id = id_num
        self._i = 0
        self._j = 0

    def place_boats(self):
        # place les bateaux automatiquement et au hasard
        self._game_manager.place_boats(self._player_id)

    def play(self):
        if self._i > 9:
            self._i = 0
            self._j += 1
        if self._j > 9:
            self._j = 0

        self._game_manager.shoot(self._player_id, self._j, self._i)

        self._i += 1
