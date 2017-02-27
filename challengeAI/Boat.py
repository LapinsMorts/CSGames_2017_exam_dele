#!/usr/bin/python
# -*- coding: utf-8 -*-

""" This module contains the Boat class, which represents a Boat in the
 Battleship board game"""

import numpy as np


class Boat(object):
    """ a boat is mostly an array of 0s that turns to 1 once they are hit.
     a boat full of 1 is a wreck"""

    def __init__(self, y_pos, x_pos, size, orientation):
        """ Initialisation function"""
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._boat_size = size
        self._boat_orientation = orientation
        self._life_array = np.zeros(size)

    def get_hit(self, y_pos, x_pos):
        """ Lets a boat take a shot and have a tile marked as 1"""
        if self._boat_orientation == 'h':
            self._life_array[x_pos - self._x_pos] = 1
        if self._boat_orientation == 'v':
            self._life_array[y_pos - self._y_pos] = 1

    def is_new_hit(self, y_pos, x_pos):
        """ Tells if the boat is hit and has not been already hit there"""
        if (self._boat_orientation == 'h' and y_pos == self._y_pos and
                x_pos >= self._x_pos and
                x_pos < self._x_pos + self._boat_size):
            return not self._life_array[x_pos - self._x_pos]
        if (self._boat_orientation == 'v' and x_pos == self._x_pos and
                y_pos >= self._y_pos and
                y_pos < self._y_pos + self._boat_size):
            return not self._life_array[y_pos - self._y_pos]
        return False

    def is_wreck(self):
        """ checks if the boat is all 1, if not, returns False"""
        return list(self._life_array).count(True) == len(self._life_array)

    def is_colliding(self, y_pos, x_pos, size, orientation):
        """ Verifies if the boat collides with another one
        in the placement phase"""
        if self._boat_orientation == 'h':
            collides = False
            if orientation == 'h':
                for i in range(size):
                    collides = (collides or
                                y_pos == self._y_pos and
                                x_pos + i >= self._x_pos and
                                x_pos + i < self._x_pos + self._boat_size)
            else:
                for i in range(size):
                    collides = (collides or
                                y_pos + i == self._y_pos and
                                x_pos >= self._x_pos and
                                x_pos < self._x_pos + self._boat_size)
            return collides
        else:
            collides = False
            if orientation == 'h':
                for i in range(size):
                    collides = (collides or
                                x_pos + i == self._x_pos and
                                y_pos >= self._y_pos and
                                y_pos < self._y_pos + self._boat_size)
            else:
                for i in range(size):
                    collides = (collides or
                                x_pos == self._x_pos and
                                y_pos + i >= self._y_pos and
                                y_pos + i < self._y_pos + self._boat_size)
            return collides
