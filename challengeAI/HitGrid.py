#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This module contains the HitGrid class. It represents the map and is what
 the players and AIs are given to find their next shot"""

import numpy as np


class HitGrid(object):
    """ Represents the game map and marks where boats have been hit"""

    def __init__(self):
        """ Initialise function"""
        self._printable_grid = np.chararray((10, 10))
        self._printable_grid[:] = '~'

    def mark_hit(self, y_pos, x_pos):
        """ Marks the grid as hit"""
        self._printable_grid[y_pos, x_pos] = '#'

    def print_self(self):
        """ Prints the grid in a nice pattern"""
        print '  0 1 2 3 4 5 6 7 8 9'
        chaine = np.array_str(self._printable_grid)
        chaine = chaine.replace("'", "")
        chaine = chaine.replace('[', '')
        chaine = chaine.replace(']', '')
        chaine = '0 ' + chaine
        chaine = chaine[:22] + '1' + chaine[22:]
        chaine = chaine[:44] + '2' + chaine[44:]
        chaine = chaine[:66] + '3' + chaine[66:]
        chaine = chaine[:88] + '4' + chaine[88:]
        chaine = chaine[:110] + '5' + chaine[110:]
        chaine = chaine[:132] + '6' + chaine[132:]
        chaine = chaine[:154] + '7' + chaine[154:]
        chaine = chaine[:176] + '8' + chaine[176:]
        chaine = chaine[:198] + '9' + chaine[198:]
        print chaine

    def get_grid(self):
        """ return the current hit grid"""
        return self._printable_grid
