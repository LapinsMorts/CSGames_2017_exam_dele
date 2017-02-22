#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

class Boat:
#a boat is mostly an array of 0s that turns to 1 once they are hit.
#a boat full of 1s is a wreck

    def __init__(self, y, x, size, orientation):
        self.x_pos = x
        self.y_pos = y
        self.boat_size = size
        self.boat_orientation = orientation
        self.life_array = np.zeros(size)

    def get_hit(self, y, x):
        if self.boat_orientation == 'h':
            self.life_array[x - self.x_pos] = 1
        if self.boat_orientation == 'v':
            self.life_array[y-self.y_pos] = 1

    def is_new_hit(self, y, x):
        if self.boat_orientation == 'h' and y == self.y_pos and x >= self.x_pos and x < self.x_pos + self.boat_size:
            return not self.life_array[x - self.x_pos]
        if self.boat_orientation == 'v' and x == self.x_pos and y >= self.y_pos and y < self.y_pos + self.boat_size:
            return not self.life_array[y -self.y_pos]
        return False

#checks if the boat is all 1, if not, returns False
    def is_wreck(self):
        for i in range(0, self.boat_size):
            if not self.life_array[i]:
                return False
        return True

    def is_colliding(self, y, x, size, orientation):
        if self.boat_orientation == 'h':
            collides = False
            if orientation == 'h':
                for i in range(0,size):
                    collides = collides or y == self.y_pos and x + i >= self.x_pos and x + i < self.x_pos + self.boat_size
            else:
                for i in range(0,size):
                    collides = collides or y + i == self.y_pos and x >= self.x_pos and x < self.x_pos + self.boat_size
            return collides
        else:
            collides = False
            if orientation == 'h':
                for i in range(0,size):
                    collides = collides or x + i == self.x_pos and y >= self.y_pos and y < self.y_pos + self.boat_size
            else:
                for i in range(0,size):
                    collides = collides or x == self.x_pos and y+i >= self.y_pos and y+i < self.y_pos + self.boat_size
            return collides
