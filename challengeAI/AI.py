#!/usr/bin/python3
# -*- coding: utf-8 -*-

from GameManager import GameManager
import numpy as np


class AI:

    def __init__(self, game_M, id_num):
        self.game_manager = game_M
        self.player_id = id_num
        self.i = 0
        self.j = 0

    def place_boats(self):
        # place les bateaux automatiquement et au hasard
        self.game_manager.place_boats(self.player_id)

    def play(self):
        if self.i > 9:
            self.i = 0
            self.j = self.j + 1
        if self.j > 9:
            self.j = 0

        self.game_manager.shoot(self.player_id, self.j, self.i)

        self.i = self.i + 1
