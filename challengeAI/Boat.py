#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np


class Boat:
    # a boat is mostly an array of 0s that turns to 1 once they are hit.
    # a boat full of 1 is a wreck

    def __init__(self, y, x, size, orientation):
        self._x_pos = x
        self._y_pos = y
        self._boat_size = size
        self._boat_orientation = orientation
        self._life_array = np.zeros(size)

    def get_hit(self, y, x):
        if self._boat_orientation == 'h':
            self._life_array[x - self._x_pos] = 1
        if self._boat_orientation == 'v':
            self._life_array[y-self._y_pos] = 1

    def is_new_hit(self, y, x):
        if (self._boat_orientation == 'h' and y == self._y_pos and
                x >= self._x_pos and x < self._x_pos + self._boat_size):
            return not self._life_array[x - self._x_pos]
        if (self._boat_orientation == 'v' and x == self._x_pos and
                y >= self._y_pos and y < self._y_pos + self._boat_size):
            return not self._life_array[y - self._y_pos]
        return False

    def is_wreck(self):
        # checks if the boat is all 1, if not, returns False
        return list(self._life_array).count(True) == len(self._life_array)

    def is_colliding(self, y, x, size, orientation):
        if self._boat_orientation == 'h':
            collides = False
            if orientation == 'h':
                for i in range(size):
                    collides = (collides or
                                y == self._y_pos and
                                x + i >= self._x_pos and
                                x + i < self._x_pos + self._boat_size)
            else:
                for i in range(size):
                    collides = (collides or
                                y + i == self._y_pos and
                                x >= self._x_pos and
                                x < self._x_pos + self._boat_size)
            return collides
        else:
            collides = False
            if orientation == 'h':
                for i in range(size):
                    collides = (collides or
                                x + i == self._x_pos and
                                y >= self._y_pos and
                                y < self._y_pos + self._boat_size)
            else:
                for i in range(size):
                    collides = (collides or
                                x == self._x_pos and
                                y + i >= self._y_pos and
                                y + i < self._y_pos + self._boat_size)
            return collides
